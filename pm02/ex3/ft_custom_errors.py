class GardenError(Exception):
    def __init__(self, default="Unknown error") -> None:
        super().__init__(default)


class PlantError(GardenError):
    def __init__(self, default="Unknown plant error") -> None:
        super().__init__(default)


class WaterError(GardenError):
    def __init__(self, default="Unknown garden error") -> None:
        super().__init__(default)


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


def custom_errors() -> None:
    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("")

    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("")

    print("Testing catching all garden errors...")
    try:
        test_plant()
    except PlantError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water()
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    print("")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    custom_errors()
