from django.urls import path
from app1.views import *

app_name="thinking"

urlpatterns = [
    path('abhi/',abhi,name='abhi')
]
