from django.contrib import admin
from .models import Category, Product
#from .forms import ProductAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #form = ProductAdminForm #自定义校验
    # 设置admin界面如何显示产品列表
    list_display = ('name','slug', 'price', 'quantity','is_available', 'created_at', 'updated_at',)
    list_filter = ('is_available','created_at','updated_at')
    list_editable = ('price','quantity','is_available')
    # list_display_links = ('name',)
    # list_per_page = 50
    # ordering = ['-created_at']
    # search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    # exclude = ('created_at', 'updated_at',) #不显示
    prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Product, ProductAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # list_display_links = ('name',)
    # list_per_page = 20
    # ordering = ['name']
    # search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    # exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Category, CategoryAdmin)
