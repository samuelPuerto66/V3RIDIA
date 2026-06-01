# api/views.py
from django.http import JsonResponse
from supabase import create_client
import os

def test_supabase(request):
    # Usamos las mismas credenciales que ya tienes configuradas
    url = "https://sreyqkkfgsywsymwsbwo.supabase.co" # Reemplaza con tus datos
    key = "sb_publishable_QK-561VBhw2bQbcVOL9q0w_hqC0Vf84" # Reemplaza con tus datos
    
    try:
        supabase = create_client(url, key)
        # Hacemos una consulta simple para ver si conecta (ej: contar tablas o seleccionar un dato)
        # Si tienes una tabla llamada 'tokens_recompensas', prueba con esto:
        response = supabase.table('tokens_recompensas').select('*').limit(1).execute()
        
        return JsonResponse({
            "status": "success",
            "message": "¡Conexión a Supabase exitosa desde Django!",
            "data": "Conectado correctamente"
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)# api/views.py
