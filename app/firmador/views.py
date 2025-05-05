from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

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
            @todo necesito revisar todos los elementos que se tienen que revisar en la factura
           
            return JsonResponse({"Message": "Certificate path does exist"}, status=200)   
            return JsonResponse({"message": "Data received", "hacienda_user": os.listdir(certpath)}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

