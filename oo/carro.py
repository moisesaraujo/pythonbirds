class Carro:
    repido = 1
    parar  = 2

    @classmethod

    def motor(self):
       return  f"velocidade -"

    def direcao(self): # move a direção
        pass

    def velocidade(cls): # acelera o carro
        cls.repido+=1
        return f"Velocidade atual: {cls.repido}"

    def frear(cls): # freia o carro
        status = ""
        nova_velocidade=0
        cls.repido = cls.repido - cls.parar
        status == cls.repido
        if cls.repido <= 0:
            status = "Carro parado"
        else:
            status = f"Velocidade reduzida para: {cls.repido}"
        return status

    def direcao(self):
        direcao = dict["N":"Norte","O":"Oeste","S":"Sul", "L":"Leste"]
        for dir in direcao:
            if dir("N"):
                return "Norte"
            elif dir("O"):
                return "Oeste"
            


    def girar_a_direita(self,direita=None):
        self.direita=direita
        return self.direita

    def girar_a_esquerda(esquerda=None):
        pass


if __name__ == "__main__":
            motor = Carro()
            #direcao = Carro(motor,direita="N")

            print(motor.velocidade()) #1
            print(motor.velocidade()) #2
            print(motor.frear())
            print(motor.frear())
            print(motor.girar_a_direita("N"))


