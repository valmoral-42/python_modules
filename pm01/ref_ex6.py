class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.growth: int = 0

    def grow(self) -> None:
        self.height += 1
        self.growth += 1
        print(f"{self.name} grew 1cm")

    def description(self) -> str:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color

    def description(self) -> str:
        print(f"- {self.name}: {self.height}cm,"
              f" {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points: int = points

    def description(self) -> str:
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming"
              f"), Prize points: {self.points}")


class Garden:
    total_growth = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.plant_cnt = 0

    def add_plant(self, plant: Plant, printable=True) -> None:
        self.plants += [plant]
        self.plant_cnt += 1

        if printable:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.description()


def sum_num(plants: list[Plant], class_type: str) -> int:
    size = 0

    for p in plants:
        if p.__class__.__name__ == class_type:
            size += 1
    return size


class GardenManager:
    garden_cntr = 0

    def __init__(self) -> None:
        self.network: dict[str, Garden] = {}

    def get_garden(self, owner: str) -> Garden:
        return self.network[owner]

    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.network[owner] = Garden(owner)
            cls.garden_cntr += 1
        return manager

    create_garden_network = classmethod(create_garden_network)

    def validate_height(height: int) -> bool:
        return height > 0

    validate_hight = staticmethod(validate_height)

    def garden_score(self, owner: str) -> int:
        if owner not in self.network:
            print("Manager name dosen't exist!!")
            return 0
        else:
            totale_height = 0
            garden = self.network[owner]
            for plant in garden.plants:
                totale_height += plant.height
            return totale_height + 40

    class GardenStatus:
        def calculate(garden: Garden) -> dict:
            regular_p = sum_num(garden.plants, "Plant")
            folwer_p = sum_num(garden.plants, "FloweringPlant")
            prize_p = sum_num(garden.plants, "PrizeFlower")

            return {"count": GardenManager.garden_cntr,
                    "growth": Garden.total_growth,
                    "types": (regular_p, folwer_p, prize_p)}


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    lavender = FloweringPlant("lavender", 20, "purple")
    corn = Plant("Corn", 32)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(corn, False)
    bob_garden.add_plant(lavender, False)

    print()
    alice_garden.grow_all()
    print()
    alice_garden.report()
    print()

    stats = GardenManager.GardenStatus.calculate(alice_garden)
    print(f"Plants added: {stats['count']}, Total growth: {stats['growth']}cm")

    r, f, p = stats["types"]
    print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers")
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    alice_score = manager.garden_score("Alice")
    bob_score = manager.garden_score("Bob")
    print(f"Garden scores - Alice: {alice_score} - Bob : {bob_score}")

    print(f"Total gardens managed: {GardenManager.garden_cntr}")