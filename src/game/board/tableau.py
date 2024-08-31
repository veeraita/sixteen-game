from .brick import Brick
from config import MAX_CARD

class Tableau():
    def __init__(self):
        self.piles = {i: [] for i in range(1, 5)}

    def get_max_pile_length(self):
        return len(max(self.piles.values(), key=len))

    def add_brick(self, brick, pile_idx, new_brick=False):
        if (pile_idx < 1) or (pile_idx > 4):
            print("Error: invalid pile number.")
            return False
        
        pile = self.piles[pile_idx]
        if new_brick:
            if len(pile) == 0:
                print(f"Brick {brick} placed in pile {pile_idx}. A new pile started.")
                pile.append(brick)
                return True
            else:
                print(f"Brick {brick} placed in pile {pile_idx}.")
                pile.append(brick)
                return True
        else:
            if (len(pile) == 0) and (brick.value == MAX_CARD):
                print(f"Brick {brick} placed in empty pile {pile_idx}.")
                pile.append(brick)
                return True
            elif (len(pile) > 0) and (brick.value == pile[-1].value - 1):
                print(f"Brick {brick} placed in pile {pile_idx}.")
                pile.append(brick)
                return True
            else:
                print("Cannot make the move.")
                return False
        
    def tableau_to_tableau(self, pile1, pile2):
        """
        Check if any cards can be moved from pile1 to pile2, and perform the move.
        """
        brick = self.piles[pile1][-1]
        res = self.add_brick(brick, pile2, new_brick=False)
        if res:
            self.piles[pile1].pop()
            return True
        return False
    
    def tableau_to_foundation(self, pile_idx, foundation):
        """
        Check if any cards can be moved from the selected tableau pile to the foundation, and perform the move.
        """
        brick = self.piles[pile_idx][-1]
        res = foundation.add_brick(brick)
        if res:
            self.piles[pile_idx].pop()
            return True
        return False

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