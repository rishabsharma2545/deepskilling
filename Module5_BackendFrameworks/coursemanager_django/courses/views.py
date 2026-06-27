from django.shortcuts import render
from django.http import HttpResponse

# 8. In courses/views.py, create a simple function-based view hello_view 
# that returns an HttpResponse with 'Course Management API is running'.
def hello_view(request):
    return HttpResponse('Course Management API is running')