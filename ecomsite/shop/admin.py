from django.contrib import admin
from .models import Products,Order


# Register your models here.

admin.site.site_header="E COMMERCE SITE"
admin.site.site_title="XYZ SHOP"
admin.site.index_title=" XYZ MANAGER"

class ProductAdmin(admin.ModelAdmin):

    # change_category_to_default.short_description='Default Category'
    list_display=('title','price','discount_price','category','description','image')
    search_fields=('title','category',)
    actions=('change_category_to_default',)
    fields=('title','price')
    list_editable=('price','category',)

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description='Default Category'
admin.site.register(Products,ProductAdmin)

admin.site.register(Order)

