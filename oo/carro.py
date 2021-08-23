"""
Você deve criar uma classe carro que vai possuir dois atributos compostos
por outras duas classes:

1) Motor
2) Direção

1- Motor controla-rá a velocidade:
Atributos:
a) velocidade
b) metodo acelerar, que acrementa a velocidade
c) metodo frear, diminuindo a velocidade

A Direção terá a Responsa de controlar a direção
1) Valor de direção com: Norte, Sul, Leste, Oeste
2) Metodo Virar a direita:
  N
O   L
  S
3) Metodo Virar a esquerda

    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade()
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade == 0: return
        self.velocidade -= 1

class Direcao:
    array_direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']

    def __init__(self):
        self.valor = self.array_direcoes[0]

    def girar_a_direita(self):
        indice_valor = self.array_direcoes.index(self.valor)
        if self.valor == self.array_direcoes[-1]: self.valor = self.array_direcoes[0]
        else: self.valor = self.array_direcoes[indice_valor + 1]

    def girar_a_esquerda(self):
        indice_valor = self.array_direcoes.index(self.valor)
        if self.valor == self.array_direcoes[0]: self.valor = self.array_direcoes[-1]
        else: self.valor = self.array_direcoes[indice_valor - 1]

class Carro:
    def __init__(self, direcao: object, motor: object):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def calcular_direcao(self):
        print(self.direcao.valor)

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()



if __name__ == '__main__':
    #Encontrando o indice
    lista = ['banana', 'maçã', 'mamão']
    print(lista.index('maçã'))