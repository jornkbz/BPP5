#JOSE CABEZAS
"""
2. Haga uso de la función filter para construir un programa que,
 dado una lista de n números devuelva aquellos que son primos.
  Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa
   que implemente debe devolver como resultado [3, 5, 5, 13]

import pdb
pdb.set_trace()

"""
#filter
#filter(una_funcion, una_lista) 
listado=[3, 4, 8, 5, 5, 22, 13]
primo2=list(filter(lambda n:all(n % m != 0 for m in range(2, n)), listado))
print(primo2)