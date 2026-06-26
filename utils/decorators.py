from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse


def superuser_required(login_url='login'):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.user.is_authenticated and request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            return redirect(reverse(login_url))

        return wrapper

    return decorator