from rest_framework import serializers
from .models import Army



class ArmySerializer(serializers.ModelSerializer):
    class Meta:
        model = Army
        fields = ['id', 'url', 'name', 'batallion', 'location', 'description', 'created']