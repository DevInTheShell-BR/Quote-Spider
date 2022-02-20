import scrapy
from scrapy.loader.processors import TakeFirst


class QuoteItem(scrapy.Item):
    quote = scrapy.Field(output_processor=TakeFirst())
    author = scrapy.Field(output_processor=TakeFirst())
    tags = scrapy.Field()
