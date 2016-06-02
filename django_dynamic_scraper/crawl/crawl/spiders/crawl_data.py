from __future__ import unicode_literals
from dynamic_scraper.spiders.django_spider import DjangoSpider
from app.models import NewsWebsite, Data, CrawlItem



class DataSpider(DjangoSpider):

    name = 'whale'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(NewsWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Data
        self.scraped_obj_item_class = CrawlItem
        super(DataSpider, self).__init__(self, *args, **kwargs)