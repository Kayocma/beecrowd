# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
# Entrada

# O arquivo de entrada contém um valor inteiro N.
# Saída

# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos.

N = int(input())

horas = N // 3600
N %= 3600

minutos = N // 60
N %= 60

segundos = N

print(f'{horas}:{minutos}:{segundos}')