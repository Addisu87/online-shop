from .cart import Cart

# create a context processor to set the current cart
# in the request context.


def cart(request):
    return {'cart': Cart(request)}
