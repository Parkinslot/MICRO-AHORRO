import csv
import os

FILE = "ahorros.csv"


def inicializar_csv():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["fecha", "monto", "total"])


def guardar_en_csv(fecha, monto, total):
    inicializar_csv()

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([fecha, monto, total])