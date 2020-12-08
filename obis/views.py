__author__ = 'Tyler Walker' # twalker1998@gmail.com
__author__ = 'Mark Stacy'
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from obis.filters import (AcctaxFilter, BasisOfRecordLookupFilter,
                          CategoryLookupFilter, ComtaxFilter, CountyFilter,
                          DistributionDataFilter, GlobalRankLookupFilter,
                          IUCNLookupFilter, NameCategoryDescLookupFilter,
                          NativityLookupFilter, OccurrenceFilter,
                          ResourceTypeLookupFilter, StateRankLookupFilter,
                          SyntaxFilter)
from obis.models import (Acctax, BasisOfRecordLookup, CategoryLookup, Comtax,
                         CoTrs, County, DDistConfidence, DistributionData,
                         DOrigin, DPopulation, DPresenceAbsence, DRegularity,
                         FedStatus, GlobalRankLookup, Hightax,
                         IdentificationVerification, Institution, IUCNLookup,
                         KingdomLookup, NameCategoryDescLookup,
                         NameTypeDescLookup, NativityLookup, Occurrence,
                         OkSwap, RankChange, ResourceTypeLookup, Source,
                         SpatialRefSys, StateRankLookup, StStatus, Syntax)
from obis.serializer import (AcctaxSerializer, BasisOfRecordLookupSerializer,
                             CategoryLookupSerializer, ComtaxSerializer,
                             CoTrsSerializer, CountySerializer,
                             DDistConfidenceSerializer,
                             DistributionDataSerializer, DOriginSerializer,
                             DPopulationSerializer, DPresenceAbsenceSerializer,
                             DRegularitySerializer, FedStatusSerializer,
                             GlobalRankLookupSerializer, HightaxSerializer,
                             IdentificationVerificationSerializer,
                             InstitutionSerializer, IUCNLookupSerializer,
                             KingdomLookupSerializer,
                             NameCategoryDescLookupSerializer,
                             NameTypeDescLookupSerializer,
                             NativityLookupSerializer, OccurenceSerializer,
                             OccurrenceSearchSerializer, OkSwapSerializer,
                             RankChangeSerializer,
                             ResourceTypeLookupSerializer, SourceSerializer,
                             SpatialRefSysSerializer,
                             StateRankLookupSerializer, StStatusSerializer,
                             SyntaxSerializer)


# ************ OBIS Table ViewSet Class ************
class obisTableViewSet(viewsets.ModelViewSet):
    filter_backends    = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes   = (BrowsableAPIRenderer, JSONRenderer)

# ************ OBIS Tables ************
class AcctaxViewSet(obisTableViewSet):
    model            = Acctax
    queryset         = Acctax.objects.all()
    filter_class     = AcctaxFilter
    serializer_class = AcctaxSerializer
    search_fields    = ('sname', 'scientificnameauthorship', 'genus', 'species', 'subspecies', 'variety',
                          'forma', 'elcode', 'iucncode', 'g_rank', 's_rank', 'nativity', 'source', 'usda_code',
                          'name', 'sspscientificnameauthorship', 'varscientificnameauthorship',
                          'formascientificnameauthorship', 'scientificname')
    ordering_fields  = ('sname', 'scientificnameauthorship', 'family', 'genus', 'species', 'subspecies', 'variety',
                          'forma', 'elcode', 'gelcode', 'iucncode', 'g_rank', 's_rank', 'nativity', 'source', 'usda_code', 'tsn',
                          'fed_status', 'st_status', 'swap', 'name', 'sspscientificnameauthorship', 'varscientificnameauthorship',
                          'formascientificnameauthorship', 'tracked')

class BasisOfRecordLookupViewSet(obisTableViewSet):
    model            = BasisOfRecordLookup
    queryset         = BasisOfRecordLookup.objects.all()
    filter_class     = BasisOfRecordLookupFilter
    serializer_class = BasisOfRecordLookupSerializer
    search_fields    = ('id')

class CategoryLookupViewSet(obisTableViewSet):
    model            = CategoryLookup
    queryset         = CategoryLookup.objects.all()
    filter_class     = CategoryLookupFilter
    serializer_class = CategoryLookupSerializer
    search_fields    = ('a_id')

