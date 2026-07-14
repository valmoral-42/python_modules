from ex0.creature import Creature
from ex0.factories import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategyError
from ex2.strategies import BattleStrategy


def run_tournament(title: str, opponents:
                   list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:
        print(title)
        parts = []
        for factory, strategy in opponents:
            temp_creature = factory.create_base()
            f_class_name = factory.__class__.__name__
            if "Healing" in f_class_name or "Transform" in f_class_name:
                f_display_name = f_class_name.replace(
                        "CreatureFactory", "").replace("Factory", "")
            else:
                f_display_name = temp_creature.name
            s_display_name = strategy.__class__.__name__.replace(
                "Strategy", "")
            parts.append(f"({f_display_name}+{s_display_name})")
        print(f" [{', '.join(parts)}]")

        print()
        print("*** TOURNAMENT ***")
        print(f"{len(opponents)} opponents involved")
        print()

        fighters = []
        for factory, strategy in opponents:
            fighters.append((factory.create_base(), strategy))

        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):

                c1: Creature = fighters[i][0]
                s1: BattleStrategy = fighters[i][1]

                c2: Creature = fighters[j][0]
                s2: BattleStrategy = fighters[j][1]

                print("* Battle *")
                print(c1.describe())
                print("   vs   ")
                print(c2.describe())
                print("   NOW FIGHT!")
                print(s1.act(c1))
                print(s2.act(c2))
                print()

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    print()
    tour0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    run_tournament("Tournament 0 (basic)", tour0)

    print()
    tour1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    run_tournament("Tournament 1 (error)", tour1)
    print()

    print()
    tour2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())]
    run_tournament("Tournament 2 (multiple)", tour2)
