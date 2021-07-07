from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .models import Bill, Item, Consumer
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnly2
from .serializers import BillSerializer, ItemSerializer, ConsumerSerializer, UserSerializer

User = get_user_model()


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly2]

    def get_queryset(self):
        return Item.objects.filter(bill__user=self.request.user)


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly2]

    def get_queryset(self):
        return Consumer.objects.filter(bill__user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
