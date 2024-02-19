import random
import string

size = int(input('Digite o tamanho de senha que você deseja: '))
    #letras maiusculas e minusculas # digitos #simbolos
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+_,.;<>:?|/'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))