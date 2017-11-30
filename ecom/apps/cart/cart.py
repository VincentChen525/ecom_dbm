from decimal import Decimal
from django.conf import settings
from ecom.apps.catalog.models import Product

# 这个Cart类用于管理购物车。我们要求用request对象初始化购物车。
# 我们用self.session = request.session存储当前会话，以便在Cart类的其它方法中可以访问。
# 首先，我们用self.session.get(settings.CART_SESSION_ID)尝试从当前会话中获得购物车。
# 如果当前会话中没有购物车，通过在会话中设置一个空字典来设置一个空的购物车。
# 我们希望购物车字典用商品ID做为键，一个带数量和价格的字典作为值。
# 这样可以保证一个商品不会在购物车中添加多次；同时还可以简化访问购物车的数据。
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    #add products
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the sessions as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # 我们将需要迭代购物车中的商品，并访问关联的Product实例。
    # 我们检索购物车中的Product实例，并把它们包括在购物车商品中。
    # 最后，我们迭代购物车商品，把price转换回Decimal类型，并为每一项添加total_price属性。
    def __iter__(self):
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # 当在一个对象上调用len()函数时，Python会调用__len__()方法返回对象的长度。
    # 我们定义一个__len__()方法，返回购物车中所有商品的总数量。
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True