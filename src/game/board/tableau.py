from .brick import Brick
from config import MAX_CARD

class Tableau():
    def __init__(self):
        self.piles = {i: [] for i in range(1, 5)}

    def get_max_pile_length(self):
        return len(max(self.piles.values(), key=len))

    def add_new_brick(self, brick, pile_idx):
        if pile_idx not in self.piles.keys():
            print("Error: invalid pile number.")
            return False
        
        pile = self.piles[pile_idx]
        if len(pile) == 0:
            print(f"Brick {brick} placed in pile {pile_idx}. A new pile started.")
            pile.append(brick)
            return True
        else:
            print(f"Brick {brick} placed in pile {pile_idx}.")
            pile.append(brick)
            return True
            
    def add_bricks(self, bricks, pile_idx):
        pile = self.piles[pile_idx]

        if (len(pile) == 0) and (bricks[0].value == MAX_CARD):
            print(f"Bricks {[str(b) for b in bricks]} moved to empty pile {pile_idx}.")
            pile.extend(bricks)
            return True
        elif (len(pile) > 0) and (bricks[0].is_below(pile[-1])):
            print(f"Bricks {[str(b) for b in bricks]} moved to pile {pile_idx}.")
            pile.extend(bricks)
            return True
        else:
            print("Cannot make the move.")
            return False
        
    def tableau_to_tableau(self, pile1, pile2):
        """
        Check if any cards can be moved from pile1 to pile2, and perform the move.
        """
        p1_bricks = self.piles[pile1]
        for i in range(len(p1_bricks)):
            if sorted(set(p1_bricks[i:]), key=lambda x: x.value, reverse=True) == p1_bricks[i:]:
                if self.add_bricks(p1_bricks[i:], pile2):
                    self.piles[pile1] = p1_bricks[:i]
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
