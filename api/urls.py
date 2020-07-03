from django.urls import path

from api.views import ProductListView, ProductDetailView
app_name ='api'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list_api'),
    path('products/<pk>', ProductDetailView.as_view(), name='product_detail_api')
]