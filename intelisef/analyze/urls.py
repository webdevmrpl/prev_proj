from .views import *
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.BasicView)
urlpatterns = [
    path('', analyze, name='analyze'),
    path('data/', include(router.urls))
]
