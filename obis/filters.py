author__ = 'mstacy'
import django_filters

from models import Acctax,Comtax,County,Occurrence,Syntax,IUCNLookup,GlobalRankLookup,StateRankLookup,NativityLookup,CategoryLookup,NameCategoryDescLookup,NameTypeDescLookup,BasisOfRecordLookup,ResourceTypeLookup,DistributionData #,SearchView

class AcctaxFilter(django_filters.FilterSet):

    a_id = django_filters.NumberFilter(lookup_type='exact')
    acode = django_filters.CharFilter(lookup_type='icontains')
    sname = django_filters.CharFilter(lookup_type='icontains')
    scientificnameauthorship = django_filters.CharFilter(lookup_type='icontains')
#    kingdom = django_filters.CharFilter(lookup_type='icontains')
    phylum = django_filters.CharFilter(lookup_type='icontains')
    taxclass = django_filters.CharFilter(lookup_type='icontains')
    taxorder = django_filters.CharFilter(lookup_type='icontains')
    family = django_filters.CharFilter(lookup_type='exact')
    genus = django_filters.CharFilter(lookup_type='icontains')
    species = django_filters.CharFilter(lookup_type='icontains')
    subspecies = django_filters.CharFilter(lookup_type='icontains')
    variety = django_filters.CharFilter(lookup_type='icontains')
    forma = django_filters.CharFilter(lookup_type='icontains')
    elcode = django_filters.CharFilter(lookup_type='icontains')
    gelcode = django_filters.NumberFilter(lookup_type='exact')
    iunccode = django_filters.CharFilter(lookup_type='icontains')
    g_rank = django_filters.CharFilter(lookup_type='icontains')
    s_rank = django_filters.CharFilter(lookup_type='icontains')
    nativity = django_filters.CharFilter(lookup_type='icontains')
    source = django_filters.CharFilter(lookup_type='icontains')
    scientificname = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Acctax
        fields = '__all__'

class ComtaxFilter(django_filters.FilterSet):
    c_id = django_filters.NumberFilter(lookup_type='exact')
    acode = django_filters.CharFilter(lookup_type='exact')
    vernacularname = django_filters.CharFilter(lookup_type='icontains')
    primary_name = django_filters.CharFilter(lookup_type='exact')

    class Meta:
        model = Comtax
        fields = '__all__'

class OccurrenceFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_type='exact')
    catalognumber = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Occurrence
        fields = '__all__'

class SyntaxFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_type='exact')
    sname = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Syntax
        fields = '__all__'

class IUCNLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = IUCNLookup
        fields = '__all__'

class GlobalRankLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = GlobalRankLookup
        fields = '__all__'

class StateRankLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = StateRankLookup
        fields = '__all__'

class NativityLookupFilter(django_filters.FilterSet):
    n_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = NativityLookup
        fields = '__all__'

class CategoryLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = CategoryLookup
        fields = '__all__'

class NameCategoryDescLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = NameCategoryDescLookup
        fields = '__all__'

class NameTypeDescLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = NameTypeDescLookup
        fields = '__all__'

class CountyFilter(django_filters.FilterSet):
    gid = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = County
        fields = '__all__'

class BasisOfRecordLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = BasisOfRecordLookup
        fields = '__all__'

class ResourceTypeLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = ResourceTypeLookup
        fields = '__all__'

class DistributionDataFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_type='exact')

    class Meta:
        model = DistributionData
        fields = '__all__'

"""
class SearchViewFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')
    acode = django_filters.CharFilter(lookup_type='icontains')
    sname = django_filters.CharFilter(lookup_type='icontains')
    scientificname = django_filters.CharFilter(lookup_type='icontains')
    status = django_filters.CharFilter(lookup_type='icontains')
    vernacularname = django_filters.CharFilter(lookup_type='icontains')
    primary_name = django_filters.CharFilter(lookup_type='icontains')
    kingdom = django_filters.CharFilter(lookup_type='icontains')
    phylum = django_filters.CharFilter(lookup_type='icontains')
    taxclass = django_filters.CharFilter(lookup_type='icontains')
    family = django_filters.CharFilter(lookup_type='icontains')
    genus = django_filters.CharFilter(lookup_type='icontains')
    category = django_filters.CharFilter(lookup_type='icontains')
    name_type_desc = django_filters.CharFilter(lookup_type='icontains')
    name_category_desc = django_filters.CharFilter(lookup_type='icontains')
    elcode = django_filters.NumberFilter(lookup_type='exact')
    gelcode = django_filters.NumberFilter(lookup_type='exact')
    tsn = django_filters.CharFilter(lookup_type='icontains')
    usda_code = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = VwSearch
"""
