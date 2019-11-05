from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import unicodedata
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from vacancy_to_sql import Vacancy, Base

client = MongoClient('localhost',27017)
vacancy_db = client.vacancy_db
vacancys_hh = vacancy_db.vacancys_hh

engine = create_engine('sqlite:///vacancy.db',echo=True)
Base = declarative_base()

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1343 Yowser/2.5 Safari/537.36'

base_url = ('https://hh.ru')
url = ('https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=python&showClusters=true')
html = requests.get(url, headers={'User-Agent': USER_AGENT}).text
parsed_html = bs(html, 'lxml')

vacancys = pd.DataFrame({'vacancy_name': [], 'requirements': [], 'salary_min': [], 'salary_max':[],
                         'currency': [], 'town': [], 'vacancy_url': [], 'base_url': []})
vacancy_list = []

def get_next_page(parsed_html):
    try:
        next_page = parsed_html.find('a', attrs={'class': 'HH-Pager-Controls-Next'}).get('href')
        url_next_page = base_url + next_page

    except AttributeError:
        url_next_page = base_url
    return url_next_page

def get_all_vacancy(url):
    html = requests.get(url, headers={'User-Agent': USER_AGENT}).text
    parsed_html = bs(html, 'lxml')
    vacancy_list.extend(parsed_html.findAll('div', {'class': 'vacancy-serp-item'}))
    url_next_page = get_next_page(parsed_html)
    if url_next_page == base_url:
        return vacancy_list
    else:
        get_all_vacancy(url_next_page)

def get_vacancy(vacancy):
    vacancy_name = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text
    try:
        salarys = vacancy.find('div', {'class': 'vacancy-serp-item__compensation'}).text
        if '-' in salarys:
            salary = salarys.split('-')
            sal = str(salary[1]).split(' ')
            salary_min = int(unicodedata.normalize("NFKD", salary[0]).replace(' ', ''))
            salary_max = int(unicodedata.normalize("NFKD", sal[0]).replace(' ', ''))
            currency = sal[1]
        elif 'от' in salarys:
            salary = salarys.split(' ')
            salary_min = int(unicodedata.normalize("NFKD", salary[1]).replace(' ', ''))
            salary_max = None
            currency = salary[2]
        elif 'до' in salarys:
            salary = salarys.split(' ')
            salary_max = int(unicodedata.normalize("NFKD", salary[1]).replace(' ', ''))
            salary_min = None
            currency = salary[2]
    except AttributeError:
        salary_min = None
        salary_max = None
        currency = None
    vacancy_url = vacancy.find('a', attrs={'class':'HH-LinkModifier'}).get('href')
    town = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    requirements = vacancy.find('div', {'data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).text

    result = {'vacancy_name':vacancy_name, 'requirements':requirements, 'salary_min':salary_min,
              'salary_max':salary_max, 'currency':currency, 'town':town, 'vacancy_url':vacancy_url,
              'base_url':base_url}
    vac_sql = Vacancy(vacancy_name, requirements, salary_min, salary_max, currency, town, vacancy_url, base_url)

    return result, vac_sql

get_all_vacancy(url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

i = 0
for vacancy in vacancy_list:
    result, vac_to_sql = get_vacancy(vacancy)
    vacancys.loc[i] = result
    vacancys_hh.update_one({'vacancy_url': result['vacancy_url']},
                        {'$set': result},
                        upsert=True)
    session.add(vac_to_sql)
    i += 1

session.commit()
session.close()

#objects = vacancys_hh.find({'salary_min': {'$gte': 100000}}, {'vacancy_name', 'salary_min', 'vacancy_url'})
#for obj in objects:
#    pprint(obj)

#vacancys.to_csv('hhru.csv', index=False)

