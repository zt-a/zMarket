from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def basketView(request):
    return render(request, 'main/basket.html')


def categoriesView(request):
    return render(request, 'main/categories.html')


def loginView(request):
    return render(request, 'main/login.html')


def shopView(request):
    return render(request, 'main/shop.html')


def aboutView(request):
    return render(request, 'main/about.html')


def contactView(request):
    return render(request, 'main/contact.html')



def searchView(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name__icontains=query)

    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'main/search.html', context=context)
