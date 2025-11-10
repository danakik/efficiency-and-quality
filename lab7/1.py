from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):

    @abstractmethod
    def calculate_cost(self, distance_km: float) -> float:
        pass


class SelfPickupStrategy(DeliveryStrategy):
    def calculate_cost(self, distance_km: float) -> float:
        return 0.0


class ExternalCourierStrategy(DeliveryStrategy):
    def calculate_cost(self, distance_km: float) -> float:
        return distance_km * 1.5


class OwnCourierStrategy(DeliveryStrategy):
    def calculate_cost(self, distance_km: float) -> float:
        return 2.5 + distance_km * 0.6


class DeliveryCostCalculator:

    def __init__(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def calculate(self, distance_km: float) -> float:
        return self.strategy.calculate_cost(distance_km)


if __name__ == "__main__":

    distance = 10

    calculator = DeliveryCostCalculator(SelfPickupStrategy())
    print("Самовивіз:", calculator.calculate(distance))

    calculator.set_strategy(ExternalCourierStrategy())
    print("Доставка зовнішньою службою:", calculator.calculate(distance))

    calculator.set_strategy(OwnCourierStrategy())
    print("Доставка власною службою:", calculator.calculate(distance))
