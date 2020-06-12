from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from myshop.models import Product
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.owner = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})



@login_required()
def orders_history(request):
    orders = Order.objects.filter(owner=request.user).order_by('created')
    return render(request, 'orders/order/history.html', {'orders':orders})

@login_required()
def detail_order(request, id):
    order = Order.objects.get(pk=id)
    items = OrderItem.objects.filter(order_id=order)
    if order.owner != request.user:
        raise Http404
    return render(request, 'orders/order/detail.html',context={'order': order, 'items': items})


