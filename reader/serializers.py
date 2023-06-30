from reader.models import Reader
from rest_framework import serializers


class ReaderSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='reader')
    
    class Meta:
        model = Reader
        readonly = ['join_date','is_active','is_admin']
        exclude = ['password']
    
    