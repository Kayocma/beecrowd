# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.
# Entrada

# A entrada será um valor inteiro positivo.
# Saída

# A saída será uma sequência de seis números ímpares.

x = int(input())

for i in range (x, x + 12):
    if i % 2 != 0:
        print(i)