import scrapy
from sipdscraper.items import QuoteItem

from scrapy_splash import SplashRequest

# waiting render page
lua_script = """
function main(splash, args)
    assert(splash:go(args.url))
    
    while not splash:select('div.quote') do
        splash:wait(0.1)
        print('waiting...')
    end
    return {html=splash:html()}
end
"""

# scrolling render page
# lua_script = """
# function main(splash, args)
#     local num_scrolls = 10
#     local scroll_delay = 1.0
    
#     local scroll_to = splash:jsfunc("window.scrollTo")
#     local get_body_height = splash:jsfunc(
#         "function() {return document.body.scrollHeight;}"
#     )
    
#     assert(splash:go(splash.args.url))
#     splash:wait(splash.args.wait)
    
#     for _ = 1, num_scrolls do
#         scroll_to(0, get_body_height())
#         splash:wait(scroll_delay)
#     end
#     return splash:html()
# end
# """

class SipdspiderSpider(scrapy.Spider):
    name = "sipdspider"
    allowed_domains = ["sipd.kemendagri.go.id"]
    start_urls = ["https://sipd.kemendagri.go.id/penatausahaan/pengeluaran/sp2d/pencairan"]

    # def start_requests(self):
    #     url = "https://sipd.kemendagri.go.id/penatausahaan/pengeluaran/sp2d/pencairan"
    #     yield SplashRequest(
    #             url, 
    #             callback=self.parse, 
    #             endpoint='execute',
    #             args={ 'wait': 0.5 
    #                 'lua_source': lua_script, 
    #                 url: 'https://sipd.kemendagri.go.id/penatausahaan/pengeluaran/sp2d/pencairan'
    #             }
    #         )

    def parse(self, response):
        # quote_item = QuoteItem()
        # for quote in response.css("div.quote"):
        #     quote_item['text'] = quote.css("span.text::text").get()
        #     quote_item['author'] = quote.css("small.author::text").get()
        #     quote_item['tags'] = quote.css("div.tags a.tag::text").getall()
        #     yield quote_item
        
        print("+++++++++++OKKKK++++++++++++++")
        print(response.text)