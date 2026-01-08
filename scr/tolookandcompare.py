import pandas as pd

def to_doc_info(df: pd.DataFrame, columna: str) -> str:

    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    frecuencias = "\n".join([f"||{idx}  {val}" for idx, val in df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2).items()])

    try:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        stats = df[columna].agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None})
        
        mean, median, mode = stats['Mean'], stats['Median'], stats['Mode']
    except:
        mean, median, mode = "N/A (no numérico)", "N/A (no numérico)", "N/A (no numérico)"

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
    print(f'{reporte}')


def to_doc_headtail(df: pd.DataFrame, columna: str) -> str:

    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    top5 = "\n".join([f"||{idx}  {val}%" for idx, val in frecuencias.head(5).items()])
    bottom5 = "\n".join([f"||{idx}  {val}%" for idx, val in frecuencias.tail(5).items()])

    try:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        stats = df[columna].agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        mean, median, mode = stats['Mean'], stats['Median'], stats['Mode']
    except:
        mean, median, mode = "N/A (no numérico)", "N/A (no numérico)", "N/A (no numérico)"

    reporte = f"""
|    dtype: {dtype}  |   {columna}   |
|-----------|---------------|
||
||**Top 5:**
{top5}
||**Bottom 5:**
||<br>
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
    print(f'{reporte}')

def transform_info(df: pd.DataFrame, columna: str) -> None:
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    print(f"Valores únicos: {valores_unicos}\nNúmero de registros: {num_registros}\nValores nulos: {valores_nulos}\nRegistros duplicados: {duplicados}\ndtype: {dtype}")
    print('----------------')
    print("\nPorcentajes:")
    print(df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2).sort_values(ascending=False))
    print("\nEstadísticas descriptivas")
    print("---------------------------------")
    try:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        stats = df[columna].agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        print(f"Media: {stats['Mean']:.2f}")
        print(f"Mediana: {stats['Median']:.2f}")
        print(f"Moda: {stats['Mode']}")
    except Exception as e:
        print(f"No hay estadísticas descriptivas para ti en esta la columna '{columna}': {str(e)}")
        print("La columna no es numérica o contiene valores no convertibles, chata.")

def transform_headtail(df: pd.DataFrame, columna: str) -> None:
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    print(f"Valores únicos: {valores_unicos}\nNúmero de registros: {num_registros}\nValores nulos: {valores_nulos}\nRegistros duplicados: {duplicados}\ndtype: {dtype}")
    print('---------------------------------')
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    print(frecuencias.head(5))
    print(frecuencias.tail(5))
    print("---------------------------------")
    try:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        stats = df[columna].agg({
            'Mean': 'mean',
            'Median': 'median',
            'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
        })
        print(f"Media: {stats['Mean']:.2f}")
        print(f"Mediana: {stats['Median']:.2f}")
        print(f"Moda: {stats['Mode']}")
    except Exception as e:
        print(f"Lo que buscas 404 not found in '{columna}': {str(e)}")
        print("La columna no es numérica o contiene valores no convertibles, Mari Loli.")
