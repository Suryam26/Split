from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Bill, Item, Consumer

User = get_user_model()


class BillSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True, view_name='item-detail', read_only=True)
    consumers = serializers.HyperlinkedRelatedField(
        many=True, view_name='consumer-detail', read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Bill
        fields = ['id', 'url', 'name', 'date', 'items', 'consumers', 'user']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'cost', 'bill']


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['id', 'name', 'bill', 'items']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email']
