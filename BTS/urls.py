from BTS.views import *

from django.urls import path
app_name='BTS'

urlpatterns=[

    path('jungkook/',jungkook,name='jungkook'),
    path('jhope/',jhope,name='jhope'),
]