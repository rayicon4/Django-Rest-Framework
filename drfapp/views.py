from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets, permissions
from .serializers import ArmySerializer
from .models import Army
from django.contrib.auth.models import User



class ArmyView(viewsets.ModelViewSet):
    queryset = Army.objects.all()
    serializer_class = ArmySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
