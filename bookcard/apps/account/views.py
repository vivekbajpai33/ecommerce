from django.shortcuts import render, HttpResponse

def account_home(request):
    return render(request, 'home/dashboard.html')