#My Import
from profiles_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tvlink',views.LiveTvViewSet)
router.register('adservice',views.AdserviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]