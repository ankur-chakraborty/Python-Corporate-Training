from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

import json

from .models import Product


def get_products(request):
    products = list(Product.objects.values())

    return JsonResponse(products, safe=False)


def get_product(request, id):
    try:

        product = Product.objects.get(id=id)

        data = {

            'id': product.id,

            'name': product.name,

            'price': product.price,

            'description': product.description,

        }

        return JsonResponse(data)

    except Product.DoesNotExist:

        return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        data = json.loads(request.body)

        product = Product.objects.create(

            name=data['name'],

            price=data['price'],

            description=data.get('description', "")

        )

        return JsonResponse({"message": "Product created successfully", "id": product.id}, status=201)


@csrf_exempt
def update_product(request, id):
    if request.method == "PUT":

        try:

            product = Product.objects.get(id=id)

            data = json.loads(request.body)

            product.name = data.get("name", product.name)

            product.price = data.get("price", product.price)

            product.description = data.get("description", product.description)

            product.save()

            return JsonResponse({"message": "Product updated successfully", "id": product.id}, status=200)

        except Product.DoesNotExist:

            return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
def delete_product(request, id):
    if request.method == "DELETE":

        try:

            product = Product.objects.get(id=id)

            product.delete()

            return JsonResponse({'message': 'Product deleted successfully'}, status=200)

        except Product.DoesNotExist:

            return JsonResponse({'error': 'Product not found'}, status=404)

