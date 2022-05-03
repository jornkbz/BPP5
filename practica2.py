#simulacion de creacion cuenta usuario
#Jose Cabezas Pulgarin
try:

    print("Bienvenido")
    def cemail(e):
        """Función que procesa el correo para comprobar que sea una dirección email valida(contenga @)
        y además que controle que se le ha pasado un parámetro.

        :param e: este es el parámetro a comprobar.
        :type e: class:`str`
        :param arr: a esta variable asignamos el caracter a comprobar .
        :type arr: class:`str`
        :param correct: con esta variable booleana controlamos que  el parámetro e contiene @.
        :type correct: class:`bool`
        :assert: comprobar que se ha introducido parámetro
        :return: devuelve  un valor booleano según el dato proporcionado
        """
        assert(len(e)!=0)
            #Debemos comprobar que sea una dirección valida(contiene @)
        arr="@"
        correct=False
        for i in (e):
            if i==arr:
                correct=True


            #print(f"variables,{i},{e},{arr},{correct}")
        if correct:
            print(f"La dirección de correo es correcta")
            return True
        else:
            print(f"La dirección de correo debe contener @")
            return False



    def cnombre(n):
        """Función que procesa el nombre introducido y compruebe de que no está vacío y 
        que tenga 4 carácteres.

        :param n: este es el parametro a comprobar.
        :type n: class:`str`
        :assert: longitud de parámetro n debe ser 4
        :return: devuelve la longitud de la variable n(nombre introducido).
        """
        #    for i in leng(n):
        assert(len(n)!=0)
        if len(n)<4:
            print(f"Nombre Usuario no Valido,debe contener más de 4 dígitos")
            return len(n)
        else:
            print(f"Nombre Usuario correcto")
            return len(n)

    def cedad(a):
        """Función que procesa el el año introducido para comprobar si es mayor de edad. Controla 
        que se le pasen parámetros y que sean de tipo int.

        :param a: este es el parámetro a comprobar.
        :type a: class:`str`
        :param diff: con esta variable calculamos la edad.
        :type dif: class:`str`
        :param sta: con esta variable forzamos que el tipo de parametro "a" sea str.
        :type correct: class:`str`
        :raises TypeError: El valor introducido debe ser del tipo int.
        :assert: comprobar que se ha introducido parámetro.
        :return: devuelve la variable dif que contiene la edad calculada.
        """
        #comp=str(a)
        a=str(a)
        assert(len(a)!=0)
        a=int(a)
        if type(a) != int:
            raise TypeError("El valor introducido debe ser del tipo int")

        dif = 2022-a
        sta = str(a)
        print(len(sta))
        if len(sta)==4:
            print(f"Perfecto,ha introducido correctamente el año de nacimiento,")
            if dif < 18:
                print("No se ha podido crear cuenta, no eres mayor de 18")

            else:
                print("Cumples el requisito de edad")

        else:
            print(f"Error el año debe contener 4 digitos")
        return dif

    p1=0
    """
    :param p1: parámetro utilizado en funcion cmulti.
    :type p1: class:`int`
    """
    p2=0
    """
    :param p1: parámetro utilizado en funcion cmulti.
    :type p1: class:`int`
    """
    def cmulti(p1,p2):
        """Funcion que procesa dos parámetros para realizar una multiplicación y además controla
        que se le pasen valores.

        :param p1: este es el primer parámetro a operar.
        :type p1: class:`int`
        :param p2: este es el seegundo parámetro a operar.
        :type p2: class:`int`
        :param resultado: este parámetro contiene la operacion utilizando p1 y p2.
        :type resultado: class:`str`
        :assert: comprobar que se ha introducido parámetro.
        :return: devuelve la variable resultado.
        """
        p1=str(p1)
        p2=str(p2)
        assert(len(p1)!=0)
        assert(len(p2)!=0)
        p1=int(p1)
        p2=int(p2)
        resultado=p1*p2
        print(f"El resultado de multiplicar {p1} por {p2} es {resultado}")
        return resultado

    e=input("Por favor, introduzca su correo electrónico: ")
    n=input("Por favor, introduzca su nombre de usuario: ")
    a=input("Por favor introduce tu año de nacimiento con 4 digitos")
    print("Por favor introduce los dos números con los que realizar la multiplicación")
    p1=input("Introduce el primer número")
    p2=input("Introduce el el segundo número")

    cemail(e)
    cnombre(n)
    cedad(a)
    cmulti(p1, p2)


except:
    print("Ha ocurrido un error")
