spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of names of spicy foods."""
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    """Return a list of spicy foods with a heat_level over 5."""
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    """Print spicy foods with their heat levels."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return a single dictionary for the spicy food matching the cuisine."""
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Print only the spiciest foods."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    """Return the average heat level of all spicy foods."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """Add a new spicy food to the list."""
    spicy_foods.append(spicy_food)
    return spicy_foods