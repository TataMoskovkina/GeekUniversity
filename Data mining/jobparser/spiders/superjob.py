# -*- coding: utf-8 -*-
import scrapy
from jobparser.items import JobparserItem

class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bc%5D%5B0%5D=1']

    def parse(self, response):
        next_page = response.css('a.f-test-link-dalshe::attr(href)').extract_first()
        if not next_page:
            pass
        yield response.follow(next_page, callback=self.parse)

        vacancy = response.css('div.f-test-vacancy-item a[target="_blank"]::attr(href)').extract_first()

        for link in vacancy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response):
        name = response.css('div._3mfro CuJz5 PlM3e _2JVkc _3LJqf::text').extract_first()
        url_vacancy = response.url
        min_salary = response.css('span._3mfro _2Wp8I ZON4b PlM3e _2JVkc::text').extract()
        sourse = 'superjob.ru'
        yield JobparserItem(name=name, url_vacancy=url_vacancy, min_salary=min_salary,
                            max_salary=None, source=sourse)


