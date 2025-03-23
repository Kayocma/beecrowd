# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
# Entrada

# O arquivo de entrada contém dois valores inteiros.
# Saída

# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

x = int(input())
y = int(input())

if x > y:
    x, y = y, x
    
soma = 0

for i in range (x + 1, y):
    if i % 2 != 0:
        soma += i
    
print(soma)