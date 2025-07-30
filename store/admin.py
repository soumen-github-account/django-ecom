from django.contrib import admin
from .models import catagory,product,Cart,Order,OrderItem,Profile,slide1,slide2,slide3,slide4
# Register your models here.


class AdminCart(admin.ModelAdmin):
    list_display=['user', 'product', 'product_qty']


admin.site.register(catagory)
admin.site.register(product)
admin.site.register(Cart, AdminCart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(slide1)
admin.site.register(slide2)
admin.site.register(slide3)
admin.site.register(slide4)