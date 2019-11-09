# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient

class AvitoparserPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except TypeError as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

class DataBasePipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.avito_cars

    def process_item(self, item, spider):
        item['price'] = int(item['price'])
        item['year'] = int(item['year'])
        item['num_doors'] = int(item['num_doors'])
        item['car_model'] = item['car_model'].strip()
        item['car_brand'] = item['car_brand'].strip()
        item['modification'] = item['modification'].strip()
        item['engine_type'] = item['engine_type'].strip()
        item['transmission'] = item['transmission'].strip()
        item['drive'] = item['drive'].strip()
        item['rudder'] = item['rudder'].strip()
        item['color'] = item['color'].strip()
        item['place_inspection'] = item['place_inspection'].strip()
        item['car_model'] = item['car_model'].strip()
        item['mileage'] = item['mileage'].replace('\xa0', ' ').strip()

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item