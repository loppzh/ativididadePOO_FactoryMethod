from abc import ABC, abstractmethod

# --- Interface do Produto ---
class MotorVehicle(ABC):
    """
    A interface do Produto (MotorVehicle).
    Define a operação que todos os veículos devem implementar.
    """
    @abstractmethod
    def build(self):
        pass

# --- Produtos Concretos ---
class Car(MotorVehicle):
    """
    Produto concreto Carro (Car).
    """
    def build(self):
        print("Construindo Carro...")

class Motorcycle(MotorVehicle):
    """
    Produto concreto Motocicleta (Motorcycle).
    """
    def build(self):
        print("Construindo Moto...")

# --- Criador Abstrato ---
class MotorVehicleFactory(ABC):
    """
    A classe abstrata da Fábrica (Creator).
    Declara o factory method que retorna um objeto do tipo MotorVehicle.
    """
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle:
        pass

    def create(self) -> MotorVehicle:
        """
        O método principal da fábrica. Note que ele retorna o tipo abstrato MotorVehicle.
        Isso permite que o código cliente funcione com qualquer subclasse de fábrica.
        """
        return self.create_motor_vehicle()

# --- Criadores Concretos ---
class CarFactory(MotorVehicleFactory):
    """
    Fábrica concreta para criar Carros (CarFactory).
    """
    def create_motor_vehicle(self) -> MotorVehicle:
        return Car()

class MotorcycleFactory(MotorVehicleFactory):
    """
    Fábrica concreta para criar Motos (MotorcycleFactory).
    """
    def create_motor_vehicle(self) -> MotorVehicle:
        return Motorcycle()

# --- Exemplo de Uso ---
if __name__ == "__main__":
    car_factory = CarFactory()
    car = car_factory.create()
    car.build()

    motorcycle_factory = MotorcycleFactory()
    motorcycle = motorcycle_factory.create()
    motorcycle.build()