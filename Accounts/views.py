from .forms import SignUpForm
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            try:
                User.objects.get(username=form.cleaned_data['username'])
                return HttpResponse('<h1>نام کاربری وجود دارد</h1>')
            except:
                user = User()
                user.username = form.cleaned_data['username']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                c_password = form.cleaned_data['c_password']
                # user.save()
                if password == c_password :
                    if len(password) >= 8 :
                        user.set_password(password)
                user.save()
                return redirect('Home')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})
    