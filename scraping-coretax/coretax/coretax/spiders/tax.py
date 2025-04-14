import scrapy
from scrapy_splash import SplashRequest

# waiting render page
# lua_script = """
# function main(splash, args)
#     assert(splash:go(args.url))
    
#     while not splash:select('div.content-portal') do
#         splash:wait(0.1)
#         print('waiting...')
#     end
#     return {html=splash:html()}
# end
# """
lua_script = """
function main(splash, args)
    splash.images_enabled = false
    splash.js_enabled = true
    splash:go(args.url)
    splash:wait(2.0)  

    local max_wait = 10  
    local waited = 0

    while not splash:select("div.content-portal") and waited < max_wait do
        splash:wait(0.5)
        waited = waited + 0.5
    end

    return {
        html = splash:html(),
        url = splash:url()
    }
end
"""


class TaxSpider(scrapy.Spider):
    name = "tax"
    # allowed_domains = ["coretaxdjp.pajak.go.id"]
    # start_urls = ["https://coretaxdjp.pajak.go.id/accounting-portal/id-ID/balancesheet-light"]
    
    def start_requests(self):
        url = "https://coretaxdjp.pajak.go.id/accounting-portal/id-ID/balancesheet-light"
        yield SplashRequest(
            url,
            callback=self.parse,
            endpoint='execute',
            args={
                'wait': 5,  # Coba tunggu lebih lama untuk JS-heavy page
                'lua_source': lua_script,
                'timeout': 90  # Tambahkan ini juga kalau perlu
            },
            meta={'download_timeout': 120}
        )


    def parse(self, response):
        print("===================ok==========")
        print(response.text)
        pass
