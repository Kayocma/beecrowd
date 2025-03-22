# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
# Entrada

# A entrada contém valores inteiros.
# Saída

# A saída deve conter uma das mensagens conforme descrito acima.

n1, n2 = input().split()

n1 = int(n1)
n2 = int(n2)

if n1 % n2 == 0 or n2 % n1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')