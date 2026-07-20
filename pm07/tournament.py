from ex0.creature import Creature
from ex0.factory import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategyError
from ex2.strategies import BattleStrategy


def tournament(tournament_info: str, opponents:
               list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:
        print(tournament_info)
        parts = []
        for factory, strategy in opponents:
            temp_creature = factory.create_base()
            factory_class_name = factory.__class__.__name__
            if "Healing" or "Transform" in factory_class_name:
                factory_display_name = factory_class_name.replace(
                        "CreatureFactory", "").replace("Factory", "")
            else:
                factory_display_name = temp_creature.name
            strategy_name = strategy.__class__.__name__.replace(
                "Strategy", "")
            parts.append(f"({factory_display_name}+{strategy_name})")
        print(f" [{', '.join(parts)}]")

        print()
        print("*** TOURNAMENT ***")
        print(f"{len(opponents)} opponents involved")
        print()

        participants = []
        for factory, strategy in opponents:
            participants.append((factory.create_base(), strategy))

        for i in range(len(participants)):
            for j in range(i + 1, len(participants)):

                c1: Creature = participants[i][0]
                s1: BattleStrategy = participants[i][1]

                c2: Creature = participants[j][0]
                s2: BattleStrategy = participants[j][1]

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
    t0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    tournament("Tournament 0 (basic)", t0)

    print()
    t1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    tournament("Tournament 1 (error)", t1)
    print()

    print()
    t2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())]
    tournament("Tournament 2 (multiple)", t2)
