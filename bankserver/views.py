from django.shortcuts import render
from .models import Banks, Branches
from .serializers import BranchSerializer
from .pagination import MyLimitOffsetPagination
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_protect


class BankViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    search_fields = ['^ifsc','^city','^state']
    queryset = Branches.objects.filter(ifsc__startswith='')
    serializer_class = BranchSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    
    filterset_fields =['ifsc']
    ordering_fields = ['ifsc']

def home(request):
    
    return render(request,'index.html')


def about(request):
    return render(request, 'about.html')
