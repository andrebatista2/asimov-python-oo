class Animal:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def walk(self) -> None:
        print(f"{self.name} walks, and look! He's {self.color}")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping!")

    def jump(self) -> None:
        print(f"{self.name} is jumping high!")


class Peacock(Animal):
    def __init__(self, name: str, color: str, feather_color: str, stats: dict):
        super().__init__(name, color)
        self.feather_color = feather_color
        self.stats = stats

    def fly(self) -> None:
        print(f"{self.name} is flying! Look at his feathers! It's {self.feather_color}")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping too much!")


# @property - getters
# @type.setter - setters
class Pessoa(object):
    def __init__(self, nome, idade, salario):
        self._nome = nome
        self._idade = idade
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario



# Sim, pessoal. É só isso :)
# Herança, polimorfismo e abstração
cockatoo = Peacock("Jack", "blue", "white", {'hungry': 2, 'gender': 'male'})
cockatoo.name = "Will"
cockatoo.fly()
cockatoo.sleep()
cockatoo.jump()
cockatoo.walk()

# É isso. Não vejo vantagens em usar encapsulamento em Python
lucas = Pessoa("André", 31, 3450)
lucas.salario = 6500  # setter
print(lucas.salario)  # getter