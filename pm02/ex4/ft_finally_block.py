class PlantError(Exception):
    def __init__(self, default: str = "Unknown plant error") -> None:
        super().__init__(default)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering systems")
    print("Cleanup always happens, even with errors!")


def finally_block() -> None:
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce", "Carrots"]

    print("Testing valid plants...")
    finally_block(valid_plants)
    print("")

    print("Testing invalid plants...")
    finally_block(invalid_plants)
    print("")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("")
    finally_block()
