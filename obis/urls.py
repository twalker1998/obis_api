__author__ = 'Tyler Walker' # twalker1998@gmail.com
__author__ = 'Mark Stacy'
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from obis.views import (AcctaxViewSet, BasisOfRecordLookupViewSet,
                        CategoryLookupViewSet, ComtaxViewSet, CoTrsViewSet,
                        CountyViewSet, DDistConfidenceViewSet,
                        DistributionDataViewSet, DOriginViewSet,
                        DPopulationViewSet, DPresenceAbsenceViewSet,
                        DRegularityViewSet, FedStatusViewSet,
                        GlobalRankLookupViewSet, HightaxViewSet,
                        IdentificationVerificationViewSet, InstitutionViewSet,
                        IUCNLookupViewSet, KingdomLookupViewSet,
                        NameCategoryDescLookupViewSet,
                        NameTypeDescLookupViewSet, NativityLookupViewSet,
                        OccurrenceViewSet, OkSwapViewSet, RankChangeViewSet,
                        ResourceTypeLookupViewSet, SourceViewSet,
                        SpatialRefSysViewSet, StateRankLookupViewSet,
                        StStatusViewSet, SyntaxViewSet)

router = routers.SimpleRouter()
router.register('acctax', AcctaxViewSet)
router.register('basisofrecord_lu', BasisOfRecordLookupViewSet)
router.register('category_lu', CategoryLookupViewSet)
router.register('comtax', ComtaxViewSet)
router.register('cotrs', CoTrsViewSet)
router.register('county', CountyViewSet)
router.register('d_dist_confidence', DDistConfidenceViewSet)
router.register('distribution_data', DistributionDataViewSet)
router.register('d_origin', DOriginViewSet)
router.register('d_population', DPopulationViewSet)
router.register('d_presence_absence', DPresenceAbsenceViewSet)
router.register('d_regularity', DRegularityViewSet)
router.register('fedstatus', FedStatusViewSet)
router.register('global_rank_lu', GlobalRankLookupViewSet)
router.register('hightax', HightaxViewSet)
router.register('identificationverification', IdentificationVerificationViewSet)
router.register('institution', InstitutionViewSet)
router.register('iucn_lu', IUCNLookupViewSet)
router.register('kingdom_lu', KingdomLookupViewSet)
router.register('name_category_desc_lu', NameCategoryDescLookupViewSet)
router.register('name_type_desc_lu', NameTypeDescLookupViewSet)
router.register('nativity_lu', NativityLookupViewSet)
router.register('occurrence', OccurrenceViewSet, basename='occurrence')
router.register('okswap', OkSwapViewSet)
router.register('rankchange', RankChangeViewSet)
router.register('resourcetype_lu', ResourceTypeLookupViewSet)
router.register('source', SourceViewSet)
router.register('spatialrefsys', SpatialRefSysViewSet)
router.register('state_rank_lu', StateRankLookupViewSet)
router.register('ststatus', StStatusViewSet)
router.register('syntax', SyntaxViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json'])
