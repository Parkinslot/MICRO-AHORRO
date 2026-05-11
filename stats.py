import sqlite3


def obtener_estadisticas():

    conn = sqlite3.connect("ahorros.db")

    cursor = conn.cursor()

    # Total ahorrado
    cursor.execute("SELECT SUM(monto) FROM ahorros")
    total = cursor.fetchone()[0]

    # Cantidad de ahorros
    cursor.execute("SELECT COUNT(*) FROM ahorros")
    cantidad = cursor.fetchone()[0]

    # Promedio
    cursor.execute("SELECT AVG(monto) FROM ahorros")
    promedio = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total or 0,
        "cantidad": cantidad or 0,
        "promedio": round(promedio or 0, 2)
    }