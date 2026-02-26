from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import  Test
from .serializer import TestSerializer
# Create your views here.
class TestListApiView(ListCreateAPIView):
    queryset=Test.objects.all()
    serializer_class=TestSerializer