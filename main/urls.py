from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/', categoriesView, name='categories'),
    path('basket/', basketView, name='basket'),
    path('login/', loginView, name='login'),
    path('shop/', shopView, name='shop'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name='about'),
    path('search/', searchView, name='search'),
]