"""
Hazel Jeong
A01166162
"""

import itertools


def game_instructions(character_name: str) -> str:
    return (f"\nGood day, {character_name}. You are a junior chef who was travelling to a village known as a dream \n"
            f"land for chefs. After a few days of travelling, you decided to take a nap in the shade of a big tree. \n"
            f"But when you woke up, an old man was watching you curiously. You asked the man what he is up to, \n"
            f"and he said he has been starving for a while, and he asked if you could get some food for him.\n"
            f"Because you have such a kind heart, you decided to help him by getting some ingredients nearby and \n"
            f"cooking some delicious dish using those. You will be using some basic culinary skills, which you will \n"
            f"learn along the way, to get ingredients and cook some dish. \n\n"
            f"As a junior chef, you will be getting some vegetables. Once you level up to a sous chef, you now \n"
            f"can get some meat. Finally, once you become a head chef, you have all the power to cook some delicious \n"
            f"dish using all ingredients you got so far. \n\n")


def dishes() -> dict:
    return {"Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}


def show_dish_options(dish_dict: dict):
    print("Here are some dish options you can choose from:\n")
    for index, dish_name in enumerate(dish_dict.keys(), 1):
        dish_difficulty = dish_dict[dish_name]["Difficulty"]
        print("%d.\t%s, Difficulty: %s" % (index, dish_name, dish_difficulty))


def get_user_dish_choice(dish_dict: dict) -> str:
    dish_number = int(input("\nSelect the dish you would like to cook for the old man: "))
    while dish_number not in range(1, len(dish_dict.keys()) + 1):
        print(f"Invalid input. Please select a number between 1 and {len(dish_dict.keys())}.")
        dish_number = int(input("\nSelect the dish you would like to cook for the old man: "))
    dish_tuple = tuple(dish_dict)
    dish_name = dish_tuple[dish_number - 1]

    return dish_name


def show_ingredients_to_get(dish_dict: dict, dish_name: str):
    ingredients = ""
    for vegetable in dish_dict[dish_name]["Vegetables"]:
        ingredients += vegetable + ", "
    ingredients += f"and {dish_dict[dish_name]["Meat"]}"
    print(f"\nYou have chosen {dish_name}."
          f"\nYou will need to get {ingredients} to cook {dish_name}. ")


def each_level_ingredients(dish_dict: dict, dish_name: str) -> dict:
    return {1: dish_dict[dish_name]["Vegetables"], 2: dish_dict[dish_name]["Meat"]}


def ingredients_specs(ingredients: dict) -> dict:
    ingredients_dict = {}
    for vegetable in ingredients[1]:
        ingredients_dict[vegetable] = {"HP": 5, "Hit": 1, "Accuracy": 0.5}
    if ingredients[2] == "Chicken":
        ingredients_dict["Chicken"] = {"HP": 10, "Hit": 2, "Accuracy": 0.5}
    elif ingredients[2] == "Pork":
        ingredients_dict["Pork"] = {"HP": 10, "Hit": 3, "Accuracy": 0.5}
    else:
        ingredients_dict["Beef"] = {"HP": 10, "Hit": 4, "Accuracy": 0.75}

    return ingredients_dict


def show_ingredients_for_current_level(character: dict, ingredients: dict):
    current_level_ingredients = ""
    if character["Level"] == 1:
        for vegetable in ingredients[character["Level"]]:
            if vegetable == ingredients[character["Level"]][-1]:
                current_level_ingredients += "and " + vegetable
            else:
                current_level_ingredients += vegetable + ", "
    elif character["Level"] == 2:
        current_level_ingredients += ingredients[character["Level"]]

    print(f"\nYou are currently {character["Title"]}.\n"
          f"You need to collect {current_level_ingredients} to level up.")


def skills() -> dict:
    return {"Rinse": {"Hit": 2, "Accuracy": 0.8},
            "Cut": {"Hit": 5, "Accuracy": 0.5},
            "Fire": {"Hit": 10, "Accuracy": 0.2}}


def levels() -> dict:
    return {1: {"Title": "Junior Chef", "Max HP": 5, "Mastered Skills": ["Rinse"]},
            2: {"Title": "Sous Chef", "Max HP": 15, "Mastered Skills": ["Rinse", "Cut"]},
            3: {"Title": "Head Chef", "Max HP": 30, "Mastered Skills": ["Rinse", "Cut", "Fire"]}}


def make_character(character_name: str) -> dict:
    return {"Name": character_name, "Title": "Junior Chef", "Level": 1, "X-coordinate": 2, "Y-coordinate": 2,
            "Current HP": 5, "Max HP": 5, "Mastered Skills": ["Rinse"], "Items": []}


def describe_current_location(character: dict):
    current_coordinate = (character["X-coordinate"], character["Y-coordinate"])
    current_hp = character["Current HP"]

    print(f"\nYou are currently at {current_coordinate}, and you have {current_hp} HP left.")


def is_alive(character: dict) -> bool:
    return character["Current HP"] > 0


def get_user_direction_choice() -> str:
    print("Enter the direction you wish to travel: ")
    directions = ("North", "South", "East", "West")
    for index, direction in enumerate(directions, 1):
        print("%d.\t%s" % (index, direction))

    direction_choice = int(input())
    while direction_choice not in range(1, len(directions) + 1):
        print("\nInvalid input. Please try again.")
        print("Enter the direction you wish to travel: ")
        directions = ("North", "South", "East", "West")
        for index, direction in enumerate(directions, 1):
            print("%d.\t%s" % (index, direction))
        direction_choice = int(input())

    return directions[direction_choice - 1]


def validate_move(rows: int, columns: int, character: dict, direction: str) -> bool:
    if direction == "North":
        return character["Y-coordinate"] > 0
    elif direction == "South":
        return character["Y-coordinate"] < rows - 1
    elif direction == "East":
        return character["X-coordinate"] < columns - 1
    elif direction == "West":
        return character["X-coordinate"] > 0


def move_character(character: dict, direction: str):
    if direction == "North":
        character["Y-coordinate"] -= 1
    elif direction == "South":
        character["Y-coordinate"] += 1
    elif direction == "East":
        character["X-coordinate"] += 1
    elif direction == "West":
        character["X-coordinate"] -= 1


def check_for_battles(character: dict) -> bool:
    if character["Level"] == 3:
        return True
    else:
        return itertools.cycle(["battle", "safe"]) == "battle"


def battle(character, ingredients, skill_dict, ingredients_specs_dict):
    pass


def character_has_leveled(character: dict, ingredients: dict) -> bool:
    if character["Level"] == 1:
        return set(character["Items"]) == set(ingredients[character["Level"]])
    elif character["Level"] == 2:
        return character["Items"][0] == ingredients[character["Level"]]
    else:
        return True


def level_up_protocol(character: dict, level_dict: dict):
    character["Level"] += 1
    character["Title"] = level_dict["Title"]
    character["X-coordinate"] = 2
    character["Y-coordinate"] = 2
    character["Max HP"] = level_dict["Max HP"]
    character["Current HP"] = character["Max HP"]
    character["Mastered Skills"] = level_dict["Mastered Skills"]
    character["Items"] = []
    print(f"Congratulations! You have leveled up to level {character['Level']}!\n")
    print(f"Now you {character["Max HP"]} Max HP.")


def check_if_goal_attained(character: dict) -> bool:
    return character["Level"] > 3


def game():
    """
    Run the game.
    """
    character_name = input("What is your name? ").strip()
    if character_name == "":
        print("Invalid input. Please try again.")
        game()
    else:
        print(game_instructions(character_name))

        dish_dict = dishes()
        show_dish_options(dish_dict)
        dish_name = get_user_dish_choice(dish_dict)
        show_ingredients_to_get(dish_dict, dish_name)
        ingredients = each_level_ingredients(dish_dict, dish_name)
        ingredients_specs_dict = ingredients_specs(ingredients)

        skill_dict = skills()
        level_dict = levels()
        character = make_character(character_name)
        show_ingredients_for_current_level(character, ingredients)

        rows = 5
        columns = 5

        achieved_goal = False
        describe_current_location(character)

        while is_alive(character) and not achieved_goal:
            direction = get_user_direction_choice()
            valid_move = validate_move(rows, columns, character, direction)
            if valid_move:
                move_character(character, direction)
                describe_current_location(character)
                there_is_a_battle = check_for_battles(character)
                if there_is_a_battle:
                    battle(character, ingredients, skill_dict, ingredients_specs_dict)
                    if character_has_leveled(character, ingredients):
                        level_up_protocol(character, level_dict)
                        show_ingredients_for_current_level(character, ingredients)
                    describe_current_location(character)
                achieved_goal = check_if_goal_attained(character)
            else:
                print("\nYou've reached to a wall. Please enter the direction you wish to travel again.")
                describe_current_location(character)
        if is_alive(character):
            print("\nCongratulations! You won!")
        else:
            print("\nSorry, you died.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
