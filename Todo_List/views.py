from django.shortcuts import render
from Todo.models import TodoModel
# Create your views here.
def home(request):
    todo_list = TodoModel.objects.all()
    return render(request,'home.html',{'todo_list':todo_list})