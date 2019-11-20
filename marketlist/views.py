from django.shortcuts import render, redirect, reverse


def marketlist(request):
    return render(request, 'marketlist.html')


def home(request):
    return redirect(reverse('marketlist'))
