from django.shortcuts import render

# This is the view that you imported in the frontend/urls.py
def indexView(request, *args, **kwargs):
    return render(request, "index.html")  # notice the template used here
