#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters, serializers
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
from rest_framework_csv.renderers import CSVRenderer
#from renderer import CustomBrowsableAPIRenderer
from obis.filters import AcctaxFilter,ComtaxFilter,SearchViewFilter
from obis.models import Acctax, Comtax, Syntax, Hightax, FedStatus,StStatus
from obis.models import SearchView 
from serializer import AcctaxSerializer,ComtaxSerializer

class obisGeneralViewSet(viewsets.ModelViewSet):
    def __init__(self,model):
        model=model
    model = self.model
    queryset = self.model.objects.all()
#    serializer_class =  ComtaxSerializer #serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
class SearchViewSet(viewsets.ReadOnlyModelViewSet):
    model = SearchView
    queryset = SearchView.objects.all()
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer,CSVRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = SearchViewFilter
    search_fields =('acode','sname','scientificnameauthorship','kingdom','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source','vernacularname')
    ordering_fields = ('acode','sname','scientificnameauthorship','kingdom','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source','vernacularname')    

class AcctaxViewSet(viewsets.ModelViewSet):
    """
    This is the Acctax list with source table hyperlinked.

    """
    model = Acctax
    queryset = Acctax.objects.all()
    serializer_class = AcctaxSerializer 
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer,CSVRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = AcctaxFilter
    search_fields =('acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source','comtax__vernacularname')
    ordering_fields = ('acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source')

class ComtaxViewSet(viewsets.ModelViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = Comtax
    queryset = Comtax.objects.all()
    serializer_class =  ComtaxSerializer #serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ComtaxFilter
    search_fields = ('acode','vernacularname',)

#'acctax__scientificnameauthorship','acctax__kingdom','acctax__phylum','acctax__taxclass',
#                    'acctax__taxorder','acctax__family','acctax__genus','acctax__species','acctax__subspecies','acctax__variety','acctax__forma',
#                    'acctax__elcode','acctax__iunccode','acctax__g_rank','acctax__s_rank','acctax__nativity','acctax__source')

class SyntaxViewSet(viewsets.ModelViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = Syntax
    queryset = Syntax.objects.all()
    #serializer_class = serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    #search_fields = ('acode','sname','scientificnameauthorship','family','genus','species','subspecies','variety')
#class LuSourceViewSet(viewsets.ModelViewSet):
#    model = LuSource
#    queryset = LuSource.objects.all() #.using('purple').all()
#    serializer_class = LuSourceSerializer
class HightaxViewSet(viewsets.ModelViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = Hightax
    queryset = Hightax.objects.all()
#    serializer_class =  ComtaxSerializer #serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
#    filter_class = ComtaxFilter
#    search_fields = ('acode','vernacularname',
class FedStatusViewSet(viewsets.ModelViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = FedStatus
    queryset = FedStatus.objects.all()
#    serializer_class =  ComtaxSerializer #serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
class StStatusViewSet(obisGeneralViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = StStatus
    #queryset = StStatus.objects.all()
#    serializer_class =  ComtaxSerializer #serializers.HyperlinkedModelSerializer
    #renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    #filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

