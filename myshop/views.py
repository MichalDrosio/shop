from PIL.ImagePalette import random
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import FormView
from taggit.models import Tag
from cart.cart import Cart
from orders.models import Order, OrderItem
from .forms import SearchProductFrom
from taggit.models import Tag
from .models import Category, Product, Pictrue
from cart.forms import CardAddProductFrom
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def product_list(request, category_slug=None, tag_slug=None):
    category = None
    tag = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'myshop/list.html',
                  context={'category': category, 'categories': categories, 'products': products, 'page': page, 'tag': tag})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    pictrues = Pictrue.objects.filter(product_id=product)
    cart_product_form = CardAddProductFrom()
    return render(request, 'myshop/detail.html', context={'product': product, 'cart_product_form': cart_product_form, 'pictrues': pictrues})

@login_required
@require_POST
def product_like(request):
    product_id = request.POST.get('id')
    action = request.POST.get('action')
    if product_id and action:
        try:
            product = Product.objects.get(id=product_id)
            if action == 'like':
                product.users_like.add(request.user)
            else:
                product.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ok'})
