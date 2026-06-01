import os
import sys
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from supabase import create_client, Client
from pathlib import Path

ruta_env = Path(__file__).resolve().parent / 'v3ridia' / '.env'
load_dotenv(dotenv_path=ruta_env)

def inicializar_backend():
    print("CONFIGURANDO CONEXIÓN DEL BACKEND V3RIDIA")

    # 1. CONEXIÓN A FIREBASE (Cloud Firestore)
    try:
        ruta_key = "serviceAccountKey.json"
        if not os.path.exists(ruta_key):
            print("Error: No se encontró el archivo serviceAccountKey.json en la raíz.")
            sys.exit(1)
            
        cred = credentials.Certificate(ruta_key)
        firebase_admin.initialize_app(cred)
        db_firestore = firestore.client()
        print("🔥 Firebase: ¡Conectado con éxito a Cloud Firestore!")
    except Exception as e:
        print(f"❌ Error de conexión con Firebase: {e}")
        db_firestore = None

    # 2. CONEXIÓN A SUPABASE (PostgreSQL & Storage)
    try:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_ANON_KEY")
        
        if not supabase_url or not supabase_key:
            print("❌ Error: Variables SUPABASE_URL o SUPABASE_ANON_KEY ausentes en el .env")
            sys.exit(1)
            
        supabase_client: Client = create_client(supabase_url, supabase_key)
        print("⚡ Supabase: ¡Conectado con éxito a PostgreSQL & Storage!")
    except Exception as e:
        print(f"❌ Error de conexión con Supabase: {e}")
        supabase_client = None

    if db_firestore and supabase_client:
        print("SISTEMA HÍBRIDO INTEGRADO Y OPERANDO CON ÉXITO")

    
    return db_firestore, supabase_client

if __name__ == "__main__":
    db, supabase = inicializar_backend()