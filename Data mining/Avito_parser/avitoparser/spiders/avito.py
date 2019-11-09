# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avitoparser.items import AvitoparserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/sankt-peterburg/avtomobili']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.js-pagination-next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        ads_links = response.xpath('//a[@class="item-description-title-link"]/@href').extract()
        for link in ads_links:
            yield response.follow(link, self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('photos',
                             '//div[contains(@class, "gallery-img-wrapper")]//div[contains(@class, "gallery-img-frame")]/@data-url')
        loader.add_css('name',
                        'h1.title-info-title span.title-info-title-text::text')
        loader.add_xpath('price', '//span[@class="js-item-price"]/@content')
        loader.add_xpath('currency', '//span[@class="price-value-prices-list-item-currency_sign"]/@content')
        loader.add_xpath('car_brand', '//li[contains(@class, "item-params-list-item")][1]/text()')
        loader.add_xpath('car_model', '//li[contains(@class, "item-params-list-item")][2]/text()')
        loader.add_xpath('modification', '//li[contains(@class, "item-params-list-item")][4]/text()')
        loader.add_xpath('year', '//li[contains(@class, "item-params-list-item")][5]/text()')
        loader.add_xpath('mileage', '//li[contains(@class, "item-params-list-item")][6]/text()')
        loader.add_xpath('num_doors', '//li[contains(@class, "item-params-list-item")][11]/text()')
        loader.add_xpath('engine_type', '//li[contains(@class, "item-params-list-item")][12]/text()')
        loader.add_xpath('transmission', '//li[contains(@class, "item-params-list-item")][13]/text()')
        loader.add_xpath('drive', '//li[contains(@class, "item-params-list-item")][14]/text()')
        loader.add_xpath('rudder', '//li[contains(@class, "item-params-list-item")][15]/text()')
        loader.add_xpath('color', '//li[contains(@class, "item-params-list-item")][16]/text()')
        loader.add_xpath('place_inspection', '//li[contains(@class, "item-params-list-item")][18]/text()')
        loader.add_value('link', response.url)
        yield loader.load_item()
