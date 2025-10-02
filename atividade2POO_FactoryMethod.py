from abc import ABC, abstractmethod

class Armchair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def place_coffee(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class ModernArmchair(Armchair):
    def sit_on(self):
        print("Sentando em uma poltrona moderna.")

class ModernCoffeeTable(CoffeeTable):
    def place_coffee(self):
        print("Colocando café em uma mesa de centro moderna.")

class ModernSofa(Sofa):
    def lie_on(self):
        print("Deitando em um sofá moderno.")

class RetroArmchair(Armchair):
    def sit_on(self):
        print("Sentando em uma poltrona retrô.")

class RetroCoffeeTable(CoffeeTable):
    def place_coffee(self):
        print("Colocando café em uma mesa de centro retrô.")

class RetroSofa(Sofa):
    def lie_on(self):
        print("Deitando em um sofá retrô.")


class FurnitureFactory(ABC):
    """
    A interface da Fábrica Abstrata (Creator).
    Define os métodos de fábrica para criar cada tipo de móvel de uma família.
    """
    @abstractmethod
    def make_armchair(self) -> Armchair:
        pass

    @abstractmethod
    def make_coffee_table(self) -> CoffeeTable:
        pass

    @abstractmethod
    def make_sofa(self) -> Sofa:
        pass

class RetroFurnitureFactory(FurnitureFactory):
    """
    Fábrica concreta para a família de móveis Retrô.
    """
    def make_armchair(self) -> Armchair:
        return RetroArmchair()

    def make_coffee_table(self) -> CoffeeTable:
        return RetroCoffeeTable()

    def make_sofa(self) -> Sofa:
        return RetroSofa()

class ModernFurnitureFactory(FurnitureFactory):
    """
    Fábrica concreta para a família de móveis Modernos.
    """
    def make_armchair(self) -> Armchair:
        return ModernArmchair()

    def make_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

    def make_sofa(self) -> Sofa:
        return ModernSofa()


def client_code(factory: FurnitureFactory):
    """
    O código cliente funciona com fábricas e produtos de uma única família
    sem saber as suas classes concretas.
    """
    armchair = factory.make_armchair()
    coffee_table = factory.make_coffee_table()
    sofa = factory.make_sofa()

    armchair.sit_on()
    coffee_table.place_coffee()
    sofa.lie_on()


if __name__ == "__main__":
    print("Criando móveis retrô:")
    client_code(RetroFurnitureFactory())

    print("\nCriando móveis modernos:")
    client_code(ModernFurnitureFactory())