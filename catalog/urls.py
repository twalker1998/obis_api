_author__ = 'mstacy'
from django.conf.urls import url
from catalog.views import Catalog,CatalogData, CatalogDataDetail # SourceList, SourceDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url('data/$', Catalog.as_view(),name='catalog-list'),
    url('data/(?P<database>[^/]+)/$',Catalog.as_view(),name='catalog-list'),
    url('data/(?P<database>[^/]+)/(?P<collection>[^/]+)/$',CatalogData.as_view(),name='catalog-detail'),
    url('data/(?P<database>[^/]+)/(?P<collection>[^/]+)/(?P<id>[^/]+)/$', CatalogDataDetail.as_view(), name='catalog-detail-id')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
