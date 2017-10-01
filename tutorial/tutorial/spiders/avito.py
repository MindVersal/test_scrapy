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
        # 'http://www.avito.ru/cherepovets/rabota',
        # 'http://www.avito.ru/cherepovets/uslugi',
        # 'http://www.avito.ru/cherepovets/zhivotnye',
        # 'http://www.avito.ru/cherepovets/hobbi_i_otdyh',
        # 'http://www.avito.ru/cherepovets/nedvizhimost',
        # 'http://www.avito.ru/cherepovets/telefony',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/tovary_dlya_kompyutera',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/audio_i_video',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/igry_pristavki_i_programmy',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/fototehnika',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/orgtehnika_i_rashodniki',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/planshety_i_elektronnye_knigi',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/noutbuki',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/nastolnye_kompyutery',  # bytovaya_elektronika
        # 'http://www.avito.ru/cherepovets/mebel_i_interer',  # dlya_doma_i_dachi
        # 'http://www.avito.ru/cherepovets/remont_i_stroitelstvo',  # dlya_doma_i_dachi
        # 'http://www.avito.ru/cherepovets/bytovaya_tehnika',  # dlya_doma_i_dachi
        # 'http://www.avito.ru/cherepovets/posuda_i_tovary_dlya_kuhni',  # dlya_doma_i_dachi
        # 'http://www.avito.ru/cherepovets/rasteniya',  # dlya_doma_i_dachi
        # 'http://www.avito.ru/cherepovets/produkty_pitaniya',  # dlya_doma_i_dachi
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
        # 'http://www.avito.ru/cherepovets',
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
