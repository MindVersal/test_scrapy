# -*- coding: utf-8 -*-
import scrapy
import time
import random


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = [
        # 'http://www.avito.ru/cherepovets',
        'http://www.avito.ru/cherepovets/dlya_biznesa',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
    ]

    def parse(self, response):
        for quote in response.css('.clearfix'):
            yield {
                'title': quote.css('.item-description-title-link::text').extract_first(),
                'price': quote.css('.about::text').extract_first(),
                'url': 'https://www.avito.ru{}'.format(
                    quote.css('a.item-description-title-link::attr(href)').extract_first()),
            }
        time.sleep(random.randint(3, 9))
        next_page = response.css('a.js-pagination-next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
