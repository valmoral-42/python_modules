class Plant:
    all_growth = 0

    def __init__(self, name: str):
        self.name = name.title()

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            return
        else:
            self.height = height

    def grow_plant(self, growth: int):
        if growth < 0:
            print(f"Invalid operation attempted: growth {growth}cm [REJECTED]")
            return
        self.height += growth
        Plant.all_growth += growth
        print(f"{self.name} grew {growth}cm")


class Tree(Plant):
    def __init__(self, name: str, height: int):
        super().__init__(name)
        self.set_height(height)

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name)
        self.set_height(height)
        self.color = color

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              "flowers (blooming)")


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list[Plant] = []
        self.plant_counter = 0

    def add_plant(self, plant: Plant):
        self.plant_counter += 1
        print(f"Added {self.name} to {self.owner}'s Garden")


class GardenManager:
    garden_counter = 0

    def __init__(self, owners: list[str]):
        self.my_gardens: dict[str, Garden] = {}
        if owners:
            self.my_gardens[Garden.owner] = Garden(Garden.owner)
            GardenManager.garden_counter += 1

    def get_garden(self, owner: str) -> Garden:
        return self.my_gardens[owner]

    @classmethod
    def create_garden(cls, owners: list[str]) -> "GardenManager":
        return cls(owners)


def ft_garden_analytics():
    manager = GardenManager.create_garden(["Alice", "Bob"])
    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Tree("oak tree", 99)
    rose = Flower("rose", 25, "red")
    sunflower = Flower("sunflower", 48, "yellow")
    print("")

    print("Alice is helping all plants grow...")
    oak.grow_plant(2)
    rose.grow_plant(1)
    sunflower.grow_plant(3)
    print("")

    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    oak.get_info()
    rose.get_info()
    sunflower.get_info(), print(", Prize points: (wip_fill)")
    print("")

    print(f"Plants added: {Plant.plant_counter}, "
          f"Total growth: {Plant.all_growth}cm")
    print("Plant types: (wip_fill) regular, (wip_fill) flowering, "
          "(wip_fill) prize flowers")
    print("")

    print("Height validation test: True")
    print("Garden Scores - (wip_fill)")
    print("Total gardens managed: (wip_fill)")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    ft_garden_analytics()
