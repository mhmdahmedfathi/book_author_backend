from datetime import date
from rest_framework import serializers
from .models import Page

class PageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    book = serializers.ReadOnlyField(source='book.title')
    title = serializers.CharField(required=False)
    book_id = serializers.IntegerField(required=False)

    class Meta:
        model = Page
        fields = '__all__' 

    def get_book_id(self, obj):
        return obj.book.id
    
    