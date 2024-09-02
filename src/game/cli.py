from board import Foundation, Tableau, Urn
from config import *


def print_commands():
    """
    Provide the list of valid commands at the start of the game or when the user presses 'h'
    """
    print("Valid Commands: ")
    print("\tf - move card from Tableau to Foundation")
    print("\t\t #P - select pile from which to move cards")
    print("\tt - move cards from one Tableau pile to another")
    print("\t\t #P1 #P2 - select source and destination pile")
    print("\th - help")
    print("\tq - quit")
    print()


def print_table(tableau, foundation):
    """
    Display the current state of the foundation and the tableau in the terminal.
    """
    print()
    print("=" * 60)
    print(foundation)
    print("=" * 60)
    print(tableau)
    print("=" * 60)
    print()


def draw_and_place_brick(urn, tableau):
    """
    Draw a brick from the urn and place it in the pile selected by the user.
    """
    brick = urn.draw_brick()
    print("***** Brick drawn:", brick, "*****")

    brick_placed = False
    while brick_placed == False:
        try:
            pile_idx = int(input("Select pile to place the brick (1 to 4).\n"))
            if not tableau.is_valid_pile_idx(pile_idx):
                print("Error: invalid pile number.")
                continue
            brick_placed = tableau.add_new_brick(brick, pile_idx)
        except ValueError:
            continue


def arrange_bricks(tableau, foundation):
    """
    Perform the second phase of each round where bricks can be
    moved between piles in the tableau and into the foundation.
    """
    print("***** Make your moves *****")
    cmd = ""
    while cmd.upper() != "Q":
        if foundation.game_won():
            print("Game won!")
            break
        cmd = input("Select command (q to quit the round).\n")
        try:
            if cmd.upper() == "T":
                # Move cards from pile to pile in the tableau
                [p1, p2] = input(
                    "Enter source and destination pile (1 to 4), separated by space.\n"
                ).split()
                if not (tableau.is_valid_pile_idx(int(p1)) and tableau.is_valid_pile_idx(int(p2))):
                    print("Error: invalid pile number.")
                    continue
                tableau.tableau_to_tableau(int(p1), int(p2))
                print_table(tableau, foundation)

            elif cmd.upper() == "F":
                # Move cards from tableau to foundation
                p = int(
                    input(
                        "Enter source pile (1 to 4) from which to move a brick into the foundation.\n"
                    )
                )
                if not tableau.is_valid_pile_idx(p):
                    print("Error: invalid pile number.")
                    continue
                tableau.tableau_to_foundation(p, foundation)
                print_table(tableau, foundation)
            elif cmd.upper() == "H":
                print_commands()
        except ValueError:
            continue


def main():
    print(TITLE)
    print_commands()

    # Set up the game
    urn = Urn(max_rank=MAX_RANK, n_stacks=N_STACKS)
    tableau = Tableau(max_rank=MAX_RANK, n_piles=N_PILES)
    foundation = Foundation(max_rank=MAX_RANK, n_stacks=N_STACKS)

    # Draw bricks from the urn
    while len(urn) > 0:
        draw_and_place_brick(urn, tableau)

        print_table(tableau, foundation)

        # Make moves on the tableau and foundation
        arrange_bricks(tableau, foundation)

        if not foundation.game_won():
            print("End of round.\n")

    if not foundation.game_won():
        print("The urn is empty! Time to make your last moves.\n")
        arrange_bricks(tableau, foundation)

    if not foundation.game_won():
        print("Better luck next time!")


if __name__ == "__main__":
    main()
