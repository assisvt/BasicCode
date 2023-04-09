########### SOMA ###################
print(5 + 3)
--

############# SUBTRAÇÃO ###############
print(5 - 3)
--

############## Divisão ##############
print(10 / 3) # aparecerá o float 3.3333333333333335
--

print(10 // 3) ##Se usar duas barrar obtém-se a aproximação.
-- 

print(10 % 3) # Ao usar % (porcentagem), ao rodar o programa, será mostrado o resto da divisão
--

################ EXPOENTE ################
print(10 ** 3) # 1000, 10 ao cubo
--

print('Digite o valor do raio para calcular o volume da esfera')
import math # Importa o módulo de matemática para usarmos "math.pi = valor de pi"
raio = float(input('Digite o valor do raio: '))
r3 = pow(raio, 3) # Raio elevado ao cubo
volume = 4 * math.pi * r3/3
print(f'O volume da esfera, de raio {raio}, é', volume)
--
print('Digite o valor do raio para calcular o volume da esfera')
import math # Importa o módulo de matemática para usarmos "math.pi = valor de pi"
raio = float(input('Digite o valor do raio: '))
volume = 4 * math.pi * raio**3/3
print(f'O volume da esfera, de raio {raio}, é', volume)
