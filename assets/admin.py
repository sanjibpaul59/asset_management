from django.contrib import admin

# Register your models here.
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('role',)
    filter_horizontal = ()

admin.site.register(models.CustomUser, UserAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation', 'joining_date')
    list_filter = ('department', 'designation')
    search_fields = ('user', 'department', 'designation')
    ordering = ('user',)
    filter_horizontal = ()

admin.site.register(models.Employee, EmployeeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email')
    list_filter = ('name','email')
    search_fields = ('name', 'address', 'phone', 'email')
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(models.Company, CompanyAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'model', 'os', 'serial_number',)
    list_filter = ('device_type', 'model', 'os', 'serial_number')
    search_fields = ('device_type', 'model', 'os', 'serial_number')
    ordering = ('device_type',)

admin.site.register(models.Device, DeviceAdmin)

class ConditionLogAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'allocation_date', 'return_date', 'condition_on_allocation', 'condition_on_return')
    list_filter = ('device_id',)
    search_fields = ('device_id',)
    ordering = ('allocation_date',)
    filter_horizontal = ()

admin.site.register(models.ConditionLog, ConditionLogAdmin)