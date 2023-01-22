from django.shortcuts import render
from Todo.models import TodoModel
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    user = request.user
    todo_list = TodoModel.objects.filter(user=user,done=False)
    todo_list_done = TodoModel.objects.filter(user=user,done=True)
    return render(request,'home.html',{'todo_list':todo_list,'todo_list_done':todo_list_done})