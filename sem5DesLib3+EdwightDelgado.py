#coding:utf-8
"""
Ejercicio 5.3.
Nos piden que escribamos una función que le pida al usuario que ingrese un
número positivo. Si el usuario ingresa cualquier cosa que no sea lo
pedido se le debe informar de su error mediante un mensaje y volverle
a pedir el número.
Resolver este problema usando
1. Ciclo interactivo.
2. Ciclo con centinela.
3. Ciclo “infinito” que se rompe.
¿Tendría sentido hacerlo con ciclo definido? Justificar.
"""
import os
def limpiar(os):
    so = os.name
    if so == "posix":
        comando = "clear"
    elif so == "nt":
        comando = "cls"
    return os.system( comando )

def main():
    while True:
        def Ciclo_infinito():
            c = 0
            while True:
                n = input('ingrese un numero positivo: ')
                if n > 0:
                    print 'valor correcto'
                    break
                else:
                    c = c + 1
                    print 'valor invalido, %d fallidos' %c


        def Ciclo_centinela():
            n = input('ingrese un numero positivo o "s" para salir: ')
            c = 0
            while n <> "s":
                if n > 0:
                    print 'valor correcto'
                else:
                    c = c + 1
                    print 'valor invalido, %d fallidos' %c
                n = input('ingrese un numero positivo o "s" para salir: ')

        def Ciclo_interactivo():
            c = 0
            n = "si"
            while n == "si":
                x = input('ingrese un numero positivo: ')
                if x > 0:
                    print 'valor correcto'
                else:
                    c = c + 1
                    print 'valor invalido, %d fallidos' %c
                n = raw_input('quiere seguir <si-no>: ')


        print """
        1. Ciclo interactivo.
        2. Ciclo con centinela.
        3. Ciclo “infinito” que se rompe.
        4. ciclo definido.
        5. Limpiar.
        6. Salir
        """
        x = input('')
        if x == 1:
            Ciclo_interactivo()
        if x == 2:
            Ciclo_centinela()
        if x == 3:
            Ciclo_infinito()
        if x == 4:
            print """
        No tiene sentido usar un ciclo definido. debido a
        que no se conoce cuantos numeros o valores seran
        introducido o la duracion de una actividad en el caso
        de que se este trabajando con tiempo de forma anticipada.
        """
        if x == 5:
            limpiar(os)
        if x == 6:
            break

