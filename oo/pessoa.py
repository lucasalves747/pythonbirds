class Pessoa:
    def __init__(self, nome=None, idade= 19):
        self.idade = idade
        self.nome = nome
    def  cumprimentar (self):
        return f' ola {id(self)} '

if __name__ == '__main__':
    P = Pessoa('lucas')
    print(Pessoa.cumprimentar(P))
    print(id(P))
    print(P.cumprimentar())
    print(P.nome)
    P.nome='casa'
    print(P.nome)
    print(P.idade)
