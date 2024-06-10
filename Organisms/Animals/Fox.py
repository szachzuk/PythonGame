from typing import Tuple, TYPE_CHECKING
from random import randint
from ..Animal import Animal

if TYPE_CHECKING:
    from ...World import World

class Fox(Animal):

    def __init__(self, world: 'World', position: Tuple[int, int], strength:int = 3) -> None:
        super().__init__(world, position, 'F', strength, 7)
        self._full_name = 'Fox'


    def Action(self, move_vector = None) -> None:
        if move_vector is None:
            considerable_directions = []

            for move_vector in self._world.POSSIBLE_MOVES:

                move_attempt = tuple(map(lambda x, y: x + y, self.GetPosition(), move_vector))

                if not self._world.IsValidPosition(move_attempt):
                    continue

                org = self._world.OrganismFromPosition(move_attempt)

                if org is not None and org.GetStrength() > self.GetStrength():
                        continue

                considerable_directions.append(move_vector)

            length = len(considerable_directions)

            if length == 0:
                move_vector = self.RandomMovement()
            elif length == 1:
                move_vector = considerable_directions[randint(0,length - 1)]
            else:
                move_vector = considerable_directions[randint(0,length - 1)]

        super().Action(move_vector)

