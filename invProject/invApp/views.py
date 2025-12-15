from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .form import ProductForm
from .models import Product
from django.views.decorators.csrf import csrf_exempt

def home_view(request):
    return JsonResponse({'message': 'Welcome to the API'}, status=200)

@csrf_exempt
def product_create_view(request):
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Method not allowed'},
            status=405
        )

    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return JsonResponse({
            'id': product.product_id,
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'status': 'created'
        }, status=201)

    return JsonResponse({'errors': form.errors}, status=400)

def product_list_view(request):
    products = Product.objects.all().values('product_id', 'name', 'price', 'quantity', 'sku')
    if products.__len__() > 0:
        return JsonResponse(list(products), safe=False, status=200)
    else: 
        return JsonResponse({'message': 'No products found'}, status=404)

@csrf_exempt
def product_update_view(request, product_id):
    try:
        product = get_object_or_404(Product, product_id=product_id)

        if request.method != 'POST':
            return JsonResponse({'error': 'Method not allowed'}, status=405)

        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                'id': product.product_id,
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
                'status': 'updated'
            }, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def product_delete_view(request, product_id):
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Method not allowed'},
            status=405
        )

    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'status': 'deleted', 'product_id': product_id}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
