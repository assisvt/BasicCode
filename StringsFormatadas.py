##Writes John [Smith] is a coder
first = 'john'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
##Para fazer uma string formatada usa-se o prefixo: f|usamos essa formatação para ler mais fácil o código criado
msg = f'{first} [{last}] is a coder'
print(msg)
--
# CALCULE O TOTAL COST DE TODOS OS ITENS DE UMA SHOPPING CART
prices = [10, 20, 30]

total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")
