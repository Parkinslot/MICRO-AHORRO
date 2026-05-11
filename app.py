import schedule
import time

from datetime import datetime

from savings import generar_monto
from database import crear_tabla, guardar_ahorro
from stats import obtener_estadisticas
from whatsapp import enviar_whatsapp
from config import ALIAS


# Crear base si no existe
crear_tabla()

def ahorro_diario():
    monto = generar_monto()
    ahora = datetime.now()

    fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
    fecha_dia = ahora.strftime("%Y-%m-%d")

    guardado = guardar_ahorro(fecha, fecha_dia, monto)

    if not guardado:
        print("⚠️ Ya existe un ahorro para hoy")
        return

    stats = obtener_estadisticas()

    mensaje = f"""
💰 AHORRO HORMIGA

📅 Fecha: {fecha_dia}
💵 Hoy: ${monto}

🏦 Alias:
{ALIAS}

💰 Total: ${stats['total']}
📆 Días: ${stats['cantidad']}
📈 Promedio: ${stats['promedio']}
"""

    enviar_whatsapp(mensaje)

    print(mensaje)


schedule.every(10).minutes.do(ahorro_diario)

print("🚀 Sistema iniciado...")
print("Esperando ejecución...")

while True:
    schedule.run_pending()
    time.sleep(1)