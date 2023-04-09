########################## if statement ##########################
''' Permite-nos que construamos programas que consigam fazer decisões baseadas em condições. O if statement pode ter um else. 
O elif representa outros ifs que meu código pode ter'''

is_hot = True # Boolan value verdadeira de uma variável
if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
print("Enjoy your day")
# Vai imprimir os 2 primeiros prints
--

is_hot = False
if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
print("Enjoy your day")
# Vai imprimir apenas Enjoy your day
--

is_hot = False # Posso mudar o boolean valu de is_hot ou is_cold e obter diferentes retornos de acordo com as condições criadas 
is_cold = True
if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
elif is_cold: ##if statements podem ter um elif associado
    print("It's a cold day")
    print("Wear warm clothes")
else: ##if statements podem ter um else associado
    print("It's a lovely day")

print("Enjoy your day")
--

'''Uma pessoa precisa comprar uma casa no valor de 1 milhão de dolares, se ela tiver um bom crédito
 o pagemento inicial devera ser 10% do preço, se não, 20% '''
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')
