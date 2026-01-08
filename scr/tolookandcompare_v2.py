# ===========================================================
#   FUNCIONES SAFE para análisis de columnas:
#   - to_doc_info
#   - to_doc_headtail
#   - transform_info
#   - transform_headtail (NUEVA versión segura)
#
#   NOTA IMPORTANTE:
#   Ninguna de estas funciones modifica el DataFrame original.
#   Son seguras para columnas numéricas y categóricas.
# ===========================================================

import pandas as pd


# -------------------------------------------------------------
# FUNCIÓN 1 — to_doc_info (SAFE)
# -------------------------------------------------------------
def to_doc_info(df: pd.DataFrame, columna: str) -> None:
    """
    Reporte formateado con:
    - información general
    - frecuencias
    - estadísticas numéricas (si se pueden calcular)
    No modifica el DataFrame original.
    """

    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    frecuencias = "\n".join([
        f"||{idx}  {val}"
        for idx, val in df[columna]
            .value_counts(normalize=True, dropna=False)
            .mul(100).round(2)
            .items()
    ])

    temp_col = pd.to_numeric(df[columna], errors='coerce')

    if temp_col.notna().sum() > 0:
        stats = temp_col.agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        mean, median, mode = stats['Mean'], stats['Median'], stats['Mode']
    else:
        mean = median = mode = "N/A (no numérico)"

    reporte = f"""
|    dtype: {dtype}  |   {columna}   |
|-----------|---------------|
||
{frecuencias}
||<br>
||**Media:** {mean}
||**Mediana:** {median}
||**Moda:** {mode}
||<br>
||Valores únicos: **{valores_unicos}**
||Número de registros: **{num_registros}**
||Valores nulos: **{valores_nulos}**
||Registros duplicados: **{duplicados}**|
---
"""
    print(reporte)


# -------------------------------------------------------------
# FUNCIÓN 2 — to_doc_headtail (SAFE)
# -------------------------------------------------------------
def to_doc_headtail(df: pd.DataFrame, columna: str) -> None:
    """
    Muestra Top 5 + Bottom 5 de frecuencias
    y estadísticas numéricas cuando es posible.
    No modifica el DataFrame original.
    """

    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    
    top5 = "\n".join([f"||{idx}  {val}%" for idx, val in frecuencias.head(5).items()])
    bottom5 = "\n".join([f"||{idx}  {val}%" for idx, val in frecuencias.tail(5).items()])

    temp_col = pd.to_numeric(df[columna], errors='coerce')

    if temp_col.notna().sum() > 0:
        stats = temp_col.agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        mean, median, mode = stats['Mean'], stats['Median'], stats['Mode']
    else:
        mean = median = mode = "N/A (no numérico)"

    reporte = f"""
|    dtype: {dtype}  |   {columna}   |
|-----------|---------------|
||
||**Top 5:**
{top5}
||**Bottom 5:**
{bottom5}
||<br>
||**Media:** {mean}
||**Mediana:** {median}
||**Moda:** {mode}
||<br>
||Valores únicos: **{valores_unicos}**
||Número de registros: **{num_registros}**
||Valores nulos: **{valores_nulos}**
||Registros duplicados: **{duplicados}**|
---
"""
    print(reporte)


# -------------------------------------------------------------
# FUNCIÓN 3 — transform_info (SAFE)
# -------------------------------------------------------------
def transform_info(df: pd.DataFrame, columna: str) -> None:
    """
    Muestra:
    - Frecuencias
    - Información general
    - Estadísticas numéricas si se pueden calcular
    Sin modificar df.
    """

    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    print(f"Valores únicos: {valores_unicos}")
    print(f"Número de registros: {num_registros}")
    print(f"Valores nulos: {valores_nulos}")
    print(f"Registros duplicados: {duplicados}")
    print(f"dtype: {dtype}")
    print("------------------------")

    print("\nPorcentajes:")
    print(df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2))

    print("\nEstadísticas descriptivas:")
    print("---------------------------------")

    temp_col = pd.to_numeric(df[columna], errors='coerce')

    if temp_col.notna().sum() > 0:
        stats = temp_col.agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        print(f"Media: {stats['Mean']:.2f}")
        print(f"Mediana: {stats['Mediana']:.2f}")
        print(f"Moda: {stats['Mode']}")
    else:
        print("⚠️ La columna no es numérica o no contiene valores convertibles.")


# -------------------------------------------------------------
# FUNCIÓN 4 — transform_headtail (SAFE)  ← NUEVA
# -------------------------------------------------------------
def transform_headtail(df: pd.DataFrame, columna: str) -> None:
    """
    Analiza:
    - valores únicos, nulos, duplicados
    - top 5 y bottom 5 frecuencias
    - estadísticas numéricas si la columna puede convertirse
    NO modifica df.
    """

    # 1. Info general
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    print(f"📌 Análisis de la columna: {columna}")
    print(f"- Valores únicos: {valores_unicos}")
    print(f"- Número de registros: {num_registros}")
    print(f"- Valores nulos: {valores_nulos}")
    print(f"- Registros duplicados: {duplicados}")
    print(f"- dtype: {dtype}")
    print("---------------------------------")

    # 2. Frecuencias
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    print("🔹 Top 5 frecuencias:")
    print(frecuencias.head(5))
    print("\n🔹 Bottom 5 frecuencias:")
    print(frecuencias.tail(5))
    print("---------------------------------")

    # 3. Estadísticas numéricas (SAFE)
    temp_col = pd.to_numeric(df[columna], errors='coerce')

    if temp_col.notna().sum() > 0:
        stats = temp_col.agg({
            'Media': 'mean',
            'Mediana': 'median',
            'Moda': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        print("📊 Estadísticas numéricas:")
        print(f"- Media: {stats['Media']:.2f}")
        print(f"- Mediana: {stats['Mediana']:.2f}")
        print(f"- Moda: {stats['Moda']}")
    else:
        print("⚠️ La columna no contiene valores numéricos convertibles.")
    print("---------------------------------")
