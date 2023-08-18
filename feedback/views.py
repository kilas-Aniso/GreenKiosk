from django.shortcuts import render
from  .models import Feedback
from  .forms import FeedbackUploadForm
# Create your views here.
def feedback_details_views(request):
    if request.method=="POST":
     form=FeedbackUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=FeedbackUploadForm()
    return render(request,'feedback/feedback_details.html',{'form':form})