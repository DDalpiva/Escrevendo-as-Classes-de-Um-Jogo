class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = None

        if self.tipo == "mago":
            ataque = "Sua magia"
        elif self.tipo == "guerreiro":
            ataque = "Sua espada"
        elif self.tipo == "monge":
            ataque = "Suas artes marciais"
        elif self.tipo == "ninja":
            ataque = "Seu shuriken"
        else:
            raise ValueError("Tipo de herói inválido")

        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")




heroi_mago = Heroi("Gandalf", 1000, "mago")
heroi_mago.atacar()
