from datetime import date
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    cover = serializers.FileField(required=False)
    pages = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    def get_pages(self, obj):
        return obj.pages.count()
    