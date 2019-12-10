class Pessoa:
    def __init__(self, nome=None, idade=48):
        self.nome=nome
        self.idade=idade

    def cuplimentar(self):
        return f'Ola!'

if __name__ == "__main__":
    p = Pessoa()
    p.nome="moises"
    p.idade==49
    print(p.cuplimentar())
    print(f"nome {p.nome}, idade {p.idade}")

