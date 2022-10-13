from django.shortcuts import render
from django.http import HttpResponse

# this is where we write functions for request -> respond
# its a reqeust handler
# Create your views here.
def say_hello(request):
    return render(request,'hello.html', {'name': 'Kaks'})