from django.shortcuts import render
from .models import Customer

from .forms import CustomerUploadForm

# Create your views here.
def customer_upload_view(request):
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CustomerUploadForm()
    return render(request, 'customer/customer_upload_view.html',{'form':form})

