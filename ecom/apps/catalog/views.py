from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from ecom.apps.cart.forms import CartAddProductForm

# def index(request, template_name):
#     page_title = '产品分类目录'
#     # render django的渲染模板
#     # request 前端发来的请求
#     return render(request, template_name, locals())

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    #过滤指定目录的商品
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(categories=category)
    return render(request,
                  'catalog/product_list.html',
                  {'category': category,
                  'categories': categories,
                  'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                'catalog/product_detail.html',
                {'product': product,
                 'cart_product_form':cart_product_form})

# def show_product(request, product_slug, template_name):
#     p = get_object_or_404(Product, slug=product_slug)
#     categories = p.categories.filter(is_available=True)
#     page_title = p.name
#     # meta_keywords = p.meta_keywords
#     # meta_description = p.meta_description
#     return render(request, template_name, locals())