from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.items import AutoRiaItemLoader, AutoRiaItem


class AutoRiaSpider(CrawlSpider):
    name = "auto_ria_spider"

    start_urls = ['https://auto.ria.com/uk/legkovie/tesla']
    allowed_domains = ['auto.ria.com']
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]'],
                allow=r'https://auto.ria.com/uk/legkovie/tesla'), 'parse'
        ),
    )

    def parse(self, response, **kwargs):
        selector = Selector(response)
        l = AutoRiaItemLoader(AutoRiaItem(), selector)
        l.add_value("model", response.model)
        l.add_xpath("year", '//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]/div[2]/div[1]/div/a/text()')
        l.add_xpath("mileage", '//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]/div[2]/div[3]/ul/li[1]/text()')
        l.add_xpath("price_uah", '//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]/div[2]/div[2]/span/span[4]/span')
        l.add_xpath("price_usd", '//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]/div[2]/div[2]/span/span[1]')
        l.add_xpath("vin_code", '//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]/div[2]/div[3]'
                                '/div/span[2]/span[1]/text()[1]')
        l.add_xpath("reference", '//*[@id="catalogSearchAT"]/div[2]/section[1]/div[4]/div[2]/div[1]/div/a')
        return l.load_item()

