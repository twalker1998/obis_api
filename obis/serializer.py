from rest_framework import serializers

from .models import *

class AcctaxSerializer(serializers.HyperlinkedModelSerializer):
    family = serializers.SlugRelatedField(slug_field='family', queryset=Acctax.objects.all())
    class Meta:
        model = Acctax
        fields = ('url','a_id','acode','sname','scientificnameauthorship','family','genus','species','subspecies','variety','forma','elcode','gelcode','iucncode','g_rank','s_rank','nativity','source','usda_code','tsn','fed_status','st_status','swap','scientificname','sspscientificnameauthorship','varscientificnameauthorship','formascientificnameauthorship','tracked')

class ComtaxSerializer(serializers.HyperlinkedModelSerializer):
    c_id = serializers.CharField()
    class Meta:
        model = Comtax
        fields = ('url','c_id','acode','vernacularname','primary_name')

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('url','source', 'description')

class HightaxSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="obis:hightax-detail")
    family = serializers.CharField()
    class Meta:
        model = Hightax
        fields = ('url','kingdom','phylum','taxclass','taxorder','family','category','name_type_desc','name_category_desc')

class SyntaxSerializer(serializers.HyperlinkedModelSerializer):    
     class Meta:
        model = Syntax
        fields = ('url','s_id','acode','scode','sname','scientificnameauthorship','family','genus','species','subspecies','variety','scientificname','sspscientificnameauthorship','varscientificnameauthorship','formascientificnameauthorship','tsn')

class OccurenceSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Occurrence
        fields = ('url','resourcetype','gid','acode','eventdate','recordedby','county','locality','behavior','habitat','sex','lifestage','associatedtaxa','verbatimelevation','depth','depthaccuracy','individualcount','occurrenceremarks','taxonremarks','institutioncode','basisofrecord','catalognumber','othercatalognumbers','typestatus','recordnumber','samplingprotocol','preparations','primary_data','associatedreferences','datasetname','coordinateprecision','decimallatitude','decimallongitude','geodeticdatum','georeferencedby','georeferenceddate','georeferenceremarks','georeferencesources','georeferenceverificationstatus','geom','problem_with_record','previousidentifications','identificationverificationstatus','identificationconfidence','identificationremarks','datelastmodified','associatedoccurrences','associatedsequences','entby','entrydate','obs_gid','mtr','township','ns','range','ew','section','quarter','zone','utme','utmn','hiderecord','hiderecordcomment','relationshipremarks','informationwitheld','awaitingreview','occurrenceid')

class FedStatusSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = FedStatus
        fields = ('url','status_id','status','description')

class StStatusSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = StStatus
        fields = ('url','status_id','status','description')

class OkSwapSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = OkSwap
        fields = ('url','swap_id','tier','description')

class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Institution
        fields = ('url','institutioncode','institution','curator','email','telephone','address','city','state','country','zipcode','institutiontype','link')

class CountySerializer(serializers.HyperlinkedModelSerializer):
    county = serializers.CharField()
    class Meta:
        model = County
        fields = ('url','county','gid')

class IdentificationVerificationSerializer(serializers.HyperlinkedModelSerializer):
    pkey = serializers.CharField()
    class Meta:
        model = IdentificationVerification
        fields = ('url','pkey','catalognumber','identifiedby','identificationremarks','datalastmodified','identifiedacode','gid')

class CoTrsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CoTrs
        fields = ('url','gid','name','geom','trs')

class RankChangeSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = RankChange
        fields = ('url','r_id','acode','previous_s_rank','s_rank','changedby','rankremarks','datelastmodified','previousdatemodified')

class SpatialRefSysSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = SpatialRefSys
        fields = ('url','srid','auth_name','auth_srid','srtext','proj4text')

class IUCNLookupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = IUCNLookup
        fields = ('code','description','id')

class GlobalRankLookupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = GlobalRankLookup
        fields = ('id','code')

class StateRankLookupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = StateRankLookup
        fields = ('id','code')

class NativityLookupSerializer(serializers.HyperlinkedModelSerializer):
    n_id = serializers.CharField()
    class Meta:
        model = NativityLookup
        fields = ('n_id','nativity')

class CategoryLookupSerializer(serializers.HyperlinkedModelSerializer):
    a_id = serializers.CharField()
    class Meta:
        model = CategoryLookup
        fields = ('a_id','category')

class NameCategoryDescLookupSerializer(serializers.HyperlinkedModelSerializer):
    a_id = serializers.CharField()
    class Meta:
        model = NameCategoryDescLookup
        fields = ('a_id','name_category_desc')

class NameTypeDescLookupSerializer(serializers.HyperlinkedModelSerializer):
    a_id = serializers.CharField()
    class Meta:
        model = NameTypeDescLookup
        fields = ('a_id','name_type_desc')

class BasisOfRecordLookupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = BasisOfRecordLookup
        fields = ('id','basisofrecord')

class ResourceTypeLookupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = ResourceTypeLookup
        fields = ('id','resourcetype')

class DOriginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DOrigin
        fields = ('url','d_origin_id','origin')

class DRegularitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DRegularity
        fields = ('url','d_regularity_id','regularity')

class DDistConfidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DDistConfidence
        fields = ('url','d_dist_confidence_id','dist_confidence')

class DPresenceAbsenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DPresenceAbsence
        fields = ('url','d_presence_absence_id','presence_absence')

class DPopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DPopulation
        fields = ('url','d_population_id','population')

class DistributionDataSerializer(serializers.HyperlinkedModelSerializer):
    d_id = serializers.CharField()
    class Meta:
        model = DistributionData
        fields = ('url','d_id','acode','elcode','origin','regularity','dist_confidence','presence_absence','population')
