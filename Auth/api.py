from Auth.models import *
from django.http import JsonResponse

def duplicate_email(request):
    email = request.GET.get('email')
    user_obj = user.objects.filter(email=email)
    if user_obj.exists():
        return JsonResponse({"status":409})
    return JsonResponse({"status":200})
    
