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

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        blooming: bool = True,
    ) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def get_info(self) -> str:
        bloom_state = "blooming" if self.blooming else "not blooming"
        return (
            f"- {self.name}: {self.height}cm, {self.color} flowers "
            f"({bloom_state})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        points: int,
        blooming: bool = True,
    ) -> None:
        super().__init__(name, height, color, blooming)
        self.points = points

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.points}"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.plant_count = 0
        self.local_growth = 0

    def add_plant(self, plant: Plant, printable: bool = True) -> None:
        self.plants.append(plant)
        self.plant_count += 1
        if printable:
            print(f"Added {plant.name} to {self.owner}'s Garden")

    def grow_all(self, growth: int = 1) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            before = plant.height
            plant.grow_plant(growth)
            self.local_growth += max(0, plant.height - before)

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())


class GardenManager:
    garden_counter = 0

    def __init__(self, owners: list[str] | None = None) -> None:
        self.my_gardens: dict[str, Garden] = {}
        if owners:
            self.register_gardens(owners)

    def register_gardens(self, owners: list[str]) -> None:
        for owner in owners:
            normalized_owner = self.normalize_owner_name(owner)
            if normalized_owner in self.my_gardens:
                continue
            self.my_gardens[normalized_owner] = Garden(normalized_owner)
            GardenManager.garden_counter += 1

    def get_garden(self, owner: str) -> Garden:
        return self.my_gardens[self.normalize_owner_name(owner)]

    def garden_score(self, owner: str) -> int:
        garden = self.get_garden(owner)
        total_height = sum(plant.height for plant in garden.plants)
        return total_height + 40

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        return cls(owners)

    @staticmethod
    def normalize_owner_name(owner: str) -> str:
        return owner.strip().title()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    @staticmethod
    def count_type(plants: list[Plant], class_name: str) -> int:
        return sum(
            1 for plant in plants if plant.__class__.__name__ == class_name
        )

    class GardenStats:
        @staticmethod
        def garden_snapshot(
            manager: "GardenManager", owner: str
        ) -> dict[str, object]:
            garden = manager.get_garden(owner)
            tree_count = GardenManager.count_type(garden.plants, "Plant")
            flowering_count = GardenManager.count_type(
                garden.plants, "FloweringPlant"
            )
            prize_count = GardenManager.count_type(
                garden.plants, "PrizeFlower"
            )

            return {
                "owner": garden.owner,
                "plants_in_garden": garden.plant_count,
                "local_growth": garden.local_growth,
                "total_height": sum(plant.height for plant in garden.plants),
                "types": {
                    "regular": tree_count,
                    "flowering": flowering_count,
                    "prize": prize_count,
                },
            }

        @staticmethod
        def network_snapshot(manager: "GardenManager") -> dict[str, object]:
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


def ft_garden_analytics() -> None:
    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Plant("oak tree", 99)
    rose = FloweringPlant("rose", 25, "red")
    sunflower = PrizeFlower("sunflower", 48, "yellow", 10)
    lavender = FloweringPlant("lavender", 20, "purple")
    corn = Plant("corn", 32)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(corn, False)
    bob_garden.add_plant(lavender, False)

    print("")
    alice_garden.grow_all(1)
    print("")

    alice_garden.report()
    print("")

    alice_stats = GardenManager.GardenStats.garden_snapshot(manager, "Alice")
    network_stats = GardenManager.GardenStats.network_snapshot(manager)

    print(
        f"Plants added: {network_stats['plants_added']}, "
        f"Total growth: {network_stats['total_growth']}cm"
    )

    types = alice_stats["types"]
    print(
        f"Plant types: {types['regular']} regular, "
        f"{types['flowering']} flowering, "
        f"{types['prize']} prize flowers"
    )

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    alice_score = manager.garden_score("Alice")
    bob_score = manager.garden_score("Bob")
    print(f"Garden Scores - Alice: {alice_score} - Bob: {bob_score}")

    print(f"Total gardens managed: {network_stats['gardens_managed']}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    ft_garden_analytics()
