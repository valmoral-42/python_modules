import potions
from ..elements import create_air
import elements


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: brew "
            f"'{create_air()}' and '{potions.strength_potion()}' "
            f"mixed with '{elements.create_fire()}'")
