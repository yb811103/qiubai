import scrapy

class QiubaiSpider(scrapy.spiders.Spider):
    name = "qiubai"
    start_urls = [
        "http://www.qiushibaike.com/"
    ]

    def parse(self, response):
	print response.xpath('//div[@class="content"]').extract()
