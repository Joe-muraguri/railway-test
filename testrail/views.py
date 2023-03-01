from django.shortcuts import render

def home(request):
    return render(request, 'testrail/index.html', {})
