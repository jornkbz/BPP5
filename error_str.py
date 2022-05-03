# Jose Cabezas
import pandas as pd
"""
***********************************************
************FUNCIONALIDAD REQUERIDA****************
***********************************************
SOLO QUEDA CONVERTIR  TODOS LOS CAMPOS A INT64
"""

try:
    df = pd.read_csv("errores_str.csv", sep='\t')
    #print(df.iloc[63])
    print(df.dtypes)

    #print(df)
#   comprobar si el fichero tiene 12 columnas
    columnas = df.shape
    #print(f"El fichero tiene: {columnas[1]} columnas")
    assert(columnas[1] == 12)

    #comprobar si hay algún valor vacio
    compr=df.notnull().all()
    #print(compr)
    compr1=False in compr.values
    #print(compr1)
    assert(compr1!=True)

    #Reemplazo de  valores con '(string) para poder pasarlos a int
    df.replace(to_replace=r"'", value="", regex=True,inplace=True)
    #Reemplazar campos nan(vacios) por 0
    df.fillna(0)
    #df["Enero"].astype(int64)
    df.Enero=pd.to_numeric(df.Enero, errors='coerce')
    df.Febrero=pd.to_numeric(df.Febrero, errors='coerce')
    df.Marzo=pd.to_numeric(df.Marzo, errors='coerce')
    df.Abril=pd.to_numeric(df.Abril, errors='coerce')
    df.Mayo=pd.to_numeric(df.Mayo, errors='coerce')
    df.Junio=pd.to_numeric(df.Junio, errors='coerce')
    df.Julio=pd.to_numeric(df.Julio, errors='coerce')
    df.Agosto=pd.to_numeric(df.Agosto, errors='coerce')
    df.Septiembre=pd.to_numeric(df.Septiembre, errors='coerce')
    df.Octubre=pd.to_numeric(df.Octubre, errors='coerce')
    df.Noviembre=pd.to_numeric(df.Noviembre, errors='coerce')
    df.Diciembre=pd.to_numeric(df.Diciembre, errors='coerce')


    print(f"\nFinal \n{df.dtypes}")
    print(f"Final \n{df}")
except IOError:
    print("Fichero no valido o no existe")
#pruebae444ASDasd