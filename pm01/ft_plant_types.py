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


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {(self.height*0.156)} square meters of shade")

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.harvest_season = harvest_season

    def nutritional_value(self, vitamin):
        print(f"{self.name} is rich in vitamin {vitamin}")

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")


def ft_plant_types():
    Flower1 = Flower("rose", 25, 30, "red")
    Flower1.get_info()
    Flower1.bloom()
    print("")

    Tree1 = Tree("oak", 500, 1825, 50)
    Tree1.get_info()
    Tree1.produce_shade()
    print("")

    Veg1 = Vegetable("tomato", 80, 90, "summer")
    Veg1.get_info()
    Veg1.nutritional_value("c")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")
    ft_plant_types()
