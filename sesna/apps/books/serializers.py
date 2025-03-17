from rest_framework import serializers
from .models import Book
from sesna.apps.authors.models import Author

# filepath: /Users/ichsannuur/Documents/Backend Project/sesna/sesna/apps/books/serializers.py

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    # custom_field = serializers.SerializerMethodField()

    # class Meta:
        # model = Book
        # fields = '__all__'

    # def get_custom_field(self, obj):
    #     return f'{obj.title} by {obj.author.name}'