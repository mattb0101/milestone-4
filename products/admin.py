from django.contrib import admin
from .models import Product, Category, Sub_Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'cat_friendlyname',
        'cat_name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'subcat_friendlyname',
        'subcat_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, SubCategoryAdmin)
