from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework import permissions, generics
from rest_framework import status
from rest_framework.response import Response

from products.api.serializers import ProductHistoricSerializer, ProductSerializer, UserCreateSerializer
from products.models import ProductModel
from products.scrap import get_asin, get_name


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        url = request.data['url']
        data = {'user': request.user.id,
                'name': get_name(url),
                'asin': get_asin(url)}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductHistoricView(generics.RetrieveDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductHistoricSerializer
