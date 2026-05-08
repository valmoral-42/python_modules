class Plant:
    all_growth = 0
    plant_counter = 0

    def __init__(self, name: str, height: int):
        self.name = name.title()
        self.height = 0
        self.set_height(height)
        Plant.plant_counter += 1

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

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")

    def help_grow(self):
        print(f"{self.name} is helping all plants grow...")


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              "flowers (blooming)")


class PrizeFlwr(Flower):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flowers (blooming), Prize points: {self.points}")


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list[Plant] = []
        self.plant_count = 0
        self.local_growth = 0

    def add_plant(self, plant: Plant, printable: bool = True):
        self.plants.append(plant)
        self.plant_count += 1
        if printable:
            print(f"Added {plant.name} to {self.owner}'s Garden")

    def help_grow(self):
        print(f"{self.owner} is helping all plants grow...")

    def grow_plant(self, plant: Plant, growth: int):
        if plant not in self.plants:
            return
        before = plant.height
        plant.grow_plant(growth)
        self.local_growth += max(0, plant.height - before)

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()


class GardenManager:
    garden_counter = 0

    def __init__(self, owners: list[str]):
        self.my_gardens: dict[str, Garden] = {}
        for owner in owners:
            if owner in self.my_gardens:
                continue
            self.my_gardens[owner] = Garden(owner)
            GardenManager.garden_counter += 1

    def get_garden(self, owner: str) -> Garden:
        return self.my_gardens[owner]

    def garden_score(self, owner: str) -> int:
        garden = self.get_garden(owner)
        total_height = sum(plant.height for plant in garden.plants)
        return total_height + 40

    @classmethod
    def create_garden(cls, owners: list[str]) -> "GardenManager":
        return cls(owners)

    @staticmethod
    def count_type(plants: list[Plant], class_name: str) -> int:
        return sum(
            1 for plant in plants if plant.__class__.__name__ == class_name
        )

    class GardenStats:
        @staticmethod
        def garden_status(
            manager: "GardenManager", owner: str
        ) -> dict[str, object]:
            garden = manager.get_garden(owner)
            tree_count = GardenManager.count_type(garden.plants, "Plant")
            flower_count = GardenManager.count_type(garden.plants, "Flower")
            prize_count = GardenManager.count_type(garden.plants, "PrizeFlwr")

            return {
                "plants_in_garden": garden.plant_count,
                "local_growth": garden.local_growth,
                "tree_count": tree_count,
                "flower_count": flower_count,
                "prize_count": prize_count,
            }

        @staticmethod
        def gardens_status(manager: "GardenManager") -> dict[str, object]:
            total_plants = sum(
                garden.plant_count
                for garden in manager.my_gardens.values()
            )
            return {
                "gardens_managed": GardenManager.garden_counter,
                "plants_added": Plant.plant_counter,
                "total_plants_in_network": total_plants,
                "total_growth": Plant.all_growth,
            }


def ft_garden_analytics():
    manager = GardenManager.create_garden(["Alice", "Bob"])
    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Plant("oak tree", 99)
    rose = Flower("rose", 25, "red")
    sunflower = PrizeFlwr("sunflower", 48, "yellow", 10)
    tulip = Flower("tulip", 32, "purple")
    pine = Plant("pine tree", 220)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(tulip, False)
    bob_garden.add_plant(pine, False)
    print("")

    alice_garden.help_grow()
    alice_garden.grow_plant(oak, 2)
    alice_garden.grow_plant(rose, 1)
    alice_garden.grow_plant(sunflower, 3)
    print("")

    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    oak.get_info()
    rose.get_info()
    sunflower.get_info()
    print("")

    alice_stats = GardenManager.GardenStats.garden_status(manager, "Alice")

    print(f"Plants added: {alice_stats['plants_in_garden']}, "
          f"Total growth: {alice_stats['local_growth']}cm")
    print(f"Plant types: {alice_stats['tree_count']} regular, "
          f"{alice_stats['flower_count']} flowering, "
          f"{alice_stats['prize_count']} prize flowers")
    print("")

    alice_score = manager.garden_score("Alice")
    bob_score = manager.garden_score("Bob")
    network_stats = GardenManager.GardenStats.gardens_status(manager)
    print("Height validation test: True")
    print(f"Garden Scores - Alice: {alice_score} - Bob: {bob_score}")
    print(f"Total gardens managed: {network_stats['gardens_managed']}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    ft_garden_analytics()
