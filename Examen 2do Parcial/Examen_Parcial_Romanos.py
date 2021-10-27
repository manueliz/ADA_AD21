
#Declaramos el directorio que ocuparemos para todo el codigo
simbolos_romanos = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

#Pedimos el valor en decimal a convertir a entero
decimal=int(input('Favor de ingresar el numero en decimal para convertir en romano: '))

#Inicializamos la funcion que hara la conversion a numeros romanos
def decimal_romano(d):

    romano=''

    while d > 0:
        #Aqui hacemos un loop con for con 2 variables tanto el numero entero como el simbolo correspondiente para cada decimal
        for i,r in simbolos_romanos:
            #mientras el valor ingresado sea mayor o igual a cualquier entero de nuestro directorio el programa hara lo siguiente
            while d >= i:
                #Primero metemos el simbolo correspondiente al valor que ingresamos
                romano += r
                #Y despues restamos la entrada de nuestro programa con el valor correspondiente al simbolo que ingresamos
                d -= i
    #Por ultimo imprimimos la cadena de simbolos correspondientes al numero en romano
    print(f"El numero en romano es: {romano}")
    return romano

#Llamamos a la funcion dentro del programa principal
decimal_romano(decimal)