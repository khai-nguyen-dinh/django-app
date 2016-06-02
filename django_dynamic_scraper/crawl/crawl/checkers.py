from dynamic_scraper.spiders.django_checker import DjangoChecker
from app.models import Data


class DataChecker(DjangoChecker):

    name = 'whale-checker'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Data, **kwargs)
        self.scraper = self.ref_object.news_website.scraper
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(DataChecker, self).__init__(self, *args, **kwargs)