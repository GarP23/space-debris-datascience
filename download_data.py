import os
import requests
from tqdm import tqdm

def descargar_dataset_ucs():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*60)
    print("🛰️  SISTEMA DE ADQUISICIÓN DE DATOS - SPACE DEBRIS PROJECT  🛰️")
    print("="*60)
    
    ruta_raw = os.path.join('data', 'raw')
    os.makedirs(ruta_raw, exist_ok=True)
    
    url = "https://www.ucsusa.org/sites/default/files/2024-01/UCS-Satellite-Database-Officialname%205-1-2023%20%28text%29.txt"
    destino = os.path.join(ruta_raw, "ucs_satellites.txt")
    
    print(f"⏳ Conectando con los servidores de la UCS...")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        
        print(f"💾 Descargando base de datos de texto a: '{destino}'")
        
        with open(destino, 'wb') as file, tqdm(
            desc="🛸 Descargando",
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            colour='cyan'
        ) as bar:
            for data in response.iter_content(block_size):
                size = file.write(data)
                bar.update(size)
                
        print("\n" + "="*60)
        print("✅ ¡DESCARGA FINALIZADA CON ÉXITO!")
        print(f"📁 Archivo de texto guardado en: {destino}")
        print("="*60)
        
    except Exception as e:
        print("\n" + "!"*60)
        print(f"❌ Ocurrió un error en la transmisión de datos: {e}")
        print("!"*60)

if __name__ == "__main__":
    descargar_dataset_ucs()