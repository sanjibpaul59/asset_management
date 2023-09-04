from django.http import HttpResponseForbidden

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")
    return _wrapped_view

def manager_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'manager' or request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")
    return _wrapped_view