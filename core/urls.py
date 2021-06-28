from django.urls import path
from django.urls.resolvers import URLPattern

from .views import index, contato, produto, about, help, programing, projects

urlpatterns = [
    path('', index, name = 'index'),
    path('contato', contato, name = 'contato'),
    path('produto', produto, name = 'produto'),
    path('about', about, name = 'about'),
    path('help', help, name = 'help'),
    path('programing', programing, name = 'programing'),
    path('projects', projects, name = 'projects'),
]