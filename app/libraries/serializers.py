from rest_framework import serializers
from .models import User, Book, Keyword, Research, ResearchBook, BookKeyword, Conducts, Consults, AssociatesWith


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username', 'email','password', 'user_type')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'publication_year', 'genre')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('keyword_id', 'keyword_text')


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ('research_id', 'research_date', 'search_query')


class ResearchBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchBook
        fields = ('research_book_id', 'research', 'book')


class BookKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookKeyword
        fields = ('book_keyword_id', 'book', 'keyword')


class ConductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conducts
        fields = ('user', 'research')


class ConsultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consults
        fields = ('research', 'book')


class AssociatesWithSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociatesWith
        fields = ('book', 'keyword')
