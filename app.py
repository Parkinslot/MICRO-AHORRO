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

    # Guardar ahorro (solo 1 por día)
    guardado = guardar_ahorro(fecha, fecha_dia, monto)

    if not guardado:
        print("⚠️ Ya existe un ahorro para hoy")
        return

    stats = obtener_estadisticas()

    mensaje = f"""
💰 AHORRO HORMIGA

📅 Fecha: {fecha_dia}

💵 Hoy deberías ahorrar: ${monto}

🏦 Alias:
{ALIAS}

📊 ESTADÍSTICAS

💰 Total acumulado: ${stats['total']}
📆 Días ahorrando: ${stats['cantidad']}
📈 Promedio diario: ${stats['promedio']}

🔥 Seguimos construyendo el hábito.
"""

    enviar_whatsapp(mensaje)

    print("\n========================")
    print(mensaje)
    print("✅ WhatsApp enviado")
    print("========================\n")


# 🔔 EJECUCIÓN DIARIA REAL
schedule.every().day.at("11:20").do(ahorro_diario)

print("🚀 Sistema iniciado...")
print("Esperando ejecución...")


while True:
    schedule.run_pending()
    time.sleep(1)