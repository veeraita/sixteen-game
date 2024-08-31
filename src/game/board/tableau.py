from .brick import Brick

class Tableau():
    def __init__(self):
        self.n_piles = 0
        self.piles = {i: [] for i in range(1, 5)}

    def get_max_pile_length(self):
        return len(max(self.piles.values(), key=len))

    def place_brick(self, brick, pile_idx):
        if pile_idx < 1:
            print("Error: invalid pile number.")
            return False
        elif pile_idx > 4:
            print("Error: cannot make more than 4 piles in the tableau.")
            return False
        elif len(self.piles[pile_idx]) == 0:
            print(f"Brick {brick} placed in pile {pile_idx}. A new pile started.")
            self.piles[pile_idx].append(brick)
            self.n_piles += 1
            return True
        else:
            print(f"Brick {brick} placed in pile {pile_idx}.")
            self.piles[pile_idx].append(brick)
            return True

    def __str__(self):
        tableau_str_rows = ["Tableau\n\t1\t2\t3\t4"]
        tableau_str_rows.append("\t" + "- " * 14)
        for row in range(self.get_max_pile_length()):
            print_str = ""
            for col in range(1, 5):
                if len(self.piles[col]) > row:
                    print_str += "\t" + str(self.piles[col][row])
                else:
                    print_str += "\t"
            tableau_str_rows.append(print_str)
        return "\n".join(tableau_str_rows)