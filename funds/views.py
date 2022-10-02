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
    fetched_id = id
    print(fetched_id[0:2])
    thislist = []
    str1 = ""
    if fetched_id[0:2] == 'MF':
        print("hello")
        queryset = JoinTableModel.objects.raw("Select funds_matchingfield.id,funds_mutualfunds.mf_name, funds_mutualfunds.mf_id as mf_id,funds_companiesname.cp_name,funds_companiesname.cp_id from funds_matchingfield JOIN funds_mutualfunds on funds_mutualfunds.mf_id = funds_matchingfield.mf_id JOIN funds_companiesname on funds_companiesname.cp_id = funds_matchingfield.cp_id where funds_matchingfield.mf_id = %s",[id])
        print(queryset)
        for p in queryset:
            # print(p.cp_name)
             thislist.append(p.cp_name)
            # return HttpResponse(p.cp_name)
        for i in thislist:
            str1 += i
            print(str1)    
    elif fetched_id[0:2] == 'CP':
        print("hello CP")
        queryset = JoinTableModel.objects.raw("Select funds_matchingfield.id,funds_mutualfunds.mf_name, funds_mutualfunds.mf_id as mf_id,funds_companiesname.cp_name,funds_companiesname.cp_id from funds_matchingfield JOIN funds_mutualfunds on funds_mutualfunds.mf_id = funds_matchingfield.mf_id JOIN funds_companiesname on funds_companiesname.cp_id = funds_matchingfield.cp_id where funds_matchingfield.cp_id = %s",[id])
        for p in queryset:
            # print(p.mf_name)
            thislist.append(p.mf_name)
            # return HttpResponse(p.mf_name)   
        for i in thislist:
            str1 += i
            print(str1)
    return HttpResponse(str1 +" ")
