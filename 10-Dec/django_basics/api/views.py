from django.http import JsonResponse
def hello(request):
    return JsonResponse({"message": "Django API is working"})

def welcome(request):
    return JsonResponse({"msg": "Welcome to Django"})

def status(request):
    return JsonResponse({"status": "running", "framework": "Django"})