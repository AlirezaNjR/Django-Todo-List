from django.shortcuts import render , redirect
from .models import TodoModel
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='Home')
def change(request,id):
        if request.method == "GET":
            work = TodoModel.objects.get(id=id)
            if request.user == work.user:
                done = request.GET.get('done')
                if done == 'on':
                    work.done = True
                    work.save()
                return redirect('Home')
            else:
                return redirect('Home')
        else:
            pass

@login_required(login_url='Home')
def add_work(request):
    if request.method == 'GET':
        work = TodoModel()
        title = request.GET.get('title')
        work.title = title
        work.user = request.user
        work.save()
        return redirect('Home')    
    else:
        pass
    
def delete_work(request,id):
    work = TodoModel.objects.get(id=id)
    work.delete()
    return redirect('Home')
