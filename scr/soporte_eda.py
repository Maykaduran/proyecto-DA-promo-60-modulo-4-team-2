import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import shapiro, kstest

pd.set_option('display.max_columns', None)

import warnings
warnings.filterwarnings("ignore")

# BASIC DATA - INITIAL REVIEW
def resumen_df(df):
    print("\nForma del DataFrame:", df.shape)

    print("\nTipos de datos:")
    print(df.dtypes)

    print("\nValores nulos:")
    print(df.isnull().sum())

    print("\nValores duplicados:", df.duplicated().sum())

    # Variables numéricas
    num_cols = df.select_dtypes(include=np.number)
    if not num_cols.empty:
        print("\nResumen estadístico (numéricas):")
        display(num_cols.describe().T)
    else:
        print("\n⚠️ No hay columnas numéricas en el DataFrame.")

    # Variables categóricas
    cat_cols = df.select_dtypes(include='object')
    if not cat_cols.empty:
        print("\nResumen estadístico (categóricas):")
        display(cat_cols.describe().T)
    else:
        print("\n⚠️ No hay columnas categóricas en el DataFrame.")
