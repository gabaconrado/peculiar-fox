'''
@file:     models.py (Marketlist)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Marketlist app models
@date:     2019
'''
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20)
