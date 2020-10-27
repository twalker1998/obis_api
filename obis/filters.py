author__ = 'mstacy'
import django_filters

from models import Acctax,Comtax,County,Occurrence,Syntax,IUCNLookup,GlobalRankLookup,StateRankLookup,NativityLookup,CategoryLookup,NameCategoryDescLookup,NameTypeDescLookup,BasisOfRecordLookup,ResourceTypeLookup,DistributionData #,SearchView

class AcctaxFilter(django_filters.FilterSet):

    a_id = django_filters.NumberFilter(lookup_expr='exact')
    acode = django_filters.CharFilter(lookup_expr='icontains')
    sname = django_filters.CharFilter(lookup_expr='icontains')
    scientificnameauthorship = django_filters.CharFilter(lookup_expr='icontains')
#    kingdom = django_filters.CharFilter(lookup_expr='icontains')
    phylum = django_filters.CharFilter(lookup_expr='icontains')
    taxclass = django_filters.CharFilter(lookup_expr='icontains')
    taxorder = django_filters.CharFilter(lookup_expr='icontains')
    family = django_filters.CharFilter(lookup_expr='exact')
    genus = django_filters.CharFilter(lookup_expr='icontains')
    species = django_filters.CharFilter(lookup_expr='icontains')
    subspecies = django_filters.CharFilter(lookup_expr='icontains')
    variety = django_filters.CharFilter(lookup_expr='icontains')
    forma = django_filters.CharFilter(lookup_expr='icontains')
    elcode = django_filters.CharFilter(lookup_expr='icontains')
    gelcode = django_filters.NumberFilter(lookup_expr='exact')
    iunccode = django_filters.CharFilter(lookup_expr='icontains')
    g_rank = django_filters.CharFilter(lookup_expr='icontains')
    s_rank = django_filters.CharFilter(lookup_expr='icontains')
    nativity = django_filters.CharFilter(lookup_expr='icontains')
    source = django_filters.CharFilter(lookup_expr='icontains')
    scientificname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Acctax
        fields = '__all__'

class ComtaxFilter(django_filters.FilterSet):
    c_id = django_filters.NumberFilter(lookup_expr='exact')
    acode = django_filters.CharFilter(lookup_expr='exact')
    vernacularname = django_filters.CharFilter(lookup_expr='icontains')
    primary_name = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Comtax
        fields = '__all__'

class OccurrenceFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_expr='exact')
    catalognumber = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Occurrence
        fields = '__all__'

class SyntaxFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_expr='exact')
    sname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Syntax
        fields = '__all__'

class IUCNLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = IUCNLookup
        fields = '__all__'

class GlobalRankLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = GlobalRankLookup
        fields = '__all__'

class StateRankLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = StateRankLookup
        fields = '__all__'

class NativityLookupFilter(django_filters.FilterSet):
    n_id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = NativityLookup
        fields = '__all__'

class CategoryLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = CategoryLookup
        fields = '__all__'

class NameCategoryDescLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = NameCategoryDescLookup
        fields = '__all__'

class NameTypeDescLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = NameTypeDescLookup
        fields = '__all__'

class CountyFilter(django_filters.FilterSet):
    gid = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = County
        fields = '__all__'

class BasisOfRecordLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = BasisOfRecordLookup
        fields = '__all__'

class ResourceTypeLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = ResourceTypeLookup
        fields = '__all__'

class DistributionDataFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = DistributionData
        fields = '__all__'

"""
class SearchViewFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_expr='exact')
    acode = django_filters.CharFilter(lookup_expr='icontains')
    sname = django_filters.CharFilter(lookup_expr='icontains')
    scientificname = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='icontains')
    vernacularname = django_filters.CharFilter(lookup_expr='icontains')
    primary_name = django_filters.CharFilter(lookup_expr='icontains')
    kingdom = django_filters.CharFilter(lookup_expr='icontains')
    phylum = django_filters.CharFilter(lookup_expr='icontains')
    taxclass = django_filters.CharFilter(lookup_expr='icontains')
    family = django_filters.CharFilter(lookup_expr='icontains')
    genus = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    name_type_desc = django_filters.CharFilter(lookup_expr='icontains')
    name_category_desc = django_filters.CharFilter(lookup_expr='icontains')
    elcode = django_filters.NumberFilter(lookup_expr='exact')
    gelcode = django_filters.NumberFilter(lookup_expr='exact')
    tsn = django_filters.CharFilter(lookup_expr='icontains')
    usda_code = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = VwSearch
"""
