# Jose Cabezas
import pandas as pd
#import numpy as np
"""
***********************************************
************FUNCIONALIDAD REQUERIDA****************
***********************************************
SOLO QUEDA CONVERTIR  TODOS LOS CAMPOS A INT64
"""

try:
    totalg=0
    totali=0
    totalgm=0
    totalim=0
    ahorro=0
    gastos={0:0}
    df = pd.read_csv("finanzas2020.csv", sep='\t')
    #print(df.iloc[63])
    #print(df.dtypes)

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
    df.replace(to_replace=r"'", value=" ", regex=True,inplace=True)


#convertir columnas a enteros
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

    #Reemplazar campos nan(vacios) por 0
    df=df.fillna(0)


    #df["Enero"].astype(int)
    #print(df.dtypes)
    #print(df)

    #df.replace(np.nan, 0)

    #print(df)

    #Recorremos cada columna(cada mes) con sus movimientos(gastos e ingresos)
    for mes in range(12):
        totalim=0
        totalgm=0
        ahorro=0
        #print(df.iloc[:, mes].to_dict())
        meses=df.iloc[:, mes].to_dict()
        #print("mostamos el dataFrame",meses)
    # recorremos el diccionario creado para poder manejarlo mejor
        for indice, cantidad in meses.items():
            #print(f"{indice}:{cantidad}")
    # recorremos distinguimos si el valor es negativo(gastos)o positivo(ingreso)
            if cantidad<0:
                #print(f" los valores negattivos son:{indice}:{cantidad}")
                totalg=cantidad+totalg
                totalgm=cantidad+totalgm
                #print(f"el total acumulado de gastos es{totalg},se ha sumado{cantidad}")
            else:
                totali=cantidad+totali
                totalim=cantidad+totalim
                #print(f"el total acumulado  de ingreso es{totali}")
        gastos[mes] = totalgm
        ahorro=totalim-(-totalgm)
        print(f"El mes {mes+1} se ha ingresado {totalim}")
        print(f"El mes {mes+1} se ha gastado {totalgm}")
        print(f"El mes {mes+1} se ha ahorrado {ahorro}")
        #print(f"Gastos del mes {gastos}")
        print("\n \n ")


    #Apartado 1
    #mini = df.min()
    #print("por columnas\n",mini)
    p = sorted(gastos.items(), key=lambda item: item[1])
    p=next(iter(p))
    print("El mes con mayor gasto es el mes:",p[0]+1)

    #Apartado 2
    total = df.sum()
    p2 = total.sort_values(ascending=False).to_dict()
    print("El mes con mas ahorro es:",next(iter(p2)))
    print("\n \n ")

    #Apartado 3
    media_anual=(totalg/12)
    print("La media anual de gastos es:",media_anual*(-1))
    #Apartado4
    print("El total de gastos este año ha sido",totalg*(-1))
    #Apartado5
    print("El total de ingresos este año ha sido",totali)
    #print(df.head(50))
    #print(df.tail(50))



except IOError:
    print("Fichero no valido o no existe")
