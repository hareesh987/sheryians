from django.urls import path
from .views import *
app_name='sheryians_app'

urlpatterns=[
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('signin/',signin,name='signin'),
]