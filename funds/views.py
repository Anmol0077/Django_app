from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import MfSerializer
from .serializers import CpSerializer
from .serializers import MathchingSerializer
from .serializers import JoinTableSerializer
from .models import Hero
from .models import MutualFunds
from .models import CompaniesName
from .models import Matchingfield
from .models import JoinTableModel
from django.http import HttpResponse


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class MfViewSet(viewsets.ModelViewSet):
    queryset = MutualFunds.objects.all().order_by('mf_id')
    serializer_class = MfSerializer

class CpViewSet(viewsets.ModelViewSet):
    queryset = CompaniesName.objects.all().order_by('cp_id')
    serializer_class = CpSerializer   

class MatchingViewSet(viewsets.ModelViewSet):
    queryset = Matchingfield.objects.all().order_by('cp_id')
    serializer_class = MathchingSerializer   

class JoinTableApi(viewsets.ModelViewSet):
    queryset = JoinTableModel.objects.raw('Select funds_matchingfield.id,funds_mutualfunds.mf_name, funds_mutualfunds.mf_id,funds_companiesname.cp_name from funds_matchingfield JOIN funds_mutualfunds on funds_mutualfunds.mf_id = funds_matchingfield.mf_id JOIN funds_companiesname on funds_companiesname.cp_id = funds_matchingfield.cp_id')
    serializer_class = JoinTableSerializer   

def get_id(request,id=None):
    message = f'You submitted ID {id}' 
    # for p in JoinTableModel.objects.raw('Select mf_id from funds_mutualfunds'):
        # print(p.mf_id)
        return HttpResponse(p.mf_id)
   
