class Pessoa:
    def __init__(self, idade, *filhos, nome = None):
        self.idade = idade
        self.nome = nome #None para nada
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(15, nome = 'Luciano' )
    renzo = Pessoa(35, luciano, nome = 'Renzo')
    print(renzo.idade)
    print(renzo.filhos)
    for filho in renzo.filhos: print(filho.nome)

