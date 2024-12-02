"""
Hazel Jeong
A01166162
"""


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


def skills() -> dict:
    return {"Rinse": {"Hit": 2, "Accuracy": 0.8},
            "Cut": {"Hit": 5, "Accuracy": 0.5},
            "Fire": {"Hit": 10, "Accuracy": 0.2}}


def make_character(character_name: str) -> dict:
    return {"Name": character_name, "X-coordinate": 2, "Y-coordinate": 2,
            "Current HP": 5, "Max HP": 5, "Level": 1, "Mastered Skills": ["Rinse"], "Items": set()}


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


def move_character(character, direction):
    pass


def check_if_goal_attained(character):
    pass


def check_for_battles():
    pass


def battle(character, ingredients, skill_dict):
    pass


def character_has_leveled(character, ingredients):
    pass


def level_up_protocol(character, skill_dict):
    pass


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

        skill_dict = skills()
        character = make_character(character_name)

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
                there_is_a_battle = check_for_battles()
                if there_is_a_battle:
                    battle(character, ingredients, skill_dict)
                    if character_has_leveled(character, ingredients):
                        level_up_protocol(character, skill_dict)
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
