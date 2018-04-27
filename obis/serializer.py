from rest_framework import serializers

from models import Acctax, Comtax, Syntax, Source
# This is an example of how you can make your own serializer. Default seems to be working.
# Left this only for examples.

class AcctaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acctax
#        fields = ['url','acode','sname','scientificnameauthorship','phylum','taxclass','taxorder',
#                  'family','genus','species','subspecies','variety','forma','elcode','gelcode',
#                  'iunccode','g_rank','s_rank','nativity','source']


class ComtaxSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer):
    class Meta:
        model= Comtax
#        fields = ['url','acode','vernacularname']

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('url','source', 'description')
