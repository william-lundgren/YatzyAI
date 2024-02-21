# TERMINAL VERSION
import random as rand


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

    #diagram_header = ""
    diagram_header = " RESULTS ".center(width, "~") + "\n"

    for i, ele in enumerate(dice_values):
        diagram_header += 4 * " " + "nr:" + str(i + 1) + 4 * " "

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    print(dice_faces_diagram)

    #return "\n".join(dice_faces_rows)


def roll_dice(number):
    results = []

    for i in range(number):
        die = rand.randint(1, 6)
        results.append(die)

    return results


def reroll(dice):
    inp = input("Which dice do you want to reroll (enter dice numbers separated by spaces: ")
    # Make it 0 indexed
    inp = [int(x) - 1 for x in inp.split()]
    if 0 in inp:
        return dice

    for i, ele in enumerate(dice):
        if i in inp:
            dice[i] = roll_dice(1)[0]
    display_dice(dice)
    return dice


def setup():
    game_over = False
    print("Lets play!")
    dice = []
    while not game_over:
        # Start by rolling 5 dice
        dice = roll_dice(5)
        display_dice(dice)
        # 2 re-rolls per round
        for i in range(2):
            dice = reroll(dice)
        game_over = True  # testing 1 round

def check_score():
    pass


def main():
    setup()


if __name__ == "__main__":
    main()
