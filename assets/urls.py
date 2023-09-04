from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("companies/", views.CompanyListView.as_view(), name="companies"),
    path("companies/<int:pk>/", views.CompanyDetailView.as_view(), name="company_details"),

    # path("employees/", views.EmployeeListView, name="employees"),
    # path("employees/<int:pk>/", views.EmployeeDetailView, name="employee_details"),

    # path("company/<int:pk>/employees/", views.CompanyEmployeeListView, name="company_employees"),

    # path("assets/", views.AssetListView, name="assets"),
    # path("assets/<int:pk>/", views.AssetDetailView, name="asset_details"),

    # path("employee/<int:pk>/assets/", views.EmployeeAssetListView, name="employee_assets"),

    # path("asset-conditions/", views.AssetConditionListView, name="asset_conditions"),
    # path("asset-conditions/<int:pk>/", views.AssetConditionDetailView, name="asset_condition_details"),

    # path("asset-allocations/", views.AssetAllocationListView, name="asset_allocations"),
    # path("asset-allocations/<int:pk>/", views.AssetAllocationDetailView, name="asset_allocation_details"),

    # path("allocate-asset/", views.AllocateAssetView, name="allocate_asset"),
    # path("deallocate-asset/<int:pk>", views.DeallocateAssetView, name="deallocate_asset"),

    # path("add-asset/", views.AddAssetView, name="add_asset"),
    # path("edit-asset/<int:pk>", views.EditAssetView, name="edit_asset"),
    # path("delete-asset/<int:pk>", views.DeleteAssetView, name="delete_asset"),

    # path("ownership-history/<int:pk>", views.OwnershipHistoryView, name="ownership_history"),

    # path("condition-log/<int:pk>", views.ConditionLogView, name="condition_logs"),
]