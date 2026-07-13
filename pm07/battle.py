from ex0 import FlameFactory, AquaFactory, CreatureFactory


def verify(factory: CreatureFactory) -> None:
    try:
        print("Testing factory")

        base = factory.create_base()
        evolved = factory.create_evolved()

        print(base.describe())
        print(base.attack())

        print(evolved.describe())
        print(evolved.attack())
    except Exception as e:
        print(f"Error testing factory: {e}")


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    try:
        print("Testing battle")

        creature_1 = f1.create_base()
        creature_2 = f2.create_base()

        print(creature_1.describe())
        print("   vs   ")
        print(creature_2.describe())
        print(" FIGHT!")
        print(creature_1.attack())
        print(creature_2.attack())
    except Exception as e:
        print(f"Error during battle: {e}")


if __name__ == "__main__":
    verify(FlameFactory())
    print()
    verify(AquaFactory())
    print()
    battle(FlameFactory(), AquaFactory())
