from django.shortcuts import render
from django.http import HttpResponse

from .models import Comment

# Create your views here.
def add(request):
    # return HttpResponse("Hello, World!")
    if request.method == 'GET':
        return render(request, 'coments/add.html') 
    else:
        coment = Comment()
        coment.text = request.POST['text']
        coment.save()
        return HttpResponse(request.POST.get('text'))