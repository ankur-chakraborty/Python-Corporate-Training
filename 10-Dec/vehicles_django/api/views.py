
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle

@csrf_exempt
def vehicle_api(request):
    if request.method == 'GET':
        vehicles = list(Vehicle.objects.values())
        return JsonResponse(vehicles, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        Vehicle.objects.create(
            number_plate=data['number_plate'],
            vehicle_type=data['vehicle_type'],
            manufacturer=data['manufacturer'],
            year=data['year']
        )
        return JsonResponse({"message": "POST EXECUTED"})

    elif request.method == 'PUT':
        data = json.loads(request.body)
        try:
            vehicle = Vehicle.objects.get(id=data['id'])
            vehicle.number_plate = data['number_plate']
            vehicle.vehicle_type = data['vehicle_type']
            vehicle.manufacturer = data['manufacturer']
            vehicle.year = data['year']
            vehicle.save()
            return JsonResponse({"message": "PUT EXECUTED"})
        except Vehicle.DoesNotExist:
            return JsonResponse({"error": "Vehicle not found"}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        try:
            vehicle = Vehicle.objects.get(id=data['id'])
            vehicle.delete()
            return JsonResponse({"message": "DELETE EXECUTED"})
        except Vehicle.DoesNotExist:
            return JsonResponse({"error": "Vehicle not found"}, status=404)

