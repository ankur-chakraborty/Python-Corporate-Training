# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
#
# # def hello(request):
# #     return JsonResponse({"message": "Django API is working"})
# #
# # def welcome(request):
# #     return JsonResponse({"message": "Welcome to Django API"})
# #
# # def status(request):
# #     return JsonResponse({"status": "running", "framework":"Django"})
#
# @csrf_exempt
# def employees(request):
#     if request.method == "GET":
#         return JsonResponse({"message":"GET EXECUTED"})
#     if request.method == "POST":
#         return JsonResponse({"message":"POST EXECUTED"})
#     if request.method == "PUT":
#         return JsonResponse({"message":"PUT EXECUTED"})
#     if request.method == "DELETE":
#         return JsonResponse({"message":"DELETE EXECUTED"})
#
#
#
#
# # Create your views here.


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json

@csrf_exempt
def employees(request):

    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Employee.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Employee.objects.create(
            name=body["name"],
            role=body["role"],
            salary=body["salary"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        emp = Employee.objects.get(id=body["id"])
        emp.name = body["name"]
        emp.role = body["role"]
        emp.salary = body["salary"]
        emp.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        emp = Employee.objects.get(id=body["id"])
        emp.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
