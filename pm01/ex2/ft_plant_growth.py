class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow_plant(self, growth: int):
        self.height += growth

    def age_plant(self, days: int):
        self.age += days

    def get_info(plant):
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def ft_plant_growth():
    Plant1 = Plant("Rose", 25, 30)
    Plant2 = Plant("Sunflower", 80, 45)
    Plant3 = Plant("Cactus", 15, 120)
    i = 1

    print("=== Day 1 ===")
    Plant1.get_info()
    Plant2.get_info()
    Plant3.get_info()

    while i < 7:
        Plant1.grow_plant(2)
        Plant1.age_plant(1)
        Plant2.grow_plant(1)
        Plant2.age_plant(1)
        Plant3.grow_plant(3)
        Plant3.age_plant(1)
        i += 1

    print(f"=== Day {i} ===")
    Plant1.get_info()
    print("Growth this week: 12cm")
    Plant2.get_info()
    print("Growth this week: 6cm")
    Plant3.get_info()
    print("Growth this week: 18cm")


if __name__ == "__main__":
    ft_plant_growth()
