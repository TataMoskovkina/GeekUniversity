# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Compose, Join, MapCompose, TakeFirst

def cleaner_photo(values):
    if values[:2] == '//':
        return f'http:{values}'
    return values

class AvitoparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    currency = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(cleaner_photo))
    car_brand = scrapy.Field(output_processor=Join())
    car_model = scrapy.Field(output_processor=Join())
    modification = scrapy.Field(output_processor=Join())
    year = scrapy.Field(output_processor=Join())
    mileage = scrapy.Field(output_processor=Join())
    num_doors = scrapy.Field(output_processor=Join())
    engine_type = scrapy.Field(output_processor=Join())
    transmission = scrapy.Field(output_processor=Join())
    drive = scrapy.Field(output_processor=Join())
    rudder = scrapy.Field(output_processor=Join())
    color = scrapy.Field(output_processor=Join())
    place_inspection = scrapy.Field(output_processor=Join())
    link = scrapy.Field(output_processor=TakeFirst())

