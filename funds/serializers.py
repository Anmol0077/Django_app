from rest_framework import serializers

from .models import Hero
from .models import MutualFunds
from .models import CompaniesName
from .models import Matchingfield
from .models import JoinTableModel

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')


class MfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MutualFunds
        fields = ('mf_id', 'mf_name')  

class CpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompaniesName
        fields = ('cp_id', 'cp_name')     

class MathchingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matchingfield
        fields = ('cp_id','mf_id')               

class JoinTableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JoinTableModel
        fields = ('cp_name','mf_name')           