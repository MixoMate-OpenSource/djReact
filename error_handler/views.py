from django.shortcuts import render

# Create your views here.
def error_404(request,exception):
    return render(request,'error_page.html',{"number":404,"error_text":"Page Not Found","oops":"Oops..."})
def error_403(request,exception):
    return render(request,'error_page.html',{"number":403,"error_text":"You are not allowed here","oops":"Sorry..."})
def error_400(request,exception):
    return render(request,'error_page.html',{"number":400,"error_text":"Bad request.","oops":"No No No..."})
def error_500(request):
    return render(request,'error_page.html',{"number":500,"error_text":"There is something wrong","oops":"Oops..."})