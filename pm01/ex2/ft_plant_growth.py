class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def grow_plant(self):
        self.height += self.growth_rate

    def age_plant(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

def ft_garden_data():
        p1 = Plant("Rose", 25.0, 30, 0.8)
        garden = [p1]
        i = 1

        for plant in garden:
            plant.show()
            while (i <= 7):
                 print(f"=== Day {i} ===")
                 plant.grow_plant()
                 plant.age_plant()
                 plant.show()
                 i += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_garden_data()
