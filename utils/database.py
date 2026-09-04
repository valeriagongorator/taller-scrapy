import sqlite3
import pandas as pd

def init_db(db_path='data/database.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS FUENTES (id_fuente INTEGER PRIMARY KEY, nombre TEXT, url TEXT);
    CREATE TABLE IF NOT EXISTS CATEGORIAS (id_categoria INTEGER PRIMARY KEY, nombre TEXT);
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        id_fuente INTEGER, tipo TEXT, nombre TEXT, precio REAL, calificacion INTEGER, url TEXT
    );
    CREATE TABLE IF NOT EXISTS TECNOLOGIA (id_producto INTEGER PRIMARY KEY, descripcion TEXT);
    CREATE TABLE IF NOT EXISTS LIBROS (id_producto INTEGER PRIMARY KEY, id_categoria INTEGER, disponibilidad TEXT, otros_datos TEXT);
    ''')
    cursor.execute("INSERT OR IGNORE INTO FUENTES VALUES (1, 'Webscraper Laptops', 'https://webscraper.io')")
    cursor.execute("INSERT OR IGNORE INTO FUENTES VALUES (2, 'Books to Scrape', 'https://books.toscrape.com')")
    cursor.execute("INSERT OR IGNORE INTO CATEGORIAS VALUES (1, 'General')")
    conn.commit()
    conn.close()

def save_data(df_laptops, df_books, db_path='data/database.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for _, r in df_laptops.iterrows():
        cursor.execute("INSERT INTO PRODUCTOS (id_fuente, tipo, nombre, precio, calificacion, url) VALUES (?, ?, ?, ?, ?, ?)",
                       (r['fuente_id'], r['tipo'], r['nombre'], r['precio'], r['calificacion'], r['url']))
        cursor.execute("INSERT INTO TECNOLOGIA VALUES (?, ?)", (cursor.lastrowid, r['descripcion']))

    for _, r in df_books.iterrows():
        cursor.execute("INSERT INTO PRODUCTOS (id_fuente, tipo, nombre, precio, calificacion, url) VALUES (?, ?, ?, ?, ?, ?)",
                       (r['fuente_id'], r['tipo'], r['nombre'], r['precio'], r['calificacion'], r['url']))
        cursor.execute("INSERT INTO LIBROS VALUES (?, ?, ?, ?)", (cursor.lastrowid, 1, r['disponibilidad'], ''))

    conn.commit()
    conn.close()

def run_queries(db_path='data/database.db'):
    conn = sqlite3.connect(db_path)
    queries = {
        "1. Producto con fuente": "SELECT p.nombre, f.nombre AS fuente FROM PRODUCTOS p JOIN FUENTES f ON p.id_fuente = f.id_fuente LIMIT 3;",
        "2. Info de categorías": "SELECT p.nombre AS libro, c.nombre AS categoria FROM LIBROS l JOIN PRODUCTOS p ON l.id_producto = p.id_producto JOIN CATEGORIAS c ON l.id_categoria = c.id_categoria LIMIT 3;",
        "3. Cantidad por tipo": "SELECT tipo, COUNT(*) AS cantidad FROM PRODUCTOS GROUP BY tipo;",
        "4. Producto más costoso": "SELECT nombre, tipo, precio FROM PRODUCTOS ORDER BY precio DESC LIMIT 1;",
        "5. Producto más económico": "SELECT nombre, tipo, precio FROM PRODUCTOS ORDER BY precio ASC LIMIT 1;",
        "6. Precio promedio": "SELECT ROUND(AVG(precio), 2) AS precio_promedio FROM PRODUCTOS;",
        "7. Calificación promedio": "SELECT ROUND(AVG(calificacion), 2) AS calificacion_promedio FROM PRODUCTOS;",
        "8. Fuente con más productos": "SELECT f.nombre, COUNT(p.id_producto) AS total FROM PRODUCTOS p JOIN FUENTES f ON p.id_fuente = f.id_fuente GROUP BY f.nombre ORDER BY total DESC LIMIT 1;"
    }
    for title, q in queries.items():
        print(f"\n{title}:")
        print(pd.read_sql_query(q, conn).to_string(index=False))
    conn.close()