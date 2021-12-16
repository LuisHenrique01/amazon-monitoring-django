from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler
from products.models import HistoricModel, ProductModel
from products.scraping.scrap import get_price

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=7)
def update_historic():
    today = date.today()
    products = ProductModel.objects.exclude(historic_product__date=today)
    prices_day = []
    for product in products:
        price_day = get_price(product.asin)
        prices_day.append(HistoricModel(product=product,
                                        price=price_day))
    HistoricModel.objects.bulk_create(prices_day)


sched.start()
