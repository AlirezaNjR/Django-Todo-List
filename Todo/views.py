from .models import TodoModel
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
@login_required(login_url='login')
def change(request,id):
    work = TodoModel.objects.get(id=id)
    
    if request.user == work.user:
        work.done = True
        work.save()
        return redirect('Home')
    else:
        return HttpResponse('403')

@login_required(login_url='login')
def add_work(request):
    if request.method == 'GET':
        work = TodoModel()
        title = request.GET.get('title')
        work.title = title
        work.user = request.user
        work.save()
        return redirect('Home')    
    else:
        return HttpResponse('eer')
    
@login_required(login_url='login')    
def delete_work(request,id):
    work = TodoModel.objects.get(id=id)
    if request.user == work.user:
        work.delete()
        return redirect('Home')
    else :
        return HttpResponse('404')
