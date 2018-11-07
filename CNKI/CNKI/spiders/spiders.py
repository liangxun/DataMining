import scrapy
from CNKI.items import CnkiItem

class CNKISpider(scrapy.Spider):
    name = "cnki"

    def start_requests(self):
        urls = [
            'http://yuanjian.cnki.net/Search/LiteratureResult?ztcode=J159'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.xpath(".//p[@class='tit clearfix']/a"):
            item = CnkiItem()
            item['href'] = a.xpath('./@href').extract()[0]
            item['title'] = a.xpath('./@title').extract()[0]
            yield item
