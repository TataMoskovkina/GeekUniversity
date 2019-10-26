from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import unicodedata
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from vacancy_to_sql import Vacancy, Base

client = MongoClient('localhost',27017)
vacancy_db = client.vacancy_db
superjob = vacancy_db.superjob

engine = create_engine('sqlite:///vacancy.db',echo=True)
Base = declarative_base()

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1343 Yowser/2.5 Safari/537.36'

base_url = ('https://www.superjob.ru')
url = ('https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bc%5D%5B0%5D=1')
html = requests.get(url, headers={'User-Agent': USER_AGENT}).text
parsed_html = bs(html, 'lxml')

vacancys = pd.DataFrame({'vacancy_name': [], 'requirements': [], 'salary_min': [], 'salary_max':[], 'currency': [],
                         'town':[], 'vacancy_url': [], 'base_url': []})
vacancy_list = []

def get_next_page(parsed_html):
    try:
        next_page = parsed_html.find('a', attrs={'class': 'f-test-link-dalshe'}).get('href')
        url_next_page = base_url + next_page

    except AttributeError:
        url_next_page = base_url
    return url_next_page

def get_all_vacancy(url):
    html = requests.get(url, headers={'User-Agent': USER_AGENT}).text
    parsed_html = bs(html, 'lxml')
    vacancy_list.extend(parsed_html.findAll('div', {'class': 'f-test-vacancy-item'}))
    url_next_page = get_next_page(parsed_html)
    if url_next_page == base_url:
        return vacancy_list
    else:
        get_all_vacancy(url_next_page)

def get_vacancy(vacancy):
    vacancy_name = vacancy.find('div', {'class': '_3mfro CuJz5 PlM3e _2JVkc _3LJqf'}).text
    try:
        salarys = vacancy.find('span', {'class': 'f-test-text-company-item-salary'}).text
        if '—' in salarys:
            salary = unicodedata.normalize("NFKD", salarys).split('—')
            sal = str(salary[1]).split(' ')
            salary_min = int(salary[0].replace(' ', ''))
            salary_max = int(sal[1]+sal[2])
            currency = 'руб'
        elif 'от' in salarys:
            salary = salarys.split(' ')
            sal = unicodedata.normalize("NFKD", salary[0]).split(' ')
            salary_min = int(sal[1]+sal[2])
            salary_max = None
            currency = 'руб'
        elif 'По договорённости' in salarys:
            salary_min = 'По договорённости'
            salary_max = None
            currency = None
        else:
            salary = unicodedata.normalize("NFKD", salarys).split(' ')
            salary_min = int(salary[0]+salary[1])
            salary_max = None
            currency = 'руб'
    except AttributeError:
        salary_min = None
        salary_max = None
        currency = None

    town = vacancy.find('span', {'class': '_3mfro _9fXTd _2JVkc _3e53o _3Ll36'}).next.next.next.text
    requirements = vacancy.find('div', {'class':'_2kyiZ _2XXYS _2cxK3'}).text
    vacancy_url = base_url + vacancy.find('div', attrs={'class': '_3mfro CuJz5 PlM3e _2JVkc _3LJqf'}).findParent()['href']

    result = {'vacancy_name': vacancy_name, 'requirements': requirements,
              'salary_min': salary_min, 'salary_max': salary_max, 'currency': currency,
              'town': town, 'vacancy_url': vacancy_url, 'base_url': base_url}
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
    superjob.update_one({'vacancy_url': result['vacancy_url']},
                        {'$set': result},
                        upsert=True)
    session.add(vac_to_sql)
    i += 1

session.commit()
session.close()

#objects = superjob.find({'salary_min': {'$gte': 100000}}, {'vacancy_name', 'salary_min', 'vacancy_url'})
#for obj in objects:
#    pprint(obj)

#vacancys.to_csv('superjob.csv', index=False)

