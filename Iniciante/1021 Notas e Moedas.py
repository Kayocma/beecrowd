# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
# Entrada

# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
# Saída

# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

N = float(input())

N = int(N * 100)

print('NOTAS:')
print(f'{N // 10000} nota(s) de R$ 100.00')
N %= 10000

print(f'{N // 5000} nota(s) de R$ 50.00')
N %= 5000

print(f'{N // 2000} nota(s) de R$ 20.00')
N %= 2000

print(f'{N // 1000} nota(s) de R$ 10.00')
N %= 1000

print(f'{N // 500} nota(s) de R$ 5.00')
N %= 500

print(f'{N // 200} nota(s) de R$ 2.00')
N %= 200

print('MOEDAS:')
print(f'{N // 100} moeda(s) de R$ 1.00')
N %= 100

print(f'{N // 50} moeda(s) de R$ 0.50')
N %= 50

print(f'{N // 25} moeda(s) de R$ 0.25')
N %= 25

print(f'{N // 10} moeda(s) de R$ 0.10')
N %= 10

print(f'{N // 5} moeda(s) de R$ 0.05')
N %= 5

print(f'{N // 1} moeda(s) de R$ 0.01')