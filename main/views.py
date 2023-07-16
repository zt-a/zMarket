import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .forms import *
from .models import *

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentView(TemplateView):
    template_name = 'payment.html'

    def post(self, request, *args, **kwargs):
        token = request.POST.get('stripeToken')
        amount = 1000  # Замените на актуальную сумму

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Оплата заказа'
            )
            # Здесь вы можете обрабатывать успешный платеж
            return render(request, 'main/payment_success.html')

        except stripe.error.CardError as e:
            error_msg = e.user_message
            return render(request, 'main/payment.html', {'error': error_msg})
def index(request):
    return render(request, 'main/index.html')


def basketView(request):
    return render(request, 'main/basket.html')


def categoriesView(request):
    return render(request, 'main/categories.html')


def loginView(request):
    return render(request, 'main/login.html')


def shopView(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main/shop.html', context=context)


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


def postShopView(request):
    return render(request, 'main/post_shop.html')

def postCategoriesView(request):
    return render(request, 'main/post_categories.html')