class ComtaxViewSet(obisTableViewSet):
    model            = Comtax
    queryset         = Comtax.objects.all()
    filter_class     = ComtaxFilter
    serializer_class = ComtaxSerializer
    search_fields    = ('acode', 'vernacularname', 'primary_name')

# TODO: might not need
class CoTrsViewSet(obisTableViewSet):
    model            = CoTrs
    queryset         = CoTrs.objects.all()
    serializer_class = CoTrsSerializer

class CountyViewSet(obisTableViewSet):
    model            = County
    queryset         = County.objects.all()
    filter_class     = CountyFilter
    serializer_class = CountySerializer
    search_fields    = ('gid')

class DDistConfidenceViewSet(obisTableViewSet):
    model            = DDistConfidence
    queryset         = DDistConfidence.objects.all()
    serializer_class = DDistConfidenceSerializer

class DistributionDataViewSet(obisTableViewSet):
    model            = DistributionData
    queryset         = DistributionData.objects.all()
    filter_class     = DistributionDataFilter
    serializer_class = DistributionDataSerializer
    search_fields    = ('acode')

class DOriginViewSet(obisTableViewSet):
    model            = DOrigin
    queryset         = DOrigin.objects.all()
    serializer_class = DOriginSerializer

class DPopulationViewSet(obisTableViewSet):
    model            = DPopulation
    queryset         = DPopulation.objects.all()
    serializer_class = DPopulationSerializer

class DPresenceAbsenceViewSet(obisTableViewSet):
    model            = DPresenceAbsence
    queryset         = DPresenceAbsence.objects.all()
    serializer_class = DPresenceAbsenceSerializer

class DRegularityViewSet(obisTableViewSet):
    model            = DRegularity
    queryset         = DRegularity.objects.all()
    serializer_class = DRegularitySerializer

class FedStatusViewSet(obisTableViewSet):
    model            = FedStatus
    queryset         = FedStatus.objects.all()
    serializer_class = FedStatusSerializer

class GlobalRankLookupViewSet(obisTableViewSet):
    model            = GlobalRankLookup
    queryset         = GlobalRankLookup.objects.all()
    filter_class     = GlobalRankLookupFilter
    serializer_class = GlobalRankLookupSerializer
    search_fields    = ('id')

class HightaxViewSet(obisTableViewSet):
    model            = Hightax
    queryset         = Hightax.objects.all()
    serializer_class = HightaxSerializer

class IdentificationVerificationViewSet(obisTableViewSet):
    model            = IdentificationVerification
    queryset         = IdentificationVerification.objects.all()
    serializer_class = IdentificationVerificationSerializer

class InstitutionViewSet(obisTableViewSet):
    model            = Institution
    queryset         = Institution.objects.all()
    serializer_class = InstitutionSerializer

class IUCNLookupViewSet(obisTableViewSet):
    model            = IUCNLookup
    queryset         = IUCNLookup.objects.all()
    filter_class     = IUCNLookupFilter
    serializer_class = IUCNLookupSerializer
    search_fields    = ('id')

class KingdomLookupViewSet(obisTableViewSet):
    model            = KingdomLookup
    queryset         = KingdomLookup.objects.all()
    serializer_class = KingdomLookupSerializer

class NameCategoryDescLookupViewSet(obisTableViewSet):
    model            = NameCategoryDescLookup
    queryset         = NameCategoryDescLookup.objects.all()
    filter_class     = NameCategoryDescLookupFilter
    serializer_class = NameCategoryDescLookupSerializer
    search_fields    = ('a_id')

class NameTypeDescLookupViewSet(obisTableViewSet):
    model            = NameTypeDescLookup
    queryset         = NameTypeDescLookup.objects.all()
    serializer_class = NameTypeDescLookupSerializer

class NativityLookupViewSet(obisTableViewSet):
    model            = NativityLookup
    queryset         = NativityLookup.objects.all()
    filter_class     = NativityLookupFilter
    serializer_class = NativityLookupSerializer
    search_fields    = ('n_id')

class OccurrenceViewSet(obisTableViewSet):
    model            = Occurrence
    filter_class     = OccurrenceFilter
    serializer_class = OccurenceSerializer
    search_fields    = ('acode', 'catalognumber') # TODO: should we add gid?

    def get_queryset(self):
        user     = self.request.user
        queryset = Occurrence.objects.all()

        if user.is_authenticated == False or user.is_staff:
            return queryset
        else:
            institutioncodes = [g.name for g in user.groups.all()]
            return queryset.filter(institutioncode__in=institutioncodes)

