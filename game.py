"""
Hazel Jeong
A01166162
"""

import random


def game_instructions(character_name: str) -> str:
    """
    Print game instructions.

    :param character_name: a string containing the character's name that the user input
    :precondition: character_name must be a string
    :postcondition: print the game instructions to the user
    :return: a string containing the game instructions

    >>> game_instructions("Chris") # doctest: +ELLIPSIS
    '\\nGood day, Chris. You are a junior chef who was travelling...all ingredients you got so far. \\n\\n'
    """
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
    """
    Create a dictionary containing all dish options the user can choose.

    :postcondition: return a dictionary containing the dish options
    :return: the dish options in a dictionary

    >>> dishes() # doctest: +NORMALIZE_WHITESPACE
    {'Galbijjim': {'Difficulty': 5, 'Vegetables': ('Carrots', 'Potatoes', 'Onions', 'Garlic'), 'Meat': 'Beef'},
    'Jeyuk': {'Difficulty': 3, 'Vegetables': ('Carrots', 'Onions', 'Garlic'), 'Meat': 'Pork'},
    'Dakgalbi': {'Difficulty': 2, 'Vegetables': ('Cabbages', 'Potatoes', 'Onions', 'Garlic'),
                 'Meat': 'Chicken'},
    'Kongbul': {'Difficulty': 3, 'Vegetables': ('Bean Sprouts', 'Onions', 'Garlic'), 'Meat': 'Pork'},
    'Jjimdak': {'Difficulty': 2, 'Vegetables': ('Carrots', 'Potatoes', 'Onions', 'Garlic'), 'Meat': 'Chicken'},
    'Samgyeopsal': {'Difficulty': 1, 'Vegetables': ('Lettuce', 'Garlic'), 'Meat': 'Pork'},
    'Bulgogi': {'Difficulty': 4, 'Vegetables': ('Carrots', 'Onions', 'Garlic'), 'Meat': 'Beef'}}
    """
    return {"Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}


def show_dish_options(dish_dict: dict):
    """
    Print the dish options to the user in a readable format.

    All dish names and each dish's difficulty level are printed to inform the user the dish options.

    :param dish_dict: a well-defined dictionary containing the dish options
    :precondition: dish_dict must be a dictionary
    :postcondition: print the dish options to the user in a readable format

    >>> dish_options = {"Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"),
    ...                             "Meat": "Beef"},
    ...                 "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
    ...                 "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
    ...                             "Meat": "Chicken"},
    ...                 "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"),
    ...                             "Meat": "Pork"},
    ...                 "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"),
    ...                              "Meat": "Chicken"},
    ...                 "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
    ...                 "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
    >>> show_dish_options(dish_options) # doctest: +NORMALIZE_WHITESPACE
    Here are some dish options you can choose from:
    1.	Galbijjim, Difficulty: 5
    2.	Jeyuk, Difficulty: 3
    3.	Dakgalbi, Difficulty: 2
    4.	Kongbul, Difficulty: 3
    5.	Jjimdak, Difficulty: 2
    6.	Samgyeopsal, Difficulty: 1
    7.	Bulgogi, Difficulty: 4
    """
    print("Here are some dish options you can choose from:\n")
    for index, dish_name in enumerate(dish_dict.keys(), 1):
        dish_difficulty = dish_dict[dish_name]["Difficulty"]
        print("%d.\t%s, Difficulty: %s" % (index, dish_name, dish_difficulty))


def get_user_dish_choice(dish_dict: dict) -> str:
    """
    Get the user's dish choice.

    :param dish_dict: a well-defined dictionary containing the dish options
    :precondition: dish_dict must be a dictionary
    :postcondition: return the dish name that the user choose
    :return: the dish name that the user choose as a string
    """
    dish_option = input("\nSelect the dish you would like to cook for the old man: ")
    while (dish_option.strip() == "" or not dish_option.isdigit()
           or int(dish_option) not in list(range(1, len(dish_dict.keys()) + 1))):
        print(f"Invalid input. Please select a number between 1 and {len(dish_dict.keys())}.")
        dish_option = input("\nSelect the dish you would like to cook for the old man: ")
    dish_tuple = tuple(dish_dict)
    dish_name = dish_tuple[int(dish_option) - 1]

    return dish_name


def show_ingredients_to_get(dish_dict: dict, dish_name: str):
    """
    Print the ingredients the user needs to get throughout the game based on the dish choice.

    :param dish_dict: a well-defined dictionary containing the dish options
    :param dish_name: a string indicating the dish name the user chose
    :precondition: dish_dict must be a dictionary
    :precondition: dish_name must be a string
    :precondition: dish_name must be one of the keys in dish_dict
    :postcondition: print the ingredients of the dish chosen to the user

    >>> dish_options = {"Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"),
    ...                             "Meat": "Beef"},
    ...                 "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
    ...                 "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
    ...                             "Meat": "Chicken"},
    ...                 "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"),
    ...                             "Meat": "Pork"},
    ...                 "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"),
    ...                              "Meat": "Chicken"},
    ...                 "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
    ...                 "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
    >>> dish = "Jeyuk"
    >>> show_ingredients_to_get(dish_options, dish) # doctest: +NORMALIZE_WHITESPACE
    You have chosen Jeyuk.
    You will need to get Carrots, Onions, Garlic, and Pork to cook Jeyuk.
    """
    ingredients = ""
    for vegetable in dish_dict[dish_name]["Vegetables"]:
        ingredients += vegetable + ", "
    ingredients += f"and {dish_dict[dish_name]["Meat"]}"
    print(f"\nYou have chosen {dish_name}."
          f"\nYou will need to get {ingredients} to cook {dish_name}. ")


def each_level_ingredients(dish_dict: dict, dish_name: str) -> dict:
    """
    Return a dictionary containing level - ingredients pairs.

    :param dish_dict: a well-defined dictionary containing the dish options
    :param dish_name: a string indicating the dish name the user chose
    :precondition: dish_dict must be a dictionary
    :precondition: dish_name must be a string
    :precondition: dish_name must be one of the keys in dish_dict
    :postcondition: return level - ingredients pairs in a dictionary
    :return: level - ingredients pairs in a dictionary

    >>> dish_options = {"Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"),
    ...                             "Meat": "Beef"},
    ...                 "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
    ...                 "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
    ...                             "Meat": "Chicken"},
    ...                 "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"),
    ...                             "Meat": "Pork"},
    ...                 "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"),
    ...                              "Meat": "Chicken"},
    ...                 "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
    ...                 "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
    >>> dish = "Jeyuk"
    >>> each_level_ingredients(dish_options, dish)
    {1: ('Carrots', 'Onions', 'Garlic'), 2: 'Pork', 3: 'Jeyuk'}
    """
    return {1: dish_dict[dish_name]["Vegetables"], 2: dish_dict[dish_name]["Meat"], 3: dish_name}


def ingredients_specs(ingredients: dict) -> dict:
    """
    Initialize the specs of ingredients the user needs to get throughout the game.

    :param ingredients: a dictionary containing the level - ingredients pairs
    :precondition: ingredients must be a dictionary
    :precondition: ingredients must contain keys indicating each level
    :precondition: ingredients must contain values indicating ingredients the user needs to get in each level
    :postcondition: initialize the specs of the ingredients including HP, Hit, and Accuracy
    :return: ingredients' specs in a dictionary

    >>> jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
    >>> ingredients_specs(jeyuk_ingredients) # doctest: +NORMALIZE_WHITESPACE
    {'Carrots': {'HP': 5, 'Hit': 1, 'Accuracy': 0.5},
    'Onions': {'HP': 5, 'Hit': 1, 'Accuracy': 0.5},
    'Garlic': {'HP': 5, 'Hit': 1, 'Accuracy': 0.5},
    'Pork': {'HP': 10, 'Hit': 3, 'Accuracy': 0.5},
    'Jeyuk': {'HP': 20, 'Hit': 5, 'Accuracy': 0.75}}
    >>> bulgogi_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Beef", 3: "Bulgogi"}
    >>> ingredients_specs(bulgogi_ingredients) # doctest: +NORMALIZE_WHITESPACE
    {'Carrots': {'HP': 5, 'Hit': 1, 'Accuracy': 0.5},
    'Onions': {'HP': 5, 'Hit': 1, 'Accuracy': 0.5},
    'Garlic': {'HP': 5, 'Hit': 1, 'Accuracy': 0.5},
    'Beef': {'HP': 10, 'Hit': 4, 'Accuracy': 0.75},
    'Bulgogi': {'HP': 20, 'Hit': 5, 'Accuracy': 0.75}}
    """
    ingredients_dict = {}
    for vegetable in ingredients[1]:
        ingredients_dict[vegetable] = {"HP": 5, "Hit": 1, "Accuracy": 0.5}

    if ingredients[2] == "Chicken":
        ingredients_dict["Chicken"] = {"HP": 10, "Hit": 2, "Accuracy": 0.5}
    elif ingredients[2] == "Pork":
        ingredients_dict["Pork"] = {"HP": 10, "Hit": 3, "Accuracy": 0.5}
    else:
        ingredients_dict["Beef"] = {"HP": 10, "Hit": 4, "Accuracy": 0.75}

    ingredients_dict[ingredients[3]] = {"HP": 20, "Hit": 5, "Accuracy": 0.75}

    return ingredients_dict


def show_ingredients_for_current_level(character: dict, ingredients: dict):
    """
    Print what ingredients the user needs to get in the current level.

    :param character: a well-defined dictionary containing the character's information
    :param ingredients: a dictionary containing the level - ingredients pairs
    :precondition: character must be a dictionary
    :precondition: ingredients must be a dictionary
    :postcondition: print an instructions on what the user needs to get in the current level

    >>> game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
    ...                   "Mastered Skills": ["Rinse"], "Items": []}
    >>> jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
    >>> show_ingredients_for_current_level(game_character, jeyuk_ingredients) # doctest: +NORMALIZE_WHITESPACE
    You are currently Junior Chef.
    You need to collect Carrots, Onions, and Garlic to level up.
    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
    >>> show_ingredients_for_current_level(game_character, jeyuk_ingredients) # doctest: +NORMALIZE_WHITESPACE
    You are currently Sous Chef.
    You need to collect Pork to level up.
    >>> game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 30, "Max HP": 30,
    ...                   "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": []}
    >>> jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
    >>> show_ingredients_for_current_level(game_character, jeyuk_ingredients) # doctest: +NORMALIZE_WHITESPACE
    You are currently Head Chef.
    You can now cook Jeyuk to win the game.
    """
    current_level_ingredients = ""
    if character["Level"] == 1:
        for vegetable in ingredients[character["Level"]]:
            if vegetable == ingredients[character["Level"]][-1]:
                current_level_ingredients += "and " + vegetable
            else:
                current_level_ingredients += vegetable + ", "
        print(f"\nYou are currently {character["Title"]}.\n"
              f"You need to collect {current_level_ingredients} to level up.")
    elif character["Level"] == 2:
        current_level_ingredients += ingredients[character["Level"]]
        print(f"\nYou are currently {character["Title"]}.\n"
              f"You need to collect {current_level_ingredients} to level up.")
    else:
        current_level_ingredients += ingredients[character["Level"]]
        print(f"\nYou are currently {character["Title"]}.\n"
              f"You can now cook {current_level_ingredients} to win the game.")


def skills() -> dict:
    """
    Create a dictionary containing all skills available to the user throughout the game.

    :postcondition: return a dictionary containing all skills available to the user throughout the game
    :return: all skills available to the user throughout the game in a dictionary

    >>> skills() # doctest: +NORMALIZE_WHITESPACE
    {'Rinse': {'Hit': 2, 'Accuracy': 0.75},
    'Cut': {'Hit': 5, 'Accuracy': 0.5},
    'Fire': {'Hit': 10, 'Accuracy': 0.25}}
    """
    return {"Rinse": {"Hit": 2, "Accuracy": 0.75},
            "Cut": {"Hit": 5, "Accuracy": 0.5},
            "Fire": {"Hit": 10, "Accuracy": 0.25}}


def levels() -> dict:
    """
    Create a dictionary containing all level information.

    :postcondition: return a dictionary containing all level information
    :return: all level information in a dictionary

    >>> levels() # doctest: +NORMALIZE_WHITESPACE
    {1: {'Title': 'Junior Chef', 'Max HP': 15, 'Mastered Skills': ['Rinse']},
    2: {'Title': 'Sous Chef', 'Max HP': 20, 'Mastered Skills': ['Rinse', 'Cut']},
    3: {'Title': 'Head Chef', 'Max HP': 30, 'Mastered Skills': ['Rinse', 'Cut', 'Fire']}}
    """
    return {1: {"Title": "Junior Chef", "Max HP": 15, "Mastered Skills": ["Rinse"]},
            2: {"Title": "Sous Chef", "Max HP": 20, "Mastered Skills": ["Rinse", "Cut"]},
            3: {"Title": "Head Chef", "Max HP": 30, "Mastered Skills": ["Rinse", "Cut", "Fire"]}}


def make_character(character_name: str) -> dict:
    """
    Create a character dictionary containing all information the game needs for the game play.

    :param character_name: a string containing the character's name that the user input
    :precondition: character_name must be a string
    :postcondition: return a character dictionary containing all information the game needs for the game play
    :return: a character dictionary containing all information the game needs for the game play in a dictionary

    >>> make_character("Chris") # doctest: +NORMALIZE_WHITESPACE
    {'Name': 'Chris', 'Title': 'Junior Chef', 'Level': 1, 'X-coordinate': 2, 'Y-coordinate': 2,
    'Current HP': 15, 'Max HP': 15, 'Mastered Skills': ['Rinse'], 'Items': []}
    """
    return {"Name": character_name, "Title": "Junior Chef", "Level": 1, "X-coordinate": 2, "Y-coordinate": 2,
            "Current HP": 15, "Max HP": 15, "Mastered Skills": ["Rinse"], "Items": []}


def describe_current_location(character: dict):
    """
    Print the current location and the current HP of the character to the user.

    :param character: a well-defined dictionary containing the character's information
    :precondition: character must be a dictionary
    :postcondition: print the current location and the HP of the character to the user

    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> describe_current_location(game_character) # doctest: +NORMALIZE_WHITESPACE
    You are currently at (2, 2), and you have 20 HP left.
    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 6, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> describe_current_location(game_character) # doctest: +NORMALIZE_WHITESPACE
    You are currently at (3, 0), and you have 6 HP left.
    """
    current_coordinate = (character["X-coordinate"], character["Y-coordinate"])
    current_hp = character["Current HP"]

    print(f"\nYou are currently at {current_coordinate}, and you have {current_hp} HP left.")


def is_alive(character: dict) -> bool:
    """
    Check if the character is alive or not.

    :param character: a well-defined dictionary containing the character's information
    :precondition: character must be a dictionary
    :postcondition: return a boolean indicating if the character is alive or not
    :return: a boolean indicating if the character is alive or not

    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> is_alive(game_character)
    True
    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 0, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> is_alive(game_character)
    False
    """
    return character["Current HP"] > 0


def get_user_direction_choice() -> str:
    """
    Get the user's direction choice.

    :postcondition: return the user's direction choice
    :return: the user's direction choice as a string
    """
    print("Enter the direction you wish to travel: ")
    directions = ("North", "South", "East", "West")
    for index, direction in enumerate(directions, 1):
        print("%d.\t%s" % (index, direction))

    direction_choice = input()
    while (direction_choice.strip() == "" or not direction_choice.isdigit()
           or int(direction_choice) not in range(1, len(directions) + 1)):
        print("\nInvalid input. Please try again.")
        print("Enter the direction you wish to travel: ")
        directions = ("North", "South", "East", "West")
        for index, direction in enumerate(directions, 1):
            print("%d.\t%s" % (index, direction))
        direction_choice = input()

    return directions[int(direction_choice) - 1]


def validate_move(rows: int, columns: int, character: dict, direction: str) -> bool:
    """
    Validate the movement of the character.

    :param rows: an integer indicating the number of rows of the board
    :param columns: an integer indicating the number of columns of the board
    :param character: a well-defined dictionary containing the character's information
    :param direction: a string indicating the direction the user wish to travel
    :precondition: rows must be a non-zero integer
    :precondition: rows must be a positive integer
    :precondition: columns must be a non-zero integer
    :precondition: columns must be a positive integer
    :precondition: character must be a dictionary
    :precondition: direction must be a string
    :precondition: direction must contain one value among "North", "South", "East", and "West"
    :postcondition: validate if the character can travel to the direction from the current location
    :return: validation result as a boolean

    >>> board_rows = 5
    >>> board_columns = 5
    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> move_direction = "South"
    >>> validate_move(board_rows, board_columns, game_character, move_direction)
    True
    >>> move_direction = "North"
    >>> validate_move(board_rows, board_columns, game_character, move_direction)
    False
    """
    if direction == "North":
        return character["Y-coordinate"] > 0
    elif direction == "South":
        return character["Y-coordinate"] < rows - 1
    elif direction == "East":
        return character["X-coordinate"] < columns - 1
    elif direction == "West":
        return character["X-coordinate"] > 0


def move_character(character: dict, direction: str):
    """
    Move the character to the direction given.

    :param character: a well-defined dictionary containing the character's information
    :param direction: a string indicating the direction the user wish to travel
    :precondition: character must be a dictionary
    :precondition: direction must be a string
    :precondition: direction must contain one value among "North", "South", "East", and "West"
    :postcondition: update the character's X- or Y-coordinates

    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    >>> move_direction = "South"
    >>> move_character(game_character, move_direction)
    >>> game_character == {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 3, "Y-coordinate": 1, "Current HP": 15, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    True
    >>> move_direction = "North"
    >>> move_character(game_character, move_direction)
    >>> game_character == {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    True
    """
    if direction == "North":
        character["Y-coordinate"] -= 1
    elif direction == "South":
        character["Y-coordinate"] += 1
    elif direction == "East":
        character["X-coordinate"] += 1
    elif direction == "West":
        character["X-coordinate"] -= 1


def check_for_battles(character: dict) -> bool:
    """
    Check if the character is about to have a battle in the current location.

    The chance of having a battle is 50% when the character is at level 1 or 2, and the chance becomes 100%
    when the character is at level 3.

    :param character: a well-defined dictionary containing the character's information
    :precondition: character must be a dictionary
    :postcondition: return True if the character is about to have a battle, otherwise False
    :return: a boolean indicating whether the character is about to have a battle
    """
    if character["Level"] == 3:
        return True
    else:
        return random.choice(["battle", "safe"]) == "battle"


def battle(character: dict, ingredients: dict, dish_name: str, skill_dict: dict, ingredients_specs_dict: dict):
    """
    Run the battle.

    :param character: a well-defined dictionary containing the character's information
    :param ingredients: a dictionary containing the level - ingredients pairs
    :param dish_name: a string indicating the dish name the user chose
    :param skill_dict: a well-defined dictionary containing all skills available throughout the game
    :param ingredients_specs_dict: a dictionary containing the specs of the ingredients including HP, Hit, and Accuracy
    :precondition: character must be a dictionary
    :precondition: ingredients must be a dictionary
    :precondition: dish_name must be a string
    :precondition: skill_dict must be a dictionary
    :precondition: ingredients_specs_dict must be a dictionary
    :postcondition: run the battle
    """
    if character["Level"] == 1:
        ingredient_encountered = random.choice(ingredients[character["Level"]])
        print(f"You see {ingredient_encountered} in front of you. Let's get it!")
    elif character["Level"] == 2:
        ingredient_encountered = ingredients[character["Level"]]
        print(f"It's time to prep some {ingredient_encountered}!")
    else:
        ingredient_encountered = dish_name
        print(f"Finally, it's time to cook {ingredient_encountered} using all ingredients you have collected so far!")

    ingredient_hit_chances = ["Hit" for _ in range(int(4 * ingredients_specs_dict[ingredient_encountered]["Accuracy"]))]
    for _ in range(4 - len(ingredient_hit_chances)):
        ingredient_hit_chances.append("Miss")

    while ingredients_specs_dict[ingredient_encountered]["HP"] > 0 and character["Current HP"] > 0:
        print(f"The remaining HP of {ingredient_encountered} is "
              f"{ingredients_specs_dict[ingredient_encountered]["HP"]}.")

        print("Choose a skill you wish to use:")
        for index, skill in enumerate(character["Mastered Skills"], 1):
            print("%d.\t%s - Hit: %s, Accuracy: %s"
                  % (index, skill, skill_dict[skill]["Hit"], skill_dict[skill]["Accuracy"]))

        skill_to_use = input()
        while (skill_to_use.strip() == "" or not skill_to_use.isdigit()
               or int(skill_to_use) not in range(1, len(character["Mastered Skills"]) + 1)):
            print("\nInvalid input. Please try again.")
            skill_to_use = input()

        chosen_skill_name = character["Mastered Skills"][int(skill_to_use) - 1]
        print(f"You attacked {ingredient_encountered} using {chosen_skill_name}!")

        skill_hit_chances = ["Hit" for _ in range(int(4 * skill_dict[chosen_skill_name]["Accuracy"]))]
        for _ in range(4 - len(skill_hit_chances)):
            skill_hit_chances.append("Miss")

        if random.choice(skill_hit_chances) == "Hit":
            print(f"Your attack was successful!")
            ingredients_specs_dict[ingredient_encountered]["HP"] -= skill_dict[chosen_skill_name]["Hit"]
        else:
            print(f"Your attack was missed!")

        if random.choice(ingredient_hit_chances) == "Hit":
            print(f"{ingredient_encountered} attacked you back!")
            character["Current HP"] -= ingredients_specs_dict[ingredient_encountered]["Hit"]
            print(f"You now have {character["Current HP"]} HP left.")
        else:
            print(f"{ingredient_encountered}'s attack was missed!")

    if character["Current HP"] > 0:
        print(f"Congratulations! You've collected {ingredient_encountered}.")
        character["Items"].append(ingredient_encountered)


def character_has_leveled(character: dict, ingredients: dict) -> bool:
    """
    Check if the character has leveled up or not.

    :param character: a well-defined dictionary containing the character's information
    :param ingredients: a dictionary containing the level - ingredients pairs
    :precondition: character must be a dictionary
    :precondition: ingredients must be a dictionary
    :postcondition: return a boolean indicating if the character has leveled up or not
    :return: a boolean indicating if the character has leveled up or not

    >>> jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
    >>> game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
    ...                   "Mastered Skills": ["Rinse"], "Items": ["Carrots", "Onions", "Garlic"]}
    >>> character_has_leveled(game_character, jeyuk_ingredients)
    True
    >>> game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": ["Pork"]}
    >>> character_has_leveled(game_character, jeyuk_ingredients)
    True
    >>> game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
    ...                   "Mastered Skills": ["Rinse"], "Items": ["Onions", "Garlic"]}
    >>> character_has_leveled(game_character, jeyuk_ingredients)
    False
    """
    if character["Level"] == 1:
        return set(character["Items"]) == set(ingredients[character["Level"]])
    elif character["Level"] == 2:
        return character["Items"][0] == ingredients[character["Level"]]
    else:
        return True


def level_up_protocol(character: dict, level_dict: dict):
    """
    Update the character's current spec to the new level's spec.

    :param character: a well-defined dictionary containing the character's information
    :param level_dict: a well-defined dictionary containing all level information
    :precondition: character must be a dictionary
    :precondition: level_dict must be a dictionary
    :postcondition: update the character's current spec to the new level's spec

    >>> level_info = {1: {"Title": "Junior Chef", "Max HP": 15, "Mastered Skills": ["Rinse"]},
    ...               2: {"Title": "Sous Chef", "Max HP": 20, "Mastered Skills": ["Rinse", "Cut"]},
    ...               3: {"Title": "Head Chef", "Max HP": 30, "Mastered Skills": ["Rinse", "Cut", "Fire"]}}
    >>> game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
    ...                   "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 3, "Max HP": 15,
    ...                   "Mastered Skills": ["Rinse"], "Items": ["Carrots", "Onions", "Garlic"]}
    >>> level_up_protocol(game_character, level_info) # doctest: +NORMALIZE_WHITESPACE
    Congratulations! You have leveled up to level 2!
    Now you have 20 Max HP.
    >>> game_character == {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
    ...                   "Mastered Skills": ["Rinse", "Cut"], "Items": []}
    True
    """
    character["Level"] += 1
    character["Title"] = level_dict[character["Level"]]["Title"]
    character["X-coordinate"] = 2
    character["Y-coordinate"] = 2
    character["Max HP"] = level_dict[character["Level"]]["Max HP"]
    character["Current HP"] = character["Max HP"]
    character["Mastered Skills"] = level_dict[character["Level"]]["Mastered Skills"]
    character["Items"] = []
    print(f"\nCongratulations! You have leveled up to level {character['Level']}!")
    print(f"Now you have {character["Max HP"]} Max HP.")


def check_if_goal_attained(character: dict, dish_name: str) -> bool:
    """
    Check if the character has achieved the game goal or not.

    :param character: a well-defined dictionary containing the character's information
    :param dish_name: a string indicating the dish name the user chose
    :precondition: character must be a dictionary
    :precondition: dish_name must be a string
    :postcondition: return True if the character has achieved the game goal, otherwise return False
    :return: a boolean indicating whether the character has achieved the game goal

    >>> game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
    ...                   "X-coordinate": 3, "Y-coordinate": 4, "Current HP": 7, "Max HP": 30,
    ...                   "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": ["Jeyuk"]}
    >>> dish = "Jeyuk"
    >>> check_if_goal_attained(game_character, dish)
    True
    >>> game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
    ...                   "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 30, "Max HP": 30,
    ...                   "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": []}
    >>> check_if_goal_attained(game_character, dish)
    False
    """
    return character["Items"] == [dish_name]


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
                    battle(character, ingredients, dish_name, skill_dict, ingredients_specs_dict)
                    if character_has_leveled(character, ingredients) and character["Level"] < 3:
                        level_up_protocol(character, level_dict)
                        show_ingredients_for_current_level(character, ingredients)
                    describe_current_location(character)
                achieved_goal = check_if_goal_attained(character, dish_name)
            else:
                print("\nYou've reached to a wall. Please enter the direction you wish to travel again.")
                describe_current_location(character)
        if is_alive(character):
            print("\nCongratulations! You won the game!")
            print("The old guy is very pleased with the dish you cooked. Well done!")
        else:
            print("\nSorry, you died.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
