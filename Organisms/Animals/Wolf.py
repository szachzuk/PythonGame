from typing import Tuple, TYPE_CHECKING
from ..Animal import Animal

if TYPE_CHECKING:
    from ...World import World

class Wolf(Animal):

    def __init__(self, world: 'World', position: Tuple[int, int], strength: int = 9) -> None:
        super().__init__(world, position, 'W', strength, 5)
        self._full_name = 'Wolf'

    def Action(self, move_vector = None) -> None:
        if move_vector is None:
            move_vector = self.RandomMovement()
        super().Action(move_vector)
