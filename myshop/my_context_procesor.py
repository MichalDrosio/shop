from random import shuffle

from myshop.models import Product


def random_products(request):
    products = Product.objects.all()
    random_products = list(products)
    shuffle(random_products)
    return {'random_products': random_products[0:4], 'request': request}