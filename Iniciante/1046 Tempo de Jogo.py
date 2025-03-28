# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
# Entrada

# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
# Saída

# Apresente a duração do jogo conforme exemplo abaixo.

def main():
    inicio, fim = map(int, input().split())
    
    if inicio < fim:
        duracao = fim - inicio
    else:
        duracao = 24 - inicio + fim
        
    print(f'O JOGO DUROU {duracao} HORA(S)')

if __name__ == '__main__':
    main()