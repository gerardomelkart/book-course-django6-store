from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Comment
from .forms import CommentForm


# Create your views here.
# def add(request):
#     # return HttpResponse("Hello, World!")
#     if request.method == 'GET':
#         return render(request, 'coments/add.html') 
#     else:
#         coment = Comment()
#         coment.text = request.POST['text']
#         coment.save()
#         return HttpResponse(request.POST.get('text'))

def add(request):
    # return HttpResponse("Hello, World!")
    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'coments/add.html', {'form': form}) 
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        #return HttpResponse("hola")
        return redirect('index')

        # coment = Comment()
        # coment.text = request.POST['text']
        # coment.save()
        # return HttpResponse(request.POST.get('text'))



# sin paginar
# def index(request):
#     comments = Comment.objects.all()
#     return render(request, 'coments/index.html', {'comments': comments})


def index(request):
    comments = get_list_or_404(Comment)
    paginator = Paginator(comments, 15)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    return render(request, 'coments/index.html', {'comments': comments_page})


def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk) 
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'coments/add.html', {'form': form, 'comment': comment})
    #return redirect('index')
    
def delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('index')
    # return HttpResponse("ok")