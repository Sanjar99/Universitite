from django.http import HttpResponse
from django.shortcuts import render
def groups_list():
    return render(HttpResponse('''<h1>salom</h1>'''))
# Create your views here.
