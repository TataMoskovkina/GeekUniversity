# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import unicodedata

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.scrapy_vacancy

    def process_item(self, item, spider):
        if spider.name == 'superjob':
            salary_min, salary_max = self.get_salary(item['min_salary'])
            item['min_salary'] = salary_min
            item['max_salary'] = salary_max

        else:
            if not item['min_salary'] :
                pass
            else:
                try:
                    item['min_salary'] = int(item['min_salary'])
                except ValueError:
                    pass
            if not item['max_salary']:
                pass
            else:
                try:
                    item['max_salary'] = int(item['max_salary'])
                except ValueError:
                    pass

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

    def get_salary(self,salary):
        try:
            if '—' in salary:
                salary = unicodedata.normalize("NFKD", salary).split('—')
                sal = str(salary[1]).split(' ')
                salary_min = int(salary[0].replace(' ', ''))
                salary_max = int(sal[1] + sal[2])
            elif 'от' in salary:
                salary = salary.split(' ')
                sal = unicodedata.normalize("NFKD", salary[0]).split(' ')
                salary_min = int(sal[1] + sal[2])
                salary_max = None
            elif 'По договорённости' in salary:
                salary_min = 'По договорённости'
                salary_max = None
            else:
                salary = unicodedata.normalize("NFKD", salary).split(' ')
                salary_min = int(salary[0] + salary[1])
                salary_max = None
        except AttributeError:
            salary_min = None
            salary_max = None

        return salary_min, salary_max
