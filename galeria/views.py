from django.shortcuts import render
from django.http import HttpResponse

html = '''
<h1>Hello, my name is Caio Araujo</h1>
<p>This is my first project using django totally in english</p>
'''

def index(request):
    return HttpResponse(html)
