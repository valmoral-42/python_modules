from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    elements_lower = ingredients.lower()
    if any(element.lower() in elements_lower
            for element in dark_spell_allowed_ingredients()):
        result = "VALID"
    else:
        result = "INVALID"
    return f"{ingredients} - {result}"
