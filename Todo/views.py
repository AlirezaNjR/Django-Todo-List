from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import TodoModel
# Create your views here.
def change(request,id):
    if request.method =="GET":
        work = TodoModel.objects.get(id=id)
        done = request.GET.get('done')
        if done == 'on':
            work.done = True
            work.save()
        return redirect('Home')
       