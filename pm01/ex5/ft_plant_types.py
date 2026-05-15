class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = height
        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._blooming = False

    def bloom(self) -> None:
        self._blooming = True
        print(f"[asking the {self.name} to bloom]")
        self.show()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {(self._height):.1f}"
              f"cm long and {self.trunk_diameter:.1f}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self, days: int, growth_rate: float) -> None:
        self._age = self._age + days
        self.nutritional_value = self.nutritional_value + days
        self._height = self._height + (days * growth_rate)
        print(f"[make {self.name} grow and age for {days} days]")
        self.show()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
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
