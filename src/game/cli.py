from board import Foundation, Tableau, Urn
from game import Game
from config import *

VALID_COMMANDS = ["H", "Q", "F", "T"]


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


def print_table(game):
    """
    Display the current state of the foundation and the tableau in the terminal.
    """
    print()
    print("=" * 60)
    print(game.foundation)
    print("=" * 60)
    print(game.tableau)
    print("=" * 60)
    print()


def parse_command(cmd):
    if cmd.upper() in VALID_COMMANDS:
        return cmd.upper()
    print("Not a valid command.")
    return None


def place_brick(tableau, brick):
    """
    Place a new brick in the pile selected by the user.
    """
    brick_placed = False
    while brick_placed == False:
        try:
            pile_idx = int(input(f"Select pile to place the brick (1 to {tableau.n_piles}).\n"))
            if not tableau.is_valid_pile_idx(pile_idx):
                print("Error: invalid pile number.")
                continue
            pile = tableau.add_new_brick(brick, pile_idx)
            if len(pile) == 1:
                print(f"Brick {brick} placed in pile {pile_idx}. A new pile started.")
            else:
                print(f"Brick {brick} placed in pile {pile_idx}.")
            brick_placed = True
        except ValueError:
            continue


def arrange_bricks(game):
    """
    Perform the second phase of each round where bricks can be
    moved between piles in the tableau and into the foundation.
    """
    print("***** Make your moves *****")
    cmd = None
    while cmd != "Q" and not game.game_won():
        active_piles = game.tableau.get_active_piles()
        active_stacks = game.foundation.get_active_stacks()

        cmd = parse_command(input("Select command (q to quit the round).\n"))
        try:
            if cmd == "T":
                # Move cards from pile to pile in the tableau
                [p1, p2] = input(
                    f"Enter source and destination pile (1 to {game.n_piles}), separated by space.\n"
                ).split()
                if not (
                    game.tableau.is_valid_pile_idx(int(p1))
                    and game.tableau.is_valid_pile_idx(int(p2))
                ):
                    print("Error: invalid pile number.")
                    continue
                moved_bricks = game.tableau.tableau_to_tableau(int(p1), int(p2))
                if not moved_bricks:
                    print("Cannot make the move.")
                else:
                    if game.tableau.get_active_piles() > active_piles:
                        print(
                            f"Bricks {', '.join([str(b) for b in moved_bricks])} moved from pile {p1} to empty pile {p2}."
                        )
                        active_piles = game.tableau.get_active_piles()
                    else:
                        print(
                            f"Bricks {', '.join([str(b) for b in moved_bricks])} moved from pile {p1} to pile {p2}."
                        )

                print_table(game)

            elif cmd == "F":
                # Move cards from tableau to foundation
                p = int(
                    input(
                        "Enter source pile (1 to 4) from which to move a brick into the foundation.\n"
                    )
                )
                if not game.tableau.is_valid_pile_idx(p):
                    print("Error: invalid pile number.")
                    continue
                moved_brick, stack = game.tableau.tableau_to_foundation(p, game.foundation)
                if not moved_brick:
                    print(f"Cannot move a brick to the foundation from stack {stack}.")
                else:
                    print(f"Brick {moved_brick} moved to foundation stack {stack}.")
                    if game.foundation.get_active_stacks() > active_stacks:
                        print("New foundation stack started.")
                        active_stacks = game.foundation.get_active_stacks()

                print_table(game)

            elif cmd == "H":
                print_commands()
        except ValueError:
            continue


def main():
    print(TITLE)
    print_commands()

    # Set up the game
    game = Game(max_rank=MAX_RANK, n_stacks=N_STACKS, n_piles=N_PILES)

    # Draw bricks from the urn
    while len(game.urn) > 0:
        brick = game.urn.draw_brick()
        print("***** Brick drawn:", brick, "*****")
        place_brick(game.tableau, brick)

        print_table(game)

        # Make moves on the tableau and foundation
        arrange_bricks(game)

        if not game.game_won():
            print("End of round.\n")
        else:
            print("Game won!")

    if not game.game_won():
        print("The urn is empty! Time to make your last moves.\n")
        arrange_bricks(game)

        if not game.game_won():
            print("Better luck next time!")
        else:
            print("Game won!")


if __name__ == "__main__":
    main()
