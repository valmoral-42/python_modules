from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        _ = creature
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            c = cast(TransformCapability, creature)
            res1 = c.transform()
            res2 = creature.attack()
            res3 = c.revert()
            return f"{res1}\n{res2}\n{res3}"
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' "
                                       "for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            c = cast(HealCapability, creature)
            res1 = creature.attack()
            res2 = c.heal()
            return f"{res1}\n{res2}"
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' "
                                       "for this defensive strategy")
