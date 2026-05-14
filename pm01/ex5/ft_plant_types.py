class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def set_height(self, height: float):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return
        else:
            self.height = height

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return
        else:
            self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._blooming = False

    def bloom(self):
        self._blooming = True
        print(f"[asking the {self.name} to bloom]")
        self.show()

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {(self.height):.1f}cm"
              f" long and {self.trunk_diameter:.1f}cm wide")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self, days: int, growth_rate: float):
        self.age = self.age + days
        self.nutritional_value = self.nutritional_value + days
        self.height = self.height + (days * growth_rate)
        print(f"[make {self.name} grow and age for {days} days]")
        self.show()

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types():
    print("=== Flower")
    f1 = Flower("rose", 15, 10, "red")
    f1.show()
    f1.bloom()
    print("")

    print("=== Tree")
    t1 = Tree("oak", 200, 365, 5)
    t1.show()
    t1.produce_shade()
    print("")

    print("=== Vegetable")
    v1 = Vegetable("tomato", 5, 10, "April", 0)
    v1.show()
    v1.grow(20, 2.1)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
