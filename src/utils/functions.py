import pandas as pd
import os
import scipy.stats as stats
import numpy as np


class color:
   """Class to define colors for markdown cells."""

   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   

def save_data(df, name):
    """Guarda el DataFrame en un archivo CSV."""
    
    os.chdir(fr"C:\Users\defco\OneDrive\Escritorio\Cursos\Programación\Cursados\Data Science Bootcamp\Spotify EDA\src\data")

    df.to_csv(f"{name}.csv", index=False)
    print(f"Datos guardados en 'data/{name}.csv\n")

    os.chdir(r"C:\Users\defco\OneDrive\Escritorio\Cursos\Programación\Cursados\Data Science Bootcamp\Spotify EDA\src")   
    print(f"Directorio actual: {os.getcwd()}")


def percent_missing(df):
    """Calcula el porcentaje de valores nulos en cada columna del DataFrame."""

    percent_nan = 100 * df.isnull().sum() / len(df)
    percent_nan = percent_nan[percent_nan > 0].sort_values(ascending=False)

    amount_nan = df.isnull().sum()
    amount_nan = amount_nan[amount_nan > 0].sort_values(ascending=False)
    
    return pd.DataFrame(zip(percent_nan, amount_nan), index=percent_nan.index, columns=['NaN %', 'NaN Amount'])


def calculate_spearman(x, y): 
    """Calcula la correlación de Spearman entre dos variables."""

    corr, p_value = stats.spearmanr(x, y)

    # Mostrar resultado
    print(f"Correlación de Spearman: {color.BLUE}{corr:.3f}{color.END}")
    print(f"Valor p: {color.BLUE}{p_value:.3f}{color.BOLD}")


def clean_release_date(date):
    """Limpia y formatea la fecha de lanzamiento."""

    if date == "0000":  # Valor inválido, lo descartamos
        return np.nan
    
    elif len(date) == 4 and date.isdigit():  # Solo año (YYYY)
        return f"{date}-01-01"
    
    elif len(date) == 7 and date[:4].isdigit() and date[5:7].isdigit():  # Año-mes (YYYY-MM)
        return f"{date}-01"
    
    return date  # Si ya está bien, lo dejamos igual


def filter_popularity(df, threshold, feature, time_counts):
    """Filtra las canciones populares y calcula el porcentaje de popularidad por mes."""
    
    # Filtrar canciones populares
    df_popular = df[df["popularity"] > threshold]

    # Contar cuántas canciones populares se lanzan cada mes
    popular_counts = df_popular.groupby(feature)["popularity"].count().reset_index()
    popular_counts.columns = [feature, "popular_songs"]

    # Contar total de canciones por mes
    total_counts = df.groupby(feature)["popularity"].count().reset_index()
    total_counts.columns = [feature, "total_songs"]

    # Unir los DataFrames
    df_summary = popular_counts.merge(total_counts, on=feature)

    # Calcular el porcentaje de canciones populares en cada mes
    df_summary["popular_percentage"] = (df_summary["popular_songs"] / df_summary["total_songs"]) * 100

    # Convertir a categoría ordenada
    df_summary[feature] = pd.Categorical(df_summary[feature], categories=time_counts.keys(), ordered=True)

    # Ordenar antes de graficar
    df_summary = df_summary.sort_values(feature)

    return df_summary