---

## 📌 Nota sobre la Consolidación de Datos y Trabajo en Equipo

El desarrollo de este laboratorio se realizó de manera colaborativa entre **Vanessa Mena** y **Valeria Góngora**. Debido a la distribución de tareas y la ejecución en entornos de desarrollo independientes, se presentaron las siguientes dinámicas en el proyecto:

1. **Entorno de Extracción Completa (Valeria Góngora):**
   * Corresponde al pipeline de extracción ETL ejecutado desde el script principal (`main.py`).
   * Procesó el catálogo completo mediante Scrapy, consolidando **117 productos de Tecnología** y **20 Libros** en la base de datos SQLite.

2. **Entorno de Pruebas y Consultas SQL (Vanessa Mena):**
   * Corresponde a la construcción y validación de las sentencias SQL (`JOIN`, `GROUP BY`, agregaciones).
   * Dichas consultas se validaron sobre un entorno local con un conjunto de datos de muestra, motivo por el cual los resultados numéricos en las capturas de ese entorno difieren del volumen total del script principal.

*La lógica de desarrollo, las estructuras de datos y la sintaxis SQL son totalmente válidas y equivalentes en ambos entornos.*
