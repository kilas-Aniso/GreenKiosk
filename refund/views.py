from django.shortcuts import render
from  .models import Refund
from  .forms import RefundUploadForm
# Create your views here.


def refund_details_views(request):
    if request.method=="POST":
     form=refundUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=RefundUploadForm()
    return render(request,'refund/refund_details.html',{'form':form})