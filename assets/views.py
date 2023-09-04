from django.shortcuts import render
from assets.decorators import admin_required, manager_required
# Create your views here.
from django.http import HttpResponse, JsonResponse

from django.views import View
from .models import Company, CustomUser, Device

def index(request):
    return HttpResponse("Hello, world. You're at the Home Page")

@manager_required
def assets_list(request):
    return HttpResponse("Assets list")

@manager_required
def employee_list(request):
    return HttpResponse("Employee list")

class CompanyListView(View):
    def get(self, request):
        companies = Company.objects.all()
        return JsonResponse(list(companies.values()), safe=False)

class CompanyDetailView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        print(company)
        return JsonResponse({"company": "company"}, safe=False)

class EmployeeListView(View):
    def get(self, request):
        employees = CustomUser.objects.all()
        return JsonResponse(list(employees.values()), safe=False)

class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = CustomUser.objects.get(pk=pk)
        return JsonResponse(employee.to_dict(), safe=False)

class CompanyEmployeeListView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        employees = company.employees.all()
        return JsonResponse(list(employees.values()), safe=False)


class AssetListView(View):
    def get(self, request):
        assets = Device.objects.all()
        return JsonResponse(list(assets.values()), safe=False)

class AssetDetailView(View):
    def get(self, request, pk):
        asset = Device.objects.get(pk=pk)
        return JsonResponse(asset.to_dict(), safe=False)
