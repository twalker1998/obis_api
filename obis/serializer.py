from rest_framework import serializers

from models import Acctax, Comtax, Syntax

class AcctaxSerializer(serializers.HyperlinkedModelSerializer):
    #comtax = ComtaxSerializer(source='Comtax',read_only=True,many=True)

    class Meta:
        model = Acctax
#        fields = ['url','acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
#                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source']


class ComtaxSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer):
    #acodes = AcctaxSerializer(read_only=True,many=True)
    class Meta:
        #depth=1
        model= Comtax
#        fields =['url','acode','vernacularname']


"""
class AcctaxSerializer(serializers.HyperlinkedModelSerializer):
    #comtax = ComtaxSerializer(source='Comtax',read_only=True,many=True)

    class Meta:
        model = Acctax
        fields = ['url','acode','sname','scientificnameauthorship','kingdom','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source']
"""
#class CarSerializer(ModelSerializer):
#    producer= ProducerSerializer(read_only=True)
#
#    class Meta:
#        model = Car
#        fields = ('producer', 'color', 'car_model', 'doors', )


#class LuSourceSerializer(serializers.HyperlinkedModelSerializer):
    #code = serializers.HyperlinkedIdentityField()
#    class Meta:
#        model = LuSource
#        fields = ('url','cource', 'comments')


#class RoostSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer()
#    class Meta:
#        model = Roosts
#        fields = ('url', 'name', 'soar_no', 'latitude', 'source','longitude', 'nex2004', 'loc_source_comment')
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)
