from typing import Tuple, TYPE_CHECKING
from ..Animal import Animal

if TYPE_CHECKING:
    from ...World import World

class Sheep(Animal):

    def __init__(self, world: "World", position: Tuple[int], name:str = 'S', strength:int = 4) -> None:
        super().__init__(world, position, name, strength, 4)
        self._full_name = 'Sheep'


    def Action(self, move_vector = None) -> None:
        if move_vector is None:
            move_vector = self.RandomMovement()
            super().Action(move_vector)
        else:
            super().Action(move_vector)

