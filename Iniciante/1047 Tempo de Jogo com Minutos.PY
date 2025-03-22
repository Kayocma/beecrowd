# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
# Entrada

# Quatro números inteiros representando a hora de início e fim do jogo.
# Saída

# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

def main():
    hi, mi, hf, mf = map(int, input().split())

    duracao_h = hf - hi
    duracao_m = mf - mi

    if duracao_m < 0:
        duracao_m += 60
        duracao_h -= 1

    if duracao_h < 0:
        duracao_h += 24

    if hi == hf and mi == mf:
        duracao_h = 24
        duracao_m = 0

    print(f'O JOGO DUROU {duracao_h} HORA(S) E {duracao_m} MINUTO(S)')

if __name__ == '__main__':
    main()