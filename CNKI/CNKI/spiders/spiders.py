import scrapy
from CNKI.items import CnkiItem
import re

class CNKISpider(scrapy.Spider):
    name = "cnki"

    '''
    def start_requests(self):
        urls = [
            # 'http://yuanjian.cnki.net/Search/LiteratureResult?ztcode=J159'
            'http://yuanjian.cnki.net/Search/ListResult'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''

    def start_requests(self):
        urls = [
            'http://yuanjian.cnki.net/Search/ListResult'
        ]
        formdata = {
            'searchType': 'MulityTermsSearch',
            'ParamIsNullOrEmpty': 'false',
            'Islegal': 'false',
            'Subject': 'J159',
            'Order': '2',
            'Page': '4',
            'ZtCode': 'J159',
        }
        for url in urls:
            for page in range(10):
                formdata['Page'] = str(page)
                yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        for a in response.xpath(".//p[@class='tit clearfix']/a"):
            href = a.xpath('./@href').extract()[0]
            if '/Article/' in href:
                title = a.xpath('./@title').extract()[0]
                yield scrapy.Request(url=href, callback=self.parse_paper, meta={'title': title, 'url': href})
            elif 'xuewen' in href:
                title = a.xpath('./@title').extract()[0]
                yield scrapy.Request(url=href, callback=self.parse_news, meta={'title': title, 'url': href})

    def parse_paper(self, response):
        if response.status is 200:
            item = CnkiItem()
            item['title'] = response.meta['title']
            item['href'] = response.meta['url']
            abstract = response.xpath(".//div[@style='text-align:left;word-break:break-all']/text()")[1].extract()
            item['abstract'] = abstract.strip()
            yield item
        else:
            print("response.status=%d" % response.status)

    def parse_news(self, response):
        if response.status is 200:
            item = CnkiItem()
            item['title'] = response.meta['title']
            item['href'] = response.meta['url']
            abstract = response.xpath('//div[@class="intro"]/p/text()')[0].extract()
            abstract = abstract.strip()
            try:
                abstract = re.sub('\.\.\.\\xa0(.|\n)*\(本文共\d页\)', '', abstract)
            finally:
                item['abstract'] = abstract.strip()
            yield item
        else:
            print("response.status=%d" % response.status)

