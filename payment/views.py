from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm

def process_payment(request, order_id):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_details_views')  
    else:
        form = PaymentForm()  
    return render(request, "payment/process_payment.html", {'form': form, 'order_id': order_id})

