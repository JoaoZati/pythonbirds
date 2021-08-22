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
    renzo.sobrenome = 'Nuccitelli'
    print(renzo.sobrenome)
    del renzo.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)

