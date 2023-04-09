############# upper ou lower case ###########
course = 'Python for Begginers'
print(course.upper()) # Imprime toda a string em upper case
--

########### Find Method #################
# Ex1
course = 'Python for Begginers'
print(course.find('P')) # Imprime a posição em que o "P" se encontra, 0.

#Ex2
course = 'Python for Begginers'
print(course.find('Begginers'))
# 11 (print)
# Temos 11 porque a palavra Beggienrs começa no index 11.
--

########### Replace Method ############
# Substituindo um palavra da string por outra.
course = 'Python for Begginers'
print(course.replace('Begginers', 'Absolute Begginers'))

# Podemos substituir uma letra por outra.
course = 'Python for Begginers'
print(course.replace('P', 'V'))
--

################### Boolean expressions - in operator ‘   ’ in variable ####################
course = 'Python for Begginers'
print('Python' in course)
# True, Python in course
-----
course = 'Python for Begginers'
print('python' in course)
# False python in lower case não estpa in course. Python is sensitive with upper and lower case.
