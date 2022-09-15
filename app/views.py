from django.shortcuts import render

def index_view(request, *args, **kwargs):
    return render(request, "index.html") 