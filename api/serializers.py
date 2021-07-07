from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueTogetherValidator

from .models import Bill, Item, Consumer

User = get_user_model()


class BillSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True, view_name='item-detail', read_only=True)
    consumers = serializers.HyperlinkedRelatedField(
        many=True, view_name='consumer-detail', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bill
        fields = ['id', 'url', 'title', 'date',
                  'items', 'consumers', 'user', 'created_at']
        validators = [
            UniqueTogetherValidator(
                queryset=Bill.objects.all(),
                fields=['title', 'user']
            )
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'cost', 'bill']
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=['name', 'bill']
            )
        ]


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['id', 'name', 'bill', 'items']
        validators = [
            UniqueTogetherValidator(
                queryset=Consumer.objects.all(),
                fields=['name', 'bill']
            )
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email']


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user
