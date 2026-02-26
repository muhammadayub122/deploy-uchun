from rest_framework.serializers import ModelSerializer
from .models import  Test
class TestSerializer(ModelSerializer):
    class Meta:
        fields="__all__"
        model=Test