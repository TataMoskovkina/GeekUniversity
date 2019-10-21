# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:31:42 2019

@author: Наталия
"""

import requests
import json

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1343 Yowser/2.5 Safari/537.36'

github_api_url = 'https://api.github.com/users/'

user_name = 'GefMar'

response = requests.get(f'{github_api_url}{user_name}', headers={'User-Agent': USER_AGENT})
data = response.json()

repos_url = data.get('repos_url')
repos = requests.get(f'{repos_url}', headers={'User-Agent': USER_AGENT})

data_rep = repos.json()

with open('repos.json', 'w', encoding='utf-8') as file:
    json.dump(data_rep, file, indent=2, ensure_ascii=False)

'''for i in data_rep:
    print(i['name'])'''
