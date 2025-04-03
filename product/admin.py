from django.contrib import admin

from product.models import Product

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','descriptions','price','company']
    search_fields=['name']