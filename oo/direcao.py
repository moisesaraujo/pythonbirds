class Direcao:
    dir ="Norte"

    def direcao(self):
        dic = {"N": "Norte", "O": "Oeste", "S": "Sul", "L": "Leste"}
        for dir in dic.values():
            print(dir)

    def girar_a_direita(cls):

            if cls.dir == "Norte":
                cls.dir="Leste"
            elif cls.dir == "Leste":
                cls.dir="Sul"
            elif cls.dir == "Sul":
                cls.dir="Oeste"
            elif cls.dir == "Oeste":
                cls.dir="Norte"
           # return self.dir

    def girar_a_esquerda(cls):

        if cls.dir == "Norte":
            cls.dir = "Oeste"
        elif cls.dir == "Oeste":
            cls.dir = "Sul"
        elif cls.dir == "Sul":
            cls.dir = "Leste"
        elif cls.dir == "Leste":
            cls.dir = "Norte"
        #return self.dir

    def valor(cls):
        return cls.dir