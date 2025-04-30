from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    response = { "message": "success call" }
    return JsonResponse(response, status=200)

@csrf_exempt
def generar_factura(request):
    if request.method == 'POST':
        
        try:
            # Usa request.body para obtener el cuerpo de la solicitud
            data = json.loads(request.body.decode('utf-8'))  # Decodifica y analiza el JSON
            print(data)
            return JsonResponse({"message": "Data received", "data": data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

