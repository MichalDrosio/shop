from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from .models import Category, Product
from cart.forms import CardAddProductFrom
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'myshop/list.html',
                  context={'category':category, 'categories':categories, 'products':products, 'page':page})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CardAddProductFrom()
    return render(request, 'myshop/detail.html', context={'product':product, 'cart_product_form':cart_product_form})





