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
    return([food["name"] for food in spicy_foods])

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    return [food_list for food_list in spicy_foods if food_list["heat_level"]>5]

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_emojis='🌶' * spicy_food['heat_level']
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_emojis}")
        
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    print([food for food in spicy_foods if food["cuisine"] == cuisine])
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
        
get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            heat_emojis='🌶' * spicy_food['heat_level'] 
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_emojis}")

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level=sum(food["heat_level"] for food in spicy_foods)
    average_heat_level=total_heat_level / len(spicy_foods)
    return int(average_heat_level)

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
