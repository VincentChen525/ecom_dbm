from .cart import Cart

# 上下文处理器 它将request对象作为参数，返回一个对象的字典
# 这些对象可用于所有使用RequestContext渲染的模板
def cart(request):
    return {'cart': Cart(request)}