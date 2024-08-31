from board import Brick, Foundation, Tableau, Urn


def print_table(tableau, foundation):
    print()
    print("=" * 50)
    print(foundation)
    print("=" * 50)
    print(tableau)
    print("=" * 50)
    print()


def main():
    urn = Urn()
    tableau = Tableau()
    foundation = Foundation()

    while len(urn) > 0:
        brick = urn.draw_brick()
        print("***** Brick drawn:", brick, "*****")

        # Place the brick in the tableau
        brick_placed = False
        while brick_placed == False:
            try:
                pile_idx = int(input("Select pile to place the brick (1 to 4).\n"))
                brick_placed = tableau.add_new_brick(brick, pile_idx)
            except ValueError:
                continue

        print_table(tableau, foundation)

        # Make moves on the tableau and foundation
        print("Make your moves")
        cmd = ""
        while cmd.upper() != "Q":
            if foundation.game_won():
                print("Game won!")
                break
            cmd = input("Select command (Q to quit the round).\n")
            try:
                if cmd.upper() == 'M':
                    # Move cards from pile to pile in the tableau
                    [p1, p2] = input("Enter source and destination pile (1 to 4), separated by space.\n").split()
                    tableau.tableau_to_tableau(int(p1), int(p2))
                    print_table(tableau, foundation)

                elif cmd.upper() == 'F':
                    # Move cards from tableau to foundation
                    p = int(input("Enter source pile (1 to 4) from which to move a brick into the foundation.\n"))
                    tableau.tableau_to_foundation(p, foundation)
                    print_table(tableau, foundation)
            except ValueError:
                continue

        print("End of round.\n")


if __name__ == '__main__':
    main()