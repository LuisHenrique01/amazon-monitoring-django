from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from products.models import HistoricModel, ProductModel
from products.scrap import get_price


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            product = ProductModel.objects.get(asin=validated_data['asin'])
            user = validated_data['user']
            product.user.add(user)
        except ObjectDoesNotExist:
            product = ProductModel.objects.create(**validated_data)
            _ = HistoricModel.objects.create(
                product=product, price=get_price(product.asin))
            return product


class HistoricSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricModel
        fields = '__all__'


class ProductHistoricSerializer(serializers.ModelSerializer):
    historic = HistoricSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = ['name', 'asin', 'historic']
