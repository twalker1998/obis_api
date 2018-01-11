from rest_framework import viewsets, filters, serializers
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from obis.filters import AcctaxFilter,ComtaxFilter #,SearchViewFilter
from obis.models import Acctax,Comtax,Syntax,Hightax,FedStatus,StStatus,OkSwap,RankChange
from obis.models import Occurrence,Source,Institution,County,CoTrs,IdentificationVerification
from obis.models import SpatialRefSys, VwSearch, VwSearchmv #SearchView
from serializer import AcctaxSerializer,ComtaxSerializer, SourceSerializer

#DB Table ViewSet Class
class obisTableViewSet(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#DB View ViewSet Class
class obisViewViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer,CSVRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#***************************************** OBIS Tables **********************************************************
class AcctaxViewSet(obisTableViewSet):
    """
    This is the Acctax ViewSet with hyperlinked tables.
    """
    model = Acctax
    queryset = Acctax.objects.all()
    #serializer_class = AcctaxSerializer
    filter_class = AcctaxFilter
    search_fields = ('acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus',
                    'species','subspecies','variety','forma','elcode','gelcode','iunccode','g_rank','s_rank',
                    'nativity','source','comtax__vernacularname')
    ordering_fields = ('acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus',
                    'species','subspecies','variety','forma','elcode','gelcode','iunccode','g_rank','s_rank',
                    'nativity','source')

class ComtaxViewSet(obisTableViewSet):
    """
    This is the Comtax ViewSet with hyperlinked tables.
    """
    model = Comtax
    queryset = Comtax.objects.all()
    #serializer_class =  ComtaxSerializer
    filter_class = ComtaxFilter
    search_fields = ('acode','vernacularname',)

class SyntaxViewSet(obisTableViewSet):
    """
    This is the Syntax ViewSet with hyperlinked tables.
    """
    model = Syntax
    queryset = Syntax.objects.all()

class HightaxViewSet(obisTableViewSet):
    """
    This is the Hightax ViewSet with hyperlinked tables.
    """
    model = Hightax
    queryset = Hightax.objects.all()

class FedStatusViewSet(obisTableViewSet):
    """
    This is the Fed Status ViewSet with hyperlinked tables.
    """
    model = FedStatus
    queryset = FedStatus.objects.all()

class StStatusViewSet(obisTableViewSet):
    """
    This is the State Status ViewSet with hyperlinked tables.
    """
    model = StStatus
    queryset = StStatus.objects.all()

class OkSwapViewSet(obisTableViewSet):
    """
    This is the Ok Swap  ViewSet with hyperlinked tables.
    """
    model = OkSwap
    queryset = OkSwap.objects.all()

class OccurrenceViewSet(obisTableViewSet):
    """
    This is the Occurrence ViewSet with hyperlinked tables.
    """
    model = Occurrence
    queryset = Occurrence.objects.all()

class SourceViewSet(obisTableViewSet):
    """
    This is the Ok Swap  ViewSet with hyperlinked tables.
    """
    model = Source
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
class InstitutionViewSet(obisTableViewSet):
    """
    This is the Institution  ViewSet with hyperlinked tables.
    """
    model = Institution
    queryset = Institution.objects.all()

class CountyViewSet(obisTableViewSet):
    """
    This is the County ViewSet with hyperlinked tables.
    """
    model = County
    queryset = County.objects.all()

class CoTrsViewSet(obisTableViewSet):
    """
    This is the CoTrs ViewSet with hyperlinked tables.
    """
    model = CoTrs
    queryset = CoTrs.objects.all()

class IdentificationVerificationViewSet(obisTableViewSet):
    """
    This is the IdentificationVerification ViewSet with hyperlinked tables.
    """
    model = IdentificationVerification
    queryset = IdentificationVerification.objects.all()

class RankChangeViewSet(obisTableViewSet):
    """
    This is the Rank Change ViewSet with hyperlinked tables.
    """
    model = RankChange
    queryset = RankChange.objects.all()
class SpatialRefSysViewSet(obisTableViewSet):
    """
    This is the Spatial-Ref-Sys  ViewSet with hyperlinked tables.
    """
    model = SpatialRefSys
    queryset = SpatialRefSys.objects.all()

#***************************************** OBIS DB Views ********************************************************

class VwSearchViewSet(obisViewViewSet):
    """
    This is the Search ViewSet with hyperlinked tables.
    """
    model = VwSearch
    queryset = VwSearch.objects.all()
    search_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')
    ordering_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')

class VwSearchmvViewSet(obisViewViewSet):
    """
    This is the Material View Search ViewSet with hyperlinked tables.
    Database: When data updated must run to update view: 'REFRESH MATERIALIZED VIEW vm_search_mv;'
    """
    model = VwSearchmv
    queryset = VwSearchmv.objects.all()
    search_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')
    ordering_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')
