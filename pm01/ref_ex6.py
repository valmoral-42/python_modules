class Plant:
    plant_counter = 0
    all_growth = 0

    def __init__(self, name: str, height: int) -> None:
        self.name = name.title()
        self.height = 0
        self.set_height(height)
        Plant.plant_counter += 1

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            return
        self.height = height

    def grow_plant(self, growth: int = 1) -> None:
        if growth < 0:
            print(f"Invalid operation attempted: growth {growth}cm [REJECTED]")
            return
        self.height += growth
        Plant.all_growth += growth
        print(f"{self.name} grew {growth}cm")

    def get_info(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class Tree(Plant):
    def __init__(self, name: str, height: int) -> None:
        super().__init__(name, height)


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} "
              "flowers (blooming)")


class PrizeFlower(Flower):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, {self.color}  "
            f"flowers (blooming), Prize points: {self.points}"
        )


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.plant_count = 0

    def add_plant(self, plant: Plant, printable: bool = True) -> None:
        self.plants.append(plant)
        self.plant_count += 1
        if printable:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, growth: int = 1) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow_plant(growth)

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()


def count_exact_type(plants: list[Plant], class_name: str) -> int:
    count = 0
    for plant in plants:
        if plant.__class__.__name__ == class_name:
            count += 1
    return count


class GardenManager:
    garden_cntr = 0

    def __init__(self, owners: list[str] | None = None) -> None:
        self.my_gardens: dict[str, Garden] = {}
        self.network = self.my_gardens
        if owners:
            self.register_gardens(owners)

    def register_gardens(self, owners: list[str]) -> None:
        for owner in owners:
            if owner in self.my_gardens:
                continue
            self.my_gardens[owner] = Garden(owner)
            GardenManager.garden_cntr += 1

    def get_garden(self, owner: str) -> Garden:
        return self.my_gardens[owner]

    @classmethod
    def create_garden(cls, owners: list[str]) -> "GardenManager":
        return cls(owners)

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    validate_hight = validate_height

    def garden_score(self, owner: str) -> int:
        if owner not in self.my_gardens:
            print("Manager name dosen't exist!!")
            return 0

        total_height = 0
        garden = self.my_gardens[owner]
        for plant in garden.plants:
            total_height += plant.height
        return total_height + 40

    class GardenStatus:
        @staticmethod
        def calculate(garden: Garden) -> dict[str, object]:
            tree_count = count_exact_type(garden.plants, "Tree")
            flower_count = count_exact_type(garden.plants, "Flower")
            prize_count = count_exact_type(garden.plants, "PrizeFlower")

            return {
                "count": GardenManager.garden_cntr,
                "growth": Plant.all_growth,
                "types": (tree_count, flower_count, prize_count),
                "plants_added": Plant.plant_counter,
            }


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden(["Alice", "Bob"])

    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Tree("Oak Tree", 100)
    rose = Flower("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    lavender = Flower("lavender", 20, "purple")
    corn = Tree("Corn", 32)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(corn, False)
    bob_garden.add_plant(lavender, False)

    print()
    alice_garden.grow_all(1)
    print()
    alice_garden.report()
    print()

    stats = GardenManager.GardenStatus.calculate(alice_garden)
    print(
        f"Plants added: {stats['plants_added']}, "
        f"Total growth: {stats['growth']}cm"
    )

    tree_count, flower_count, prize_count = stats["types"]
    print(
        f"Plant types: {tree_count} regular, {flower_count} flowering, "
        f"{prize_count} prize flowers"
    )
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    alice_score = manager.garden_score("Alice")
    bob_score = manager.garden_score("Bob")
    print(f"Garden scores - Alice: {alice_score} - Bob : {bob_score}")

    print(f"Total gardens managed: {GardenManager.garden_cntr}")
