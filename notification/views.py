from django.shortcuts import render
from  .models import Notification
from  .forms import NotificationUploadForm
# Create your views here.
def notification_details_views(request):
    if request.method=="POST":
     form=NotificationUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=NotificationUploadForm()
    return render(request,'notification/add_notification.html',{'form':form})