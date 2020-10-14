import datetime as dt

from base_class import BaseProduct

class Food(BaseProduct):
    def __init__(self, kcal: int, best_before: dt.datetime, nutritional_value: list ):
        super().__init__(name, price, quantity)
        self.kcal = kcal
        self.best_before = best_before
        self.nutritional_value = nutritional_value

x = Food("Banan", 1, 3, 3, dt.datetime.today(), ["potas"])

print(x)