from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField()
    
    class Meta:
        model = User
        readonly = ['join_date','is_active','is_admin']
        exclude = ['password']
    
    