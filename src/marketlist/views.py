from django.shortcuts import render, redirect, reverse
from .models import Item


def clean_list(request):
    Item.objects.all().delete()
    return redirect(reverse('marketlist:marketlist'))


def marketlist(request):
    if request.method == 'POST':
        Item.objects.create(name=request.POST.get('name'))
        return redirect(reverse('marketlist:marketlist'))
    return render(request, 'marketlist.html', {'items': Item.objects.all()})


def home(request):
    return redirect(reverse('marketlist:marketlist'))
