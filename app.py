import schedule
import time

from datetime import datetime

from savings import generar_monto
from database import crear_tabla, guardar_ahorro
from stats import obtener_estadisticas
from whatsapp import enviar_whatsapp
from config import ALIAS

# NUEVO: CSV
from csv_db import guardar_en_csv


# Crear base de datos si no existe
crear_tabla()


def ahorro_diario():

    # 1. Generar monto del día
    monto = generar_monto()

    # 2. Fecha actual
    ahora = datetime.now()

    fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
    fecha_dia = ahora.strftime("%Y-%m-%d")

    # 3. Guardar en SQLite (control de duplicados)
    guardado = guardar_ahorro(fecha, fecha_dia, monto)

    if not guardado:
        print("⚠️ Ya existe un ahorro para hoy")
        return

    # 4. Estadísticas
    stats = obtener_estadisticas()

    # 5. Guardar en CSV (historial simple)
    guardar_en_csv(fecha, monto, stats["total"])

    # 6. Mensaje WhatsApp
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

    # 7. Enviar WhatsApp
    enviar_whatsapp(mensaje)

    # 8. Logs
    print("\n========================")
    print(mensaje)
    print("💾 Guardado en SQLite + CSV")
    print("========================\n")


# 🔔 Ejecución diaria
schedule.every().day.at("10:00").do(ahorro_diario)

print("🚀 Sistema iniciado...")
print("Esperando ejecución...")


# Loop principal
while True:
    schedule.run_pending()
    time.sleep(1)