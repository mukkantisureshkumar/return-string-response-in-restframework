from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from app.serializers import *
from app.models import *
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
def first(request):
    return Response({'MESSAGE':'hai rest framework'})

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def studentData(request):
    ms=Student.objects.all()
    sm=Studentms(ms,many=True)

    return Response(sm.data)