class Pessoa:
    olhos = 2

    def __init__(self, idade, *filhos, nome = None):
        self.idade = idade
        self.nome = nome #None para nada
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        print('Metodo Estátio')

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'a classe {cls} possui {cls.olhos} olhos'

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
    print(Pessoa.olhos)
    print(renzo.olhos)
    luciano.olhos = 1
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    Pessoa.olhos = 3
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos, luciano.olhos, renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

