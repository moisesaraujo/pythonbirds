class Pessoa:
    def __init__(self,*filhos, nome=None, idade=48):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cuplimentar(self):
        return f'Ola!'

if __name__ == "__main__":
    p = Pessoa()
    p.nome="moises"
    miria = Pessoa(nome="Miria")
    larissa = Pessoa(nome="Larissa")
    moises = Pessoa(miria,larissa,nome="Moises")

    #moises = Pessoa(larissa,nome="Larissa")
    p.idade==49
    print(p.cuplimentar())
    print(f"nome {p.nome}, idade {p.idade}")

    for filho in moises.filhos:
        print(filho.nome)

