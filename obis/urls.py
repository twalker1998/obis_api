__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers

from obis.views import AcctaxViewSet , ComtaxViewSet, SyntaxViewSet,SearchViewSet


router = routers.SimpleRouter()
router.register('acctax', AcctaxViewSet)
router.register('comtax', ComtaxViewSet)
router.register('syntax', SyntaxViewSet)
router.register('searchview',SearchViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
