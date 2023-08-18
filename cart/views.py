from django.shortcuts import render, redirect
from .models import Cart
from .forms import CartForm
def cart_view(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items})
def add_to_cart(request):
    cart_items = Cart.objects.all()
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart_view")
    else:
        form = CartForm()
    return render(request, "cart/add_to_cart.html", {'form': form})

