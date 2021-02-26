class Pessoa:
    def  cumprimentar (self):
        return f' ola {id(self)} '

if __name__ == '__main__':
    P = Pessoa()
    print(Pessoa.cumprimentar(P))
    print(id(P))
    print(P.cumprimentar())
