from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import TopicForm
from .models import UploadTopics
# Create your views here.

def success(request):
    return HttpResponse("Your file is uploaded")
    
def entry(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success") 
    else:
        form = TopicForm()
    

    return render(request, "upload.html", {
        "form": form
    })
    