from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='author')
    
    class Meta:
        model = Author
        readonly = ['join_date','is_active','is_admin']
        exclude = ['password']
    
    