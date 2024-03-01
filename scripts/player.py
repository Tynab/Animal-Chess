from scripts.common import PlayerSide, CellPosition

# Import all the pieces
import scripts.pieces.rat as rat
import scripts.pieces.cat as cat
import scripts.pieces.dog as dog
import scripts.pieces.wolf as wolf
import scripts.pieces.leopard as leopard
import scripts.pieces.tiger as tiger
import scripts.pieces.lion as lion
import scripts.pieces.elephant as elephant

class Player:
    """
    Represents a player in the Animal Chess game.
    """

    def __init__(self, side):
        """
        Initializes a new instance of the Player class.

        Args:
            side: The side of the player.
        """
        self.side = side  # Store the side of the player
        # Initialize the pieces for the player
        self.pieces = [rat.Rat(side), cat.Cat(side), dog.Dog(side), wolf.Wolf(side), leopard.Leopard(side), tiger.Tiger(side), lion.Lion(side), elephant.Elephant(side)]
        # Set the den for the player based on their side
        self.den =  side == PlayerSide.DARK and CellPosition.DARK_DEN or CellPosition.LIGHT_DEN
        # Set the traps for the player based on their side
        self.traps = side == PlayerSide.DARK and [CellPosition.DARK_TRAP_1, CellPosition.DARK_TRAP_2, CellPosition.DARK_TRAP_3] or [CellPosition.LIGHT_TRAP_1, CellPosition.LIGHT_TRAP_2, CellPosition.LIGHT_TRAP_3]