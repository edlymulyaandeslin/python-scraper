import scrapy


class TaxSpider(scrapy.Spider):
    name = "tax"
    allowed_domains = ["coretaxdjp.pajak.go.id"]
    start_urls = ["https://coretaxdjp.pajak.go.id/accounting-portal/id-ID/balancesheet-light"]

    def parse(self, response):
        print("===================ok==========")
        print(response.text)
        pass
