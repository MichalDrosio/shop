from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


# Create your views here.

def order_create(request):
    cart = Cart(request)
    user = User.objects.filter(is_active=True)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order':order, 'user':user})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})

