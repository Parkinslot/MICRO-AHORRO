import sqlite3


def conectar():

    conn = sqlite3.connect("ahorrosv2.db")

    return conn


def crear_tabla():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ahorros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        fecha_dia TEXT UNIQUE,
        monto INTEGER
    )
    """)

    conn.commit()

    conn.close()


def guardar_ahorro(fecha, fecha_dia, monto):

    conn = conectar()

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO ahorros (
            fecha,
            fecha_dia,
            monto
        )
        VALUES (?, ?, ?)
        """, (
            fecha,
            fecha_dia,
            monto
        ))

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()