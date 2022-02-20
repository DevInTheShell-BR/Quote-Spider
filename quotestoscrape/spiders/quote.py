import scrapy
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from quotestoscrape.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(2))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='http://quotes.toscrape.com/js',
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script
            })

    def parse(self, response):
        """ This functions parses quotes 

        @url http://quotes.toscrape.com/js
        @returns items 1 10
        @scrapes quote author tags
        """
        items = response.xpath("//div[@class='quote']")
        for item in items:
            quote_loader = ItemLoader(
                item=QuoteItem(),
                response=response
            )

            quote_loader.add_value('quote',
                                   item.xpath(".//span[@class='text']/text()").get()[1:-1])
            quote_loader.add_value('author',
                                   item.xpath(".//span[2]/small[@class='author']/text()").get())
            quote_loader.add_value('tags', item.xpath(
                ".//div[@class='tags']/a/text()").getall())

            yield quote_loader.load_item()

        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page:
            absolute_url = "http://quotes.toscrape.com" + next_page
            yield SplashRequest(
                url=absolute_url,
                callback=self.parse,
                endpoint='execute',
                args={
                    'lua_source': self.script
                })
