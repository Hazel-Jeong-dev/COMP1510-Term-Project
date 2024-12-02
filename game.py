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


def make_character(character_name):
    pass


def dishes():
    pass


def skills():
    pass


def show_dish_options(dish_dict):
    pass


def get_user_dish_choice(dish_dict):
    pass


def ingredients_to_get(character, dish_choice):
    pass


def describe_current_location(character):
    pass


def get_user_direction_choice():
    pass


def validate_move(rows, columns, character, direction):
    pass


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


def is_alive(character):
    pass


def game():
    """
    Run the game.
    """
    character_name = input("What is your name? ")
    print(game_instructions(character_name))

    dish_dict = dishes()
    show_dish_options(dish_dict)
    dish_choice = get_user_dish_choice(dish_dict)

    skill_dict = skills()
    character = make_character(character_name)
    ingredients = ingredients_to_get(character, dish_choice)

    rows = 5
    columns = 5

    achieved_goal = False
    print(describe_current_location(character))

    while is_alive(character) and not achieved_goal:
        direction = get_user_direction_choice()
        valid_move = validate_move(rows, columns, character, direction)
        if valid_move:
            move_character(character, direction)
            print(describe_current_location(character))
            there_is_a_battle = check_for_battles()
            if there_is_a_battle:
                battle(character, ingredients, skill_dict)
                if character_has_leveled(character, ingredients):
                    level_up_protocol(character, skill_dict)
                print(describe_current_location(character))
            achieved_goal = check_if_goal_attained(character)
        else:
            print("\nYou've reached to a wall. Please enter the direction you wish to travel again.")
            print(describe_current_location(character))
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
