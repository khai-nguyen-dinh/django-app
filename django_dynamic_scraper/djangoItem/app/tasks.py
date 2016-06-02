from celery.task import task
from django.db.models import Q
from dynamic_scraper.utils.task_utils import TaskUtils
from app.models import NewsWebsite, Data

@task()
def run_spiders():
    t = TaskUtils()
    args = (Q(name='egg'),)
    t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'whale', *args, **kwargs)

@task()
def run_checkers():
    t = TaskUtils()
    args = (Q(id__gt=100),)
    t.run_checkers(Data, 'news_website__scraper', 'checker_runtime', 'whale_checker', *args, **kwargs)