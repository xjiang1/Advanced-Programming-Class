import scrapy


class SnpSpider(scrapy.Spider):
    name = "snp_loop"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        number = response.xpath('//div[@class="table-responsive"]//tbody/tr/td[1]/text()').get()
        company = response.xpath('//div[@class="table-responsive"]//tbody/tr/td[2]/a/text()').get()
        symbol = response.xpath('//div[@class="table-responsive"]//tbody/tr/td[3]/a/text()').get()
        YTDreturn = response.xpath('//div[@class="table-responsive"]//tbody/tr/td[4]/text()').get()
        return {"number": number, "company": company, "symbol": symbol, "YTDreturn": YTDreturn}
