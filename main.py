class Condition:

    def __init__(self, num1=0, num2=0):
        self.number1 = num1
        self.number2 = num2
        # number = num1 + num2
        self.number3 = num1
    
    def useIf(self):
        if self.number1 == self.number2:
            print("~ El numero 1 '{}' es igual al numero 2 '{}'.".format(self.number1, self.number2))
        elif self.number1 == self.number3:
            print("~ El numero 1 '{}' es igual al numero 3 '{}'.".format(self.number1, self.number3))
        else:
            print("~ Números no iguales.")


# condition1 = Condition()
# print(condition1.num1)
# print(condition1.num2)

# condition2 = Condition(90, 90)
# condition2.useIf()
# print("~ '" + str(condition2.number1) + "'")


class Cicle:
    def __init__(self, num1=5):
        self.number = num1

    def useWhile(self):
        car = input("~ Ingrese una vocal: ").lower()
        while car not in ("a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"):
            car = input(" ! Vuelva a ingresar una vocal: ").lower()
        print('~ Felicidades, el caracter ({}) si es una vocal.'.format(car))


ciclo = Cicle()
ciclo.useWhile()
