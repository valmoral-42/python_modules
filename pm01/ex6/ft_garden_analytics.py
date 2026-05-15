class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(a) -> "Plant":
        return a("Unknown plant", 0, 0)

    def grow_plant(self, growth_height: float) -> None:
        self._height = self._height + growth_height
        self._stats._grow_i += 1

    def age_plant(self, growth_days: int) -> None:
        self._age = self._age + growth_days
        self._stats._age_i += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
        self._stats._show_i += 1

    class Stats:
        def __init__(self) -> None:
            self._grow_i = 0
            self._age_i = 0
            self._show_i = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_i} grow, {self._age_i} age, "
                  f"{self._show_i} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._blooming = False

    def bloom(self) -> None:
        self._blooming = True
        print(f"[asking the {self.name} to grow and bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {(self._height):.1f}"
              f"cm long and {self.trunk_diameter:.1f}cm wide")
        self._stats._shade_i += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_i = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_i} shade")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def grow_seed(self, new_seeds: int) -> None:
        self.seeds = self.seeds + new_seeds
        self._blooming = True
        print(f"[make {self.name} grow, age and bloom]")

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def ft_plant_analytics() -> None:
    print("=== Check year-old")
    days_to_check = 30
    print(f"Is {days_to_check} days more than a year? -> "
          f"{Plant.is_older_than_a_year(days_to_check)}")
    days_to_check = 400
    print(f"Is {days_to_check} days more than a year? -> "
          f"{Plant.is_older_than_a_year(days_to_check)}")
    print("")

    print("=== Flower")
    f1 = Flower("rose", 15, 10, "red")
    f1.show()
    display_stats(f1)
    f1.grow_plant(8)
    f1.bloom()
    f1.show()
    display_stats(f1)
    print("")

    print("=== Tree")
    t1 = Tree("oak", 200, 365, 5)
    t1.show()
    display_stats(t1)
    t1.produce_shade()
    display_stats(t1)
    print("")

    print("=== Seed")
    s1 = Seed("sunflower", 80, 45, "yellow", 0)
    s1.show()
    s1.grow_plant(30)
    s1.age_plant(20)
    s1.grow_seed(42)
    s1.show()
    display_stats(s1)
    print("")

    print("=== Anonymous")
    a1 = Plant.anonymous()
    a1.show()
    display_stats(a1)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_plant_analytics()
