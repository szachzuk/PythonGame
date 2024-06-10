from typing import Tuple, TYPE_CHECKING

from Organism import Organism
from ..Plant import Plant

if TYPE_CHECKING:
    from ...World import World

class Guarana(Plant):

    def __init__(self, world: "World", position: Tuple[int, int]):
        super().__init__(world, position, 'U')
        self._full_name = 'Guarana'


    def ReactionOnCollision(self, attacker: Organism, move_vector: Tuple[int]):
        attacker._strength += 3
        super().ReactionOnCollision(attacker, move_vector)


