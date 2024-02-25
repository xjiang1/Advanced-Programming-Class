import scrapy


class SnpSpider(scrapy.Spider):
    name = "snp"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        ows = response.xpath('//table[@class="table table-hover table-borderless table-sm"]//tbody/tr')
        for row in rows:
            number = row.xpath('td[1]/text()').get()
            company = row.xpath('td[2]/a/text()').get()
            symbol = row.xpath('td[3]/a/text()').get()
            YTDreturn = row.xpath('td[4]/text()').get()
            yield {"number": number, "company": company, "symbol": symbol, "YTDreturn": YTDreturn}

