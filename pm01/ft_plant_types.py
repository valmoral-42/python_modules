class Plant:
    def __init__(self, name: str):
        self.name = name.capitalize()

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            return
        else:
            self.height = height

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            return
        else:
            self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int, shade: int):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self):
        print(f"{self.name} provides {(self.shade)} "
              "square meters of shade")

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def ft_plant_types():
    Flower1 = Flower("rose", 25, 30, "red")
    Flower2 = Flower("Sunflower", 80, 45, "yellow")
    Flower1.get_info()
    print("")
    Flower2.get_info()
    print("")

    Tree1 = Tree("oak", 500, 1825, 50, 78)
    Tree2 = Tree("pine", 220, 1000, 25, 110)
    Tree1.get_info()
    print("")
    Tree2.get_info()
    print("")

    Veg1 = Vegetable("tomato", 80, 90, "summer", "c")
    Veg2 = Vegetable("broccoli", 10, 30, "winter", "k and c")
    Veg1.get_info()
    print("")
    Veg2.get_info()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")
    ft_plant_types()
