__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers

from obis.views import AcctaxViewSet , ComtaxViewSet, SyntaxViewSet,HightaxViewSet,FedStatusViewSet,StStatusViewSet

from obis.views import SearchViewSet


router = routers.SimpleRouter()
router.register('acctax', AcctaxViewSet)
router.register('comtax', ComtaxViewSet)
router.register('syntax', SyntaxViewSet)
router.register('hightax',HightaxViewSet)
router.register('fedstatus',FedStatusViewSet)
router.register('ststatus',StStatusViewSet)


router.register('searchview',SearchViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
