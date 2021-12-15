from datetime import date

from products.models import HistoricModel, ProductModel
from products.scraping.scrap import get_price


def update_historic():
    today = date.today()
    products = ProductModel.objects.exclude(historic_product__date=today)
    prices_day = []
    for product in products:
        price_day = get_price(product.asin)
        prices_day.append(HistoricModel(product=product,
                                        price=price_day))
    HistoricModel.objects.bulk_create(prices_day)
