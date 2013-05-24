import os
limpiar = os.system('clear')
def main():
    #binario a decimal
    def binarioToDec(valor):
        suma = 0
        n = 0
        for x in valor:
            cuadrado = 2**n
            binario = int(x) * cuadrado
            suma = suma + binario
            n = n + 1
        print suma

    #decimal a binario
    def decimalToBin(x):
        #d = n *(-1)
        while x > 1:
            print x%2,
            x = x/2
            if x == 1:
                print x,


    print """
        Conversor Binario/Decimal, Decimal/Binario.
        1. Decimal a binario.
        2. Binario a decimal Ej: 001 --> 4.
        3. limpiar pantalla.
            """
    opcion = input('')

    if opcion == 1:
        valor = int(raw_input('valor'))
        decimalToBin(valor)
    elif opcion == 2:
        valor = raw_input('valor')
        binarioToDec(valor)
    elif opcion == 3:
        limpiar
    else:
        print 'valor incorrecto'

"""
n = 9
b = ''
while n > 0:
    b = str(n % 2) + b
    n >>= 1
print(b)
"""
"""
def decimalToBin(n):
    if n==0: return ''
    else:
        return decimalToBin(n/2) + str(n%2)
"""
