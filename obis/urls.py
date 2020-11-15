__author__ = 'mstacy'
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

router = routers.SimpleRouter()
router.register('acctax', AcctaxViewSet)
router.register('comtax', ComtaxViewSet)
router.register('syntax', SyntaxViewSet)
router.register('hightax', HightaxViewSet)
router.register('fedstatus', FedStatusViewSet)
router.register('ststatus', StStatusViewSet)
router.register('okswap', OkSwapViewSet)
router.register('occurrence', OccurrenceViewSet, base_name='occurrence')
router.register('source',SourceViewSet)
router.register('institution', InstitutionViewSet)
router.register('county', CountyViewSet)
router.register('cotrs', CoTrsViewSet)
router.register('identificationverification', IdentificationVerificationViewSet)
router.register('rankchange', RankChangeViewSet)
router.register('spatialrefsys', SpatialRefSysViewSet)
router.register('iucn_lu', IUCNLookupViewSet)
router.register('global_rank_lu', GlobalRankLookupViewSet)
router.register('state_rank_lu', StateRankLookupViewSet)
router.register('nativity_lu', NativityLookupViewSet)
router.register('category_lu', CategoryLookupViewSet)
router.register('name_category_desc_lu', NameCategoryDescLookupViewSet)
router.register('name_type_desc_lu', NameTypeDescLookupViewSet)
router.register('basisofrecord_lu', BasisOfRecordLookupViewSet)
router.register('resourcetype_lu', ResourceTypeLookupViewSet)
router.register('d_origin', DOriginViewSet)
router.register('d_regularity', DRegularityViewSet)
router.register('d_dist_confidence', DDistConfidenceViewSet)
router.register('d_presence_absence', DPresenceAbsenceViewSet)
router.register('d_population', DPopulationViewSet)
router.register('distribution_data', DistributionDataViewSet)

# View
router.register('vwsearch', VwSearchViewSet)
#router.register('vwsearchmv', VwSearchmvViewSet)


urlpatterns = [
    url('', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
