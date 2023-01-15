from django.urls import path 
from .views import change
app_name = 'Todo'

urlpatterns = [
    path('Change/<int:id>',change,name='Change'),
]
