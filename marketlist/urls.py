'''
@file:     urls.py (marketlist)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Marketlist app URL->Views mappings
@date:     2019
'''

from django.urls import path
from . import views

app_name = 'marketlist'
urlpatterns = [
    path('clean/', views.clean_list, name='clean'),
    path('marketlist/', views.marketlist, name='marketlist'),
    path('', views.home, name='home'),
]
