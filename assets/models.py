from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_by",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_updated_by",
    )

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    # Add your additional fields here
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    
    class Meta:
        permissions = [
            ("can_view_employee", "Can view employee"),
            ("can_view_manager", "Can view manager"),
            ("can_allocate_asset", "Can allocate asset"),
            ("can_deallocate_asset", "Can deallocate asset"),
            ("can_view_asset", "Can view asset"),
            ("can_add_asset", "Can add asset"),
            ("can_edit_asset", "Can edit asset"),
            ("can_delete_asset", "Can delete asset"),
            ("can_view_asset_condition", "Can view asset condition"),
            ("can_add_asset_condition", "Can add asset condition"),
            ("can_edit_asset_condition", "Can edit asset condition"),
            ("can_delete_asset_condition", "Can delete asset condition"),
            ("can_return_asset", "Can return asset"),
        ]

class Company(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField()
    employees = models.ManyToManyField(CustomUser, related_name='employees')

class Device(BaseModel):
    device_type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    current_condition = models.CharField(max_length=50)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='devices_owned')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices_owned')

class ConditionLog(BaseModel):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='condition_logs')
    employee_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='condition_logs_allocated')
    allocation_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True)
    condition_on_allocation = models.TextField()
    condition_on_return = models.TextField()

    class Meta:
        ordering = ['-allocation_date']
