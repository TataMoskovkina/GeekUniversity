from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re
import random
import time

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1343 Yowser/2.5 Safari/537.36'

base_url = ('https://www.superjob.ru/')
url = ('https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bc%5D%5B0%5D=1')
html = requests.get(url, headers={'User-Agent': USER_AGENT}).text
parsed_html = bs(html, 'lxml')

vacancys = pd.DataFrame({'vacancy_name': [], 'requirements': [], 'salary_min': [], 'salary_max':[], 'currency': [], 'town':[], 'base_url': []})
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
            salary = salarys.split('—')
            sal = str(salary[1]).split(' ')
            salary_min = salary[0].replace(r'\xa', ' ')
            salary_max = sal[0].replace(r'\xa', ' ')
            currency = 'руб'
        elif 'от' in salarys:
            salary = salarys.split(' ')
            salary_min = salary[0].replace(r'\xa0', ' ')
            salary_max = ''
            currency = 'руб'
        elif 'По договорённости' in salarys:
            salary_min = 'По договорённости'
            salary_max = ''
            currency = ''
    except AttributeError:
        salary_min = ''
        salary_max = ''
        currency = ''
    town = vacancy.find('span', {'class': '_3mfro _9fXTd _2JVkc _3e53o _3Ll36'}).next.next.next.text
    requirements = vacancy.find('div', {'class':'_2kyiZ _2XXYS _2cxK3'}).text

    result = [vacancy_name, requirements, salary_min, salary_max, currency, town, base_url]

    return result

get_all_vacancy(url)

i = 0
for vacancy in vacancy_list:
    result = get_vacancy(vacancy)
    vacancys.loc[i] = result
    i += 1

vacancys.to_csv('superjob.csv', index=False)