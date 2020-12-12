from django.db.models import fields
from rest_framework import serializers

from .models import InviteUser

class InviteUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = InviteUser
        fields = ('id', 'email')
