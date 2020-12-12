__author__ = 'Tyler Walker' # twalker1998@gmail.com
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CheckUUIDView

router = routers.SimpleRouter()
router.register('checkUuid', CheckUUIDView, basename='checkUuid')

urlpatterns = [
    url(r'^', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json'])
