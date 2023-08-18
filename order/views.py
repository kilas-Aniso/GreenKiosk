from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_view")
    else:
        form = OrderForm()
    return render(request, "order/place_order.html", {'form': form})

def order_view(request):
    orders = Order.objects.all()
    return render(request, 'order/order_view.html', {'orders': orders})
