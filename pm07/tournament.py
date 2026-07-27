from ex0.creature import Creature
from ex0.factory import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategyError
from ex2.strategies import BattleStrategy


def opponent_label(factory: CreatureFactory, strategy: BattleStrategy) -> str:
    creature = factory.create_base()
    strategy_name = strategy.__class__.__name__.replace("Strategy", "")

    if isinstance(factory, HealingCreatureFactory):
        factory_name = "Healing"
    elif isinstance(factory, TransformCreatureFactory):
        factory_name = "Transform"
    else:
        factory_name = creature.name

    return f"({factory_name}+{strategy_name})"


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    participants: list[tuple[Creature, BattleStrategy]] = []
    for factory, strategy in opponents:
        participants.append((factory.create_base(), strategy))

    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            creature_1 = participants[i][0]
            strategy_1 = participants[i][1]

            creature_2 = participants[j][0]
            strategy_2 = participants[j][1]

            print("\n* Battle *")
            print(f"{creature_1.describe()}")
            print("  vs.  ")
            print(f"{creature_2.describe()}")
            print("  NOW FIGHT!")
            print(strategy_1.act(creature_1))
            print(strategy_2.act(creature_2))


def tournament(
    tournament_info: str,
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(tournament_info)

    labels = []
    for factory, strategy in opponents:
        labels.append(opponent_label(factory, strategy))
    print(", ".join(labels))

    try:
        battle(opponents)
    except InvalidStrategyError as error:
        print("Battle error, aborting tournament: ", error)


if __name__ == "__main__":
    t0 = [(FlameFactory(), NormalStrategy()),
          (HealingCreatureFactory(), DefensiveStrategy()),]
    tournament("== Tournament 0 (basic) ==", t0)
    print()

    t1 = [(FlameFactory(), AggressiveStrategy()),
          (HealingCreatureFactory(), DefensiveStrategy()),]
    tournament("== Tournament 1 (error) ==", t1)
    print()

    t2 = [(AquaFactory(), NormalStrategy()),
          (HealingCreatureFactory(), DefensiveStrategy()),
          (TransformCreatureFactory(), AggressiveStrategy()),]
    tournament("== Tournament 2 (multiple) ==", t2)
