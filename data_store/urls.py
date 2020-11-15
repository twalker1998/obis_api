__author__ = 'mstacy'
from django.conf.urls import url
from data_store.views import MongoDataStore, DataStore, DataStoreDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('data/$', MongoDataStore.as_view(), name='data-list'),
    url('data/(?P<database>[^/]+)/$', MongoDataStore.as_view(), name='data-list'),
    url('data/(?P<database>[^/]+)/(?P<collection>[^/]+)/$', DataStore.as_view(), name='data-detail'),
    url('data/(?P<database>[^/]+)/(?P<collection>[^/]+)/(?P<id>[^/]+)/$', DataStoreDetail.as_view(), name='data-detail-id')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])