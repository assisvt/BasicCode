i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")
--

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")
--

#Cuidado com a diferença de posicionamentos da impressão (print), com um simples posicionamento:
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
    print("Done")
