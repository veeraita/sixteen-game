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
        new_brick = urn.draw_brick()
        print("Brick drawn:", new_brick)

        # Place the brick in the tableau
        brick_placed = False
        while brick_placed == False:
            cmd = input("Select T to place the brick into the tableau, or F to place it into the foundation.\n")
            try:
                if cmd.upper() == "T":
                    pile_idx = int(input("Select pile to place the brick (1 to 4).\n"))
                    brick_placed = tableau.place_new_brick(new_brick, pile_idx)
                elif cmd.upper() == "F":
                    stack_idx = int(input("Select foundation stack to place the brick (1 to 6).\n"))
                    brick_placed = foundation.add_brick(new_brick, stack_idx)
            except ValueError:
                continue

        print_table(tableau, foundation)

        # Make moves


if __name__ == '__main__':
    main()