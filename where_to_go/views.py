import os
from django.shortcuts import render
from django.conf import settings


def show_index_page(request):
    return render(request, 'index.html')
