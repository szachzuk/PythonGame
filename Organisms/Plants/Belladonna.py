from typing import Tuple, TYPE_CHECKING

from Organism import Organism
from ..Plant import Plant


if TYPE_CHECKING:
    from ...World import World

class Belladonna(Plant):

    def __init__(self, world: "World", position: Tuple[int, int]):
        super().__init__(world, position, 'J', 99)
        self._full_name = 'Belladonna'


    def ReactionOnCollision(self, attacker: Organism, move_vector: Tuple[int, int]):
        attacker.is_dead = True
        super().ReactionOnCollision(attacker, move_vector)
        self._world.ClearPosition(self.GetPosition())
        self._world.ClearPosition(attacker.GetPosition())
        self.is_dead = True
