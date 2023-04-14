"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    # Se lee la DB
    df = pd.read_csv("solicitudes_credito.csv", sep=";").drop(columns=['Unnamed: 0'])

    # Se eliminan nulos y duplicados
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # Todos los valores se estandarizan en minuscura para sexo y tipo_de_emprendimiento
    df["sexo"] = df["sexo"].apply(lambda x: x.lower())
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x: str(x).lower())

    # Se reemplazan valores claves para las columnas
    df["idea_negocio"] = df["idea_negocio"].replace("-"," ", regex=True).str.replace("_"," ", regex=True).apply(lambda x: x.lower())
    df["barrio"] = df["barrio"].str.replace("_","-", regex=True).str.replace("-"," ", regex=True).str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("-"," ").str.replace("_"," ").str.lower()
    df['monto_del_credito'] = df['monto_del_credito'].str.strip('$ ').replace({'$ ':''}, regex=True).replace({',':''}, regex=True).astype(float).astype(int)

    # Se ubica el dia como primer valor para la columna 
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)

    df = df.drop_duplicates().dropna()

    return df
