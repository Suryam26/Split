from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BillViewSet, ItemViewSet, ConsumerViewSet, UserViewSet


router = DefaultRouter()
router.register('bills', BillViewSet)
router.register('items', ItemViewSet)
router.register('consumers', ConsumerViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
