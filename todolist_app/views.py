from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    # return HttpResponse('Welcome to Task page')
    return render(request, 'todolist.html', {})