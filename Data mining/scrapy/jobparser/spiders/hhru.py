# -*- coding: utf-8 -*-
import scrapy
from jobparser.items import JobparserItem
from scrapy.loader import ItemLoader

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?only_with_salary=false&clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=python']

    def parse(self, response):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse) #проходим по всем страницам

        vacancy = response.css(
        'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)'
        ).extract() #собираем ссылки на вакансии

        for link in vacancy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response):
        #name = response.css('div.vacancy-title h1.header::text').extract_first()
        url_vacancy = response.url
        #min_salary = response.css('meta[itemprop="minValue"]::attr(content)').extract_first()
        #max_salary = response.css('meta[itemprop="maxValue"]::attr(content)').extract_first()
        #source = 'hh.ru'
        #yield JobparserItem(name=name, url_vacancy=url_vacancy, min_salary=min_salary,
        #                    max_salary=max_salary, source=source)

        loader = ItemLoader(item=JobparserItem(), response=response)
        loader.add_css('name', 'div.vacancy-title h1.header::text')
        loader.add_value('url_vacancy', response.url)
        loader.add_css('min_salary', 'meta[itemprop="minValue"]::attr(content)')
        loader.add_css('max_salary', 'meta[itemprop="maxValue"]::attr(content)')
        loader.add_value('source', 'hh.ru')
