# TERMINAL VERSION
import random as rand
import re


def get_two_pair(dice):
    sorted_dice = sorted(dice)
    # If there is a two pair the sorted list must look like XYYZZ or YYXZZ or YYZZX depending on number sizes
    for i in (0, 2, 4):
        copied_list = sorted_dice.copy()
        copied_list.pop(i) # remove the odd number that is not a pair, must be on of these 3 as above
        if copied_list.count(copied_list[0]) == 2 and copied_list.count(copied_list[-1]) == 2:
            return sum(copied_list)
    return 0


def check_for_house(dice):
    # Two regex that check for the pattern XXYYY and XXXYY where X!=Y.
    # This will give a true/false for house after sorting all dice tosses.

    pattern = re.compile(r"(\d)\1\1((?!\1)\d)\2")
    pattern2 = re.compile(r"(\d)\1((?!\1)\d)\2\2")

    # Join the dice list into a single string for regex
    string = "".join(str(number) for number in sorted(dice))

    if pattern.search(string) or pattern2.search(string):
        return True
    else:
        return False


# borrrowed function from real python webiste to generate nice visuals
def display_dice(dice_values):
    DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }
    DIE_HEIGHT = len(DICE_ART[1])
    DIE_WIDTH = len(DICE_ART[1][0])
    DIE_FACE_SEPARATOR = " "

    """Return an ASCII diagram of dice faces from `dice_values`.
    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])

    # diagram_header = ""
    diagram_header = " RESULTS ".center(width, "~") + "\n"

    for i, ele in enumerate(dice_values):
        diagram_header += 4 * " " + "nr:" + str(i + 1) + 4 * " "

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    print(dice_faces_diagram)

    # return "\n".join(dice_faces_rows)


def roll_dice(number):
    results = []

    for i in range(number):
        die = rand.randint(1, 6)
        results.append(die)

    return results


def reroll(dice):
    inp = input("Which dice do you want to reroll (enter dice numbers separated by spaces: ")
    # Make it 0 indexed
    if "0" in inp:
        return dice
    inp = [int(x) - 1 for x in inp.split()]

    for i, ele in enumerate(dice):
        if i in inp:
            dice[i] = roll_dice(1)[0]
    display_dice(dice)
    return dice


def setup():
    game_over = False
    print("Lets play!")

    while not game_over:
        # Start by rolling 5 dice
        dice = roll_dice(5)
        old_dice = dice.copy()
        display_dice(dice)

        # 2 re-rolls per round
        for i in range(2):

            dice = reroll(dice)
            # They wanted to quit
            if old_dice == dice:
                break
        print(check_score(dice))
        game_over = True  # testing 1 round


def check_score(dice):
    ALL_SCORES = {
        "aces": dice.count(1),
        "twos": 2 * dice.count(2),
        "threes": 3 * dice.count(3),
        "fours": 4 * dice.count(4),
        "fives": 5 * dice.count(5),
        "sixes": 6 * dice.count(6),
        "pair": max(set([2 * x for x in dice if dice.count(x) > 1]), default=0),
        "two pair": get_two_pair(dice),
        "three of a kind": max(set([3 * x for x in dice if dice.count(x) > 2]), default=0),
        "four of a kind": max(set([4 * x for x in dice if dice.count(x) > 3]), default=0),
        "full house": check_for_house(dice) * sum(dice),  # true = 1, false = 0. will return sum of dice of it is house
        "small straight": 15 if sorted(dice) == [1, 2, 3, 4, 5] else 0,
        "large straight": 20 if sorted(dice) == [2, 3, 4, 5, 6] else 0,
        "yatzy": 50 if len(set(dice)) == 1 else 0,
        "chance": sum(dice)
    }

    return ALL_SCORES


def main():
    setup()


if __name__ == "__main__":
    main()
