from django.shortcuts import render
from assets.decorators import admin_required, manager_required
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Home Page")

@manager_required
def assets_list(request):
    return HttpResponse("Assets list")

@manager_required
def employee_list(request):
    return HttpResponse("Employee list")