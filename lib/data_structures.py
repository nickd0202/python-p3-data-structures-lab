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
    pass
    list = []
    for n in spicy_foods:
        list.append(n.get('name'))
    return list

def get_spiciest_foods(spicy_foods):
    pass
    list = [n for n in spicy_foods if n.get('heat_level') > 5]
    return list
    

def print_spicy_foods(spicy_foods):
    pass
    for n in spicy_foods:
        list = n.get('name') + " (" + n.get('cuisine') + ") " + "| Heat Level: " + "🌶"*n.get('heat_level')
        print(list)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for n in spicy_foods:
        if n.get('cuisine') == cuisine:
            return n


def print_spiciest_foods(spicy_foods):
    pass
    for n in spicy_foods:
        if n.get("heat_level") > 5:
            list = n.get('name') + " (" + n.get('cuisine') + ") " + "| Heat Level: " + "🌶"*n.get('heat_level')
            print(list)

def get_average_heat_level(spicy_foods):
    pass
    list = []
    for n in spicy_foods:
        list.append(n.get('heat_level'))
    sum_l = sum(list)
    avg = sum_l/len(list)
    return avg


def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
