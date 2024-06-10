from typing import Tuple, TYPE_CHECKING
from random import randint
from ..Animal import Animal
from Organism import Organism

if TYPE_CHECKING:
    from ...World import World

class Antelope(Animal):

    def __init__(self, world: 'World', position: Tuple[int, int], strength:int = 4) -> None:
        super().__init__(world, position, 'A', strength, 4)
        self._full_name = 'Antilope'

    def Action(self, move_vector = None) -> None:
        if move_vector is None:
            move_vector = self.RandomMovement()
            super().Action(move_vector)
            if self.is_dead == False:
                move_vector = self.RandomMovement()
                super().Action(move_vector)
        else:
            super().Action(move_vector)

    def ReactionOnCollision(self, attacker: Organism, move_vector: Tuple[int]):
        chance = randint(0, 1)

        if chance:
            super().ReactionOnCollision(attacker, move_vector)
            return

        runaway_attempt = self._world.FirstFreePosition(self.GetPosition())

        if runaway_attempt == None:
            super().ReactionOnCollision(attacker, move_vector)
            return

        move_vector = tuple(map(lambda x, y: y - x, self.GetPosition(), runaway_attempt))
        super().Action(move_vector)