import scrapy
from sp500.items import Sp500Item


class SnpLoopSpider(scrapy.Spider):
    name = "snp_loop"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        stock = Sp500Item()
        rows = response.xpath('//div[@class="table-responsive"]//tbody/tr/]//tbody/tr')

        for row in rows[1:]:
            stock['number'] = row.xpath('td[1]/text()').get()
            stock['company'] = row.xpath('td[2]/a/text()').get()
            stock['symbol'] = row.xpath('td[3]/a/text()').get()
            stock['YTDreturn'] = row.xpath('td[4]/text()').get()
            yield stock