from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'adress', 'postal_code', 'city', 'paid', 'created', 'update']
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInline]



admin.site.register(Order, OrderAdmin)