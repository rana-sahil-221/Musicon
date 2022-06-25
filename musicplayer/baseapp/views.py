from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import Song
from django.http import HttpResponse

# OUr homepage view for musicplayer - Musicon

def home(request):
    paginator = Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj}
    return render(request,"baseapp/index.html",context)


