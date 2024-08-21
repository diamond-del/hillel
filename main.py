class Car:
    def __init__(self, model, year, cost):
        self.model = model
        self.year = year
        self.cost = cost

    def drive(self, distance):
        depreciation = 10 * distance
        self.cost -= depreciation
        if self.cost < 0:
            self.cost = 0

    @property
    def category(self):
        if self.cost > 10_000_000:
            return "Елітне"
        elif 2_000_000 <= self.cost <= 10_000_000:
            return "Середнячок"
        else:
            return "Економ"

    def __str__(self):
        return f"Модель: {self.model}, Рік: {self.year}, Вартість: {self.cost} грн, Категорія: {self.category}"


car = Car("Tesla Model S", 2022, 12_000_000)
print(car)

car.drive(2000)
print(car)
