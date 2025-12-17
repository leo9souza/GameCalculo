from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    jogo = True
    
    while jogo:
        dificuldade: str = input('Informe o nível de dificuldade desejado [Facil(1 ponto), Medio(2 pontos), Dificil(3 pontos)]: ')

        calc: Calcular = Calcular(dificuldade)

        print('Informe o resultado para a seguinte operação: ')
        calc.mostrar_operacao()

        resultado: int = int(input())

        if dificuldade == 'facil':
            if calc.checar_resultado(resultado):
                pontos = pontos + 1
                print(f'você tem {pontos} ponto(s).')
        elif dificuldade == 'medio':
            if calc.checar_resultado(resultado):
                pontos = pontos + 2
                print(f'você tem {pontos} ponto(s).')
        else:  #dificil
            if calc.checar_resultado(resultado):
                pontos = pontos + 3
                print(f'você tem {pontos} ponto(s).')

        continuar = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]: '))
        jogo = continuar == 1

    print(f'Você finalizou com {pontos} ponto(s). Até a próxima!')


if __name__ == "__main__":
    main()

