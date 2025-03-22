# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.
# Entrada

# Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.
# Saída

# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)

# Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

def main():

    dia_inicio = int(input().split()[1])
    hora_inicio = list(map(int, input().split(' : ')))
    
    dia_fim = int(input().split()[1])
    hora_fim = list(map(int, input().split(' : ')))
    
    duracao = [0, 0, 0, 0]
    duracao[3] = hora_fim[2] - hora_inicio[2]
    if duracao[3] < 0:
        duracao[3] += 60
        hora_fim[1] -= 1
    duracao[2] = hora_fim[1] - hora_inicio[1]
    if duracao[2] < 0:
        duracao[2] += 60
        hora_fim[0] -= 1
    duracao[1] = hora_fim[0] - hora_inicio[0]
    if duracao[1] < 0:
        duracao[1] += 24
        dia_fim -= 1
    duracao[0] = dia_fim - dia_inicio
    
    print(f'{duracao[0]} dia(s)')
    print(f'{duracao[1]} hora(s)')
    print(f'{duracao[2]} minuto(s)')
    print(f'{duracao[3]} segundo(s)')

main()