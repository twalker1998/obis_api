author__ = 'mstacy'
import django_filters

from models import Acctax,Comtax,Occurrence,Syntax,IUCNLookup,GlobalRankLookup,StateRankLookup,NativityLookup,CategoryLookup,NameCategoryDescLookup,NameTypeDescLookup #,SearchView

class AcctaxFilter(django_filters.FilterSet):

    a_id = django_filters.NumberFilter(lookup_type='exact')
    acode = django_filters.CharFilter(lookup_type='icontains')
    sname = django_filters.CharFilter(lookup_type='icontains')
    scientificnameauthorship = django_filters.CharFilter(lookup_type='icontains')
#    kingdom = django_filters.CharFilter(lookup_type='icontains')
    phylum = django_filters.CharFilter(lookup_type='icontains')
    taxclass = django_filters.CharFilter(lookup_type='icontains')
    taxorder = django_filters.CharFilter(lookup_type='icontains')
    family = django_filters.CharFilter(lookup_type='icontains')
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

class ComtaxFilter(django_filters.FilterSet):
    c_id = django_filters.NumberFilter(lookup_type='exact')
    acode = django_filters.CharFilter(lookup_type='exact')
    vernacularname = django_filters.CharFilter(lookup_type='icontains')
    primary_name = django_filters.CharFilter(lookup_type='exact')
    class Meta:
        model  = Comtax

class OccurrenceFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_type='exact')

    class Meta:
        model = Occurrence

class SyntaxFilter(django_filters.FilterSet):
    acode = django_filters.CharFilter(lookup_type='exact')
    sname = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Syntax

class IUCNLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = IUCNLookup

class GlobalRankLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = GlobalRankLookup

class StateRankLookupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = StateRankLookup

class NativityLookupFilter(django_filters.FilterSet):
    n_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = NativityLookup

class CategoryLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = CategoryLookup

class NameCategoryDescLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = NameCategoryDescLookup

class NameTypeDescLookupFilter(django_filters.FilterSet):
    a_id = django_filters.NumberFilter(lookup_type='exact')

    class Meta:
        model = NameTypeDescLookup

class CountyFilter(django_filters.FilterSet):
    gid = django_filters.NumberFilter(lookup_type='exact')

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
