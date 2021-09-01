from django.shortcuts import redirect


def unauthenticated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect("home_page")
    
    return view_func(request, *args, **kwargs)
  
  return wrapper_func


def for_allowed_users_only(allowed_roles: tuple):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):
      if request.user.username in allowed_roles:
        return view_func(request, *args, **kwargs)
      
      return redirect("home_page")
    return wrapper_func
  return decorator