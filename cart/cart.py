class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
