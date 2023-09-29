from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Book, Keyword, Research, ResearchBook
from .serializers import UserSerializer, BookSerializer, KeywordSerializer, ResearchSerializer, ResearchBookSerializer
from django.shortcuts import render




def index(request):
    return render(request, 'libraries/index.html')

@api_view(['GET'])
def search_view(request):
    # Retrieve search parameters from the request
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    subject = request.GET.get('subject', '')
    year = request.GET.get('year', '')
    language = request.GET.get('language', '')

    # Perform the search logic based on the parameters
    # pylint: disable=no-member
    books = Book.objects.filter(
        title__icontains=title,
        author__icontains=author,
        genre__icontains=subject,
        publication_year__icontains=year,
        language__icontains=language
    )
    # pylint: enable=no-member

    # Pass the retrieved books to the template for display
    return render(request, 'libraries/search_results.html', {
        'title': title,
        'author': author,
        'subject': subject,
        'year': year,
        'language': language,
        'books': books  # Pass the books to the template
    })

@api_view(['GET'])
def search_research_by_title(request, title):
    # pylint: disable=no-member
    research_books = ResearchBook.objects.filter(book__title__icontains=title)
    # pylint: enable=no-member
    serializer = ResearchBookSerializer(research_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_research_by_author(request, author):
    # pylint: disable=no-member
    research_books = ResearchBook.objects.filter(book__author__icontains=author)
    # pylint: enable=no-member
    serializer = ResearchBookSerializer(research_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_research_by_subject(request, subject):
    # pylint: disable=no-member
    research_books = ResearchBook.objects.filter(book__genre__icontains=subject)
    # pylint: enable=no-member
    serializer = ResearchBookSerializer(research_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_research_by_year(request, year):
    # pylint: disable=no-member
    research_books = ResearchBook.objects.filter(book__publication_year=year)
    # pylint: enable=no-member
    serializer = ResearchBookSerializer(research_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_research_by_language(request, language):
    # pylint: disable=no-member
    research_books = ResearchBook.objects.filter(book__language__icontains=language)
    # pylint: enable=no-member
    serializer = ResearchBookSerializer(research_books, many=True)
    return Response(serializer.data)
