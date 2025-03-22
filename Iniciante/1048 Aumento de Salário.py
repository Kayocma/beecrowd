# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

# Salário 	Percentual de Reajuste

# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00
	

# 15%
# 12%
# 10%
# 7%
# 4%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
# Entrada

# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
# Saída

# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

n = float(input())

if n >= 0 and n <= 400.00:
    percentual = 0.15
elif n > 400.00 and n <= 800.00:
    percentual = 0.12
elif n > 800.00 and n <= 1200.00:
    percentual = 0.10
elif n > 1200.00 and n <= 2000.00:
    percentual = 0.07
else:
    percentual = 0.04
ajuste = n * percentual
print(f'Novo salario: {n + ajuste:.2f}')
print(f'Reajuste ganho: {ajuste:.2f}')
print(f'Em percentual: {int(percentual * 100)} %')