# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 02:41:55 2019

@author: Наталия
"""

import requests
import json

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1343 Yowser/2.5 Safari/537.36'

weatherstack_api_url = 'http://api.weatherstack.com/current'

params = {'access_key': '042218ea528404840683f91018b70d77',
          'query' : 'Saint Petersburg'}
response = requests.get(f'{weatherstack_api_url}', params, headers={'User-Agent':USER_AGENT})

data = response.json()

with open('weather.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

