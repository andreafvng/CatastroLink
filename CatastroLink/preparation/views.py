from django.shortcuts import render

def preparation(request):
    return render(request, "preparation/preparation.html")