import schedule
import time

from datetime import datetime

from savings import generar_monto

from database import (
    crear_tabla,
    guardar_ahorro
)

from stats import obtener_estadisticas

from whatsapp import enviar_whatsapp

from config import ALIAS


# Crear tabla
crear_tabla()


def ahorro_diario():

    monto = generar_monto()

    ahora = datetime.now()

    fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")

    fecha_dia = ahora.strftime("%Y-%m-%d")

    # Guardar ahorro
    guardado = guardar_ahorro(
        fecha,
        fecha_dia,
        monto
    )

    # Evitar duplicados
    if not guardado:

        print("⚠️ Ya existe un ahorro para hoy")

        return

    # Estadísticas
    stats = obtener_estadisticas()

    # Mensaje WhatsApp
    mensaje = f"""
💰 AHORRO HORMIGA

📅 Fecha: {fecha_dia}

💵 Hoy deberías ahorrar: ${monto}

🏦 Alias para transferir:
{ALIAS}

📊 ESTADÍSTICAS

💰 Total acumulado: ${stats['total']}
📆 Días ahorrando: {stats['cantidad']}
📈 Promedio diario: ${stats['promedio']}

🔥 Crezco economicamente dia a dia
"""

    # Enviar WhatsApp
    enviar_whatsapp(mensaje)

    # Consola
    print("\n========================")
    print(mensaje)
    print("✅ WhatsApp enviado")
    print("========================\n")


# EJECUCIÓN DIARIA
schedule.every(30).seconds.do(ahorro_diario)

print("🚀 Sistema iniciado...")
print("Esperando ejecución...")


while True:

    schedule.run_pending()

    time.sleep(1)