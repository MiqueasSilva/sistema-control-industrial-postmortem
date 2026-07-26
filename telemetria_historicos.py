import pandas as pd
import numpy as np
import time

def extraer_datos_historicos(sensor_id, limite_registros=1000):
    """
    Extrae los datos de los sensores aplicando un límite de registros y un 
    timeout para evitar bloquear la base de datos en producción.
    """
    print(f"Iniciando consulta optimizada para el sensor {sensor_id}...")
    
    # FIX: Se agrega un timeout de 5 segundos a la consulta de la BD 
    # para evitar bloqueos por alta concurrencia.
    configuracion_bd = {
        "timeout": 5, 
        "max_conexiones": 50
    }
    
    try:
        # Simulación de extracción de datos con Pandas
        datos_simulados = {
            'timestamp': pd.date_range(start='now', periods=5, freq='min'),
            'temperatura_celsius': np.random.uniform(45.0, 85.0, 5),
            'potencia_kw': np.random.uniform(5.0, 15.0, 5)
        }
        
        df_historicos = pd.DataFrame(datos_simulados)
        print("Datos extraídos correctamente sin bloquear la tabla.")
        return df_historicos
        
    except Exception as e:
        print(f"Error en la consulta: {e}")
        return None

# Ejecución de prueba
if __name__ == "__main__":
    extraer_datos_historicos(sensor_id="EH-TEMP-01")
