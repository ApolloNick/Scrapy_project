# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join


class AutoRiaItem(scrapy.Item):
    model = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    price_uah = scrapy.Field()
    price_usd = scrapy.Field()
    vin_code = scrapy.Field()
    reference = scrapy.Field()


class AutoRiaItemLoader(ItemLoader):
    model_out = TakeFirst()
    year_out = TakeFirst()
    mileage = TakeFirst()
    price_uah_out = TakeFirst()
    price_usd_out = TakeFirst()
    vin_code_out = Join()
    reference_out = TakeFirst()
