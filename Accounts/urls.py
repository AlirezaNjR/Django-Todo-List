from django.urls import path
from .views import signup

app_name = 'Accounts'

urlpatterns = [
    path('Signup/',signup,name='Signup'),
]
