from django.urls import path
from . import views
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    #path('', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)), 
    path('login/', views.login_views, name='login'),# URL for the login page
    path('', views.index, name='index'),  # URL for the index page
    path('search/', views.search_view, name='search_books'),
    path('api/research_books/search/title/<str:title>/', views.search_research_by_title, name='search-research-by-title'),
    path('api/research_books/search/author/<str:author>/', views.search_research_by_author, name='search-research-by-author'),
    path('api/research_books/search/subject/<str:subject>/', views.search_research_by_subject, name='search-research-by-subject'),
    path('api/research_books/search/year/<int:year>/', views.search_research_by_year, name='search-research-by-year'),
    path('api/research_books/search/language/<str:language>/', views.search_research_by_language, name='search-research-by-language'),
    

]
