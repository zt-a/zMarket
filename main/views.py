import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
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


def cartView(request):
    cart = request.session.get('cart', {})  # Получаем корзину из сессии или создаем новую, если она не существует

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        # Добавление товара в корзину
        if product_id:
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity

        # Удаление товара из корзины
        remove_product_id = request.POST.get('remove_product_id')
        if remove_product_id and remove_product_id in cart:
            del cart[remove_product_id]

        # Обновление количества товара в корзине
        update_product_id = request.POST.get('update_product_id')
        if update_product_id and update_product_id in cart:
            cart[update_product_id] = quantity

        # Сохранение корзины в сессии
        request.session['cart'] = cart

        return redirect('cart')

    context = {
        'cart': cart,
    }

    return render(request, 'main/cart.html', context=context)


def categoriesView(request):
    categories = Category.objects.filter(is_published=True)
    context = {
        'categories': categories,
    }
    return render(request, 'main/categories.html', context=context)


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
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()
    if form.is_valid():
        form.save()
        redirect('home')

    context = {
        'title': 'Обратная связь',
        'form': form,
    }
    return render(request, 'main/contact.html', context=context)



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


def postShopView(request, slug):
    return render(request, 'main/post_shop.html')

def postCategoriesView(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category,
    }
    return render(request, 'main/post_categories.html', context=context)
