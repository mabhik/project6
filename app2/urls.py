from django.urls import path
from app2.views import html,appp2fil,a2f2

app_name='friday'

urlpatterns=[
    path('html/',html,name='html'),
    path('appp2fil/',appp2fil,name='appp2fil'),
    path('a2f2/',a2f2,name='a2f2'),
]