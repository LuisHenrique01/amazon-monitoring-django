from django.urls import path

from products.api.viewsets import ProductHistoricView, ProductView, UserCreateView

urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('product/', ProductView.as_view()),
    path('product-historic/', ProductHistoricView.as_view())
]
