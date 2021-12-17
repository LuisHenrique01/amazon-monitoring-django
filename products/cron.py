from products.scrap import get_price
from products.models import HistoricModel, ProductModel
from datetime import date


def update_historic():
    today = date.today()
    products = ProductModel.objects.exclude(historic_product__date=today)
    prices_day = []
    for product in products:
        price_day = get_price(product.asin)
        prices_day.append(HistoricModel(product=product,
                                        price=price_day))
    HistoricModel.objects.bulk_create(prices_day)
