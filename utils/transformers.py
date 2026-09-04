import pandas as pd
import re

def clean_price(val):
    if not val:
        return 0.0
    clean_val = re.sub(r'[^\d.]', '', str(val))
    return float(clean_val) if clean_val else 0.0

def process_laptops(raw_data):
    df = pd.DataFrame(raw_data)
    if df.empty:
        return df
    df['nombre'] = df['nombre'].str.strip()
    df['precio'] = df['precio'].apply(clean_price)
    df['descripcion'] = df['descripcion'].str.strip()
    df['tipo'] = 'Tecnologia'
    df['fuente_id'] = 1
    return df.drop_duplicates().dropna(subset=['nombre', 'precio'])

def process_books(raw_data):
    df = pd.DataFrame(raw_data)
    if df.empty:
        return df
    df['nombre'] = df['nombre'].str.strip()
    df['precio'] = df['precio'].apply(clean_price)
    df['tipo'] = 'Libros'
    df['fuente_id'] = 2
    return df.drop_duplicates().dropna(subset=['nombre', 'precio'])