from RCB.views import *

from django.urls import path
app_name='RCB'

urlpatterns=[

    path('virat/',virat,name='virat'),
    path('maxwell/',maxwell,name='maxwell'),
]