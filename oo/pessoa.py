class Pessoa:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome #None para nada

    def comprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())
    print(p.nome)
    p.nome = "Renzo"
    print(p.nome)
