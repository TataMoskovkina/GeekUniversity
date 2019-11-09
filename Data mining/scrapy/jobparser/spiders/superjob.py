# -*- coding: utf-8 -*-
import scrapy
from jobparser.items import JobparserItem
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response):
        next_page = response.css('a.f-test-link-dalshe::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancy = response.css('div.f-test-vacancy-item a.icMQ_::attr(href)').get()

        for link in vacancy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response):
        #name = response.css('div._3mfro CuJz5 PlM3e _2JVkc _3LJqf::text').extract_first()
        #url_vacancy = response.url
        #min_salary = response.css('span._3mfro _2Wp8I ZON4b PlM3e _2JVkc::text').extract()
        #sourse = 'superjob.ru'
        #yield JobparserItem(name=name, url_vacancy=url_vacancy, min_salary=min_salary,
        #                    max_salary=None, source=sourse)
        loader = ItemLoader(item=JobparserItem(), response=response)
        loader.add_css('name', 'div._3mfro CuJz5 PlM3e _2JVkc _3LJqf::text')
        loader.add_value('url_vacancy', response.url)
        loader.add_css('min_salary', 'span._3mfro _2Wp8I ZON4b PlM3e _2JVkc::text')
        loader.add_value('max_salary', None)
        loader.add_value('source', 'superjob.ru')

