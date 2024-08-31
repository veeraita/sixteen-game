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
            pile_idx = int(input(f"Select pile to place the brick (1 to 4).\n"))
            brick_placed = tableau.place_brick(new_brick, pile_idx)

        print_table(tableau, foundation)

        # Make moves


if __name__ == '__main__':
    main()