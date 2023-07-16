from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/', categoriesView, name='categories'),
    path('categories/<slug:slug>/', postCategoriesView, name='post_categories'),
    path('cart/', cartView, name='cart'),
    path('login/', loginView, name='login'),
    path('shop/', shopView, name='shop'),
    path('shop/<slug:slug>/', postShopView, name='post_shop'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name='about'),
    path('search/', searchView, name='search'),
    # path('payment/', PaymentView.as_view(), name='payment'),
]