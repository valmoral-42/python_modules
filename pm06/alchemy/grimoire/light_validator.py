from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    elements_lower = ingredients.lower()
    if any(element.lower() in elements_lower
            for element in light_spell_allowed_ingredients()):
        result = "VALID"
    else:
        result = "INVALID"
    return f"{ingredients} - {result}"