class OccurrenceSearchViewSet(obisTableViewSet):
    model            = Occurrence
    serializer_class = OccurrenceSearchSerializer

    def get_queryset(self):
        user     = self.request.user
        queryset = Occurrence.objects.all()

        if self.request.method == 'GET':
            params           = self.request.GET
            county           = params.get('county', '')
            sname            = params.get('sname', '')
            family           = params.get('family', '')
            genus            = params.get('genus', '')
            species          = params.get('species', '')
            subspecies       = params.get('ssp', '')
            variety          = params.get('var', '')
            vernacularname   = params.get('commonname', '')
            recordedby       = params.get('collector', '')
            start_date       = params.get('date1', '')
            end_date         = params.get('date2', '')
            catalognumber    = params.get('catalognumber', '')

            if county:
                queryset = queryset.filter(county__county__exact=county)
            if sname:
                queryset = queryset.filter(acode__sname__icontains=sname)
            if family:
                queryset = queryset.filter(acode__family__family__icontains=family)
            if genus:
                queryset = queryset.filter(acode__genus__icontains=genus)
            if species:
                queryset = queryset.filter(acode__species__icontains=species)
            if subspecies:
                queryset = queryset.filter(acode__subspecies__icontains=subspecies)
            if variety:
                queryset = queryset.filter(acode__variety__icontains=variety)
            if vernacularname:
                comtax_query = Comtax.objects.filter(vernacularname__icontains=vernacularname).values_list('acode', flat=True)
                queryset     = queryset.filter(acode__acode__in=comtax_query)
            if recordedby:
                queryset = queryset.filter(recordedby__icontains=recordedby)
            if start_date and end_date:
                queryset = queryset.filter(eventdate__range=(start_date, end_date))
            if catalognumber:
                queryset = queryset.filter(catalognumber__exact=catalognumber)
        
        if user.is_authenticated == False or user.is_staff:
            return queryset.order_by('acode__sname')
        else:
            institutioncodes = [g.name for g in user.groups.all()]
            return queryset.filter(institutioncode__in=institutioncodes).order_by('acode__sname')

class OkSwapViewSet(obisTableViewSet):
    model            = OkSwap
    queryset         = OkSwap.objects.all()
    serializer_class = OkSwapSerializer

class RankChangeViewSet(obisTableViewSet):
    model            = RankChange
    queryset         = RankChange.objects.all()
    serializer_class = RankChangeSerializer

class ResourceTypeLookupViewSet(obisTableViewSet):
    model            = ResourceTypeLookup
    queryset         = ResourceTypeLookup.objects.all()
    filter_class     = ResourceTypeLookupFilter
    serializer_class = ResourceTypeLookupSerializer
    search_fields    = ('id')

class SourceViewSet(obisTableViewSet):
    model            = Source
    queryset         = Source.objects.all()
    serializer_class = SourceSerializer

class SpatialRefSysViewSet(obisTableViewSet):
    model            = SpatialRefSys
    queryset         = SpatialRefSys.objects.all()
    serializer_class = SpatialRefSysSerializer

class StateRankLookupViewSet(obisTableViewSet):
    model            = StateRankLookup
    queryset         = StateRankLookup.objects.all()
    filter_class     = StateRankLookupFilter
    serializer_class = StateRankLookupSerializer
    search_fields    = ('id')

class StStatusViewSet(obisTableViewSet):
    model            = StStatus
    queryset         = StStatus.objects.all()
    serializer_class = StStatusSerializer

class SyntaxViewSet(obisTableViewSet):
    model            = Syntax
    queryset         = Syntax.objects.all()
    filter_class     = SyntaxFilter
    serializer_class = SyntaxSerializer
    search_fields    = ('acode', 'scode', 'sname', 'scientificnameauthorship',
                        'family', 'genus', 'species', 'subspecies', 'variety',
                        'name', 'sspscientificnameauthorship', 'varscientificnameauthorship',
                        'formascientificnameauthorship')
    ordering_fields  = ('s_id', 'acode', 'scode', 'sname', 'scientificnameauthorship',
                        'family', 'genus', 'species', 'subspecies', 'variety',
                        'name', 'sspscientificnameauthorship', 'varscientificnameauthorship',
                        'formascientificnameauthorship', 'tsn')
