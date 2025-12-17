from random import randint

class Calcular:
    def __init__(self, dificuldade: str) -> None:
        self.__dificuldade: str = dificuldade.lower()
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3) #1- Somar #2- Subtrair #3- Multiplicacao
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self) -> str:
        return self.__dificuldade
    
    @property
    def valor1(self) -> int:
        return self.__valor1
    
    @property
    def valor2(self) -> int:
        return self.__valor2
    
    @property
    def operacao(self) -> int:
        return self.__operacao
    
    @property
    def resultado(self) -> int:
        return self.__resultado

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = "operação desconhecida"
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 'facil':
            return randint(0, 10)
        elif self.dificuldade == 'medio':
            return randint(0, 100)
        else:  #dificil
            return randint(0, 1000)

    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1: #somar
            return self.valor1 + self.valor2
        elif self.operacao == 2: #subtrair
            return self.valor1 - self.valor2
        else:  #multiplicar
            return self.valor1 * self.valor2

    @property 
    def _op_simbolo(self):
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'
        

    def checar_resultado(self, resposta: int) -> bool:
        check: bool = False
        if resposta == self.resultado:
            print('Resposta Correta!')
            check = True
        else:
            print('Resposta Incorreta!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return check

    def mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')