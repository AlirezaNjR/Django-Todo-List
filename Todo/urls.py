from django.urls import path 
from .views import change , add_work , delete_work

app_name = 'Todo'

urlpatterns = [
    path('Change/<int:id>',change,name='Change'),
    path('Add/',add_work,name="Add_Work"),
    path('Delete/<int:id>',delete_work,name='Delete_Work'),
]
