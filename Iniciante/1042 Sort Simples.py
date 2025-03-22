# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
# Entrada

# A entrada contem três números inteiros.
# Saída

# Imprima a saída conforme foi especificado.

def seq_numeros(numeros):
    sequencia_numeros = sorted(numeros)
    for numero in sequencia_numeros:
        print(numero)
    print()
    for numero in numeros:
        print(numero)
        
numeros = list(map(int, input().split()))
seq_numeros(numeros)