#My Import
from django.conf.urls.static import static

from profiles_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_project import settings

router = DefaultRouter()
router.register('tvlink',views.LiveTvViewSet)
router.register('adservice',views.AdserviceViewSet)
router.register('matchschedule',views.MatchSchedule)

urlpatterns = [
    path('', include(router.urls)),
]