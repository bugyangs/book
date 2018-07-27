# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=()))
    )

    def parse(self, response):
        pass
