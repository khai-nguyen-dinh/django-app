Requirements:
     + Python 2.7+ or 3.4+
     + Django 1.8/1.9
     + Scrapy 1.1
     + Scrapy-djangoitem 1.1
     + Python JSONPath RW 1.4+
     + Python future
     + scrapyd
     + django-celery

run:
scrapy crawl whale -a id=1 -a do_action=yes
run schedule:
python manage.py celeryd -l info -B --settings=djangoItem.settings
run check error:
scrapy crawl whale_checker -a id=ITEM_ID -a do_action=yes
