BOT_NAME = 'quotestoscrape'

SPIDER_MODULES = ['quotestoscrape.spiders']
NEWSPIDER_MODULE = 'quotestoscrape.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

SPLASH_URL = 'http://127.0.0.1:8050'
