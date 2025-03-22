# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
# Entrada

# Seis valores, negativos e/ou positivos.
# Saída

# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

positivo = 0

for i in range(6):
    if float(input()) > 0:
        positivo += 1
        
print(f'{positivo} valores positivos')