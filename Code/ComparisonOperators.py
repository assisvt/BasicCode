temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
--

name = "J"
##print(len(name))
##RP
#1
if len(name)  < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
--

#Função que calcula o enésimo número de Fibonacci
def Fibonacci(n):
    if n < 0:
        print("Entrada inválida")
        # O primeiro número de Fibonacci é Ø
    elif n == 1:
        return 0
    # O segundo número de Fibonacci é 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

if __name__ == "__main__":

    print(Fibonacci(9))
