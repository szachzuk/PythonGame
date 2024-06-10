from typing import Tuple, TYPE_CHECKING

from Organism import Organism
from ..Plant import Plant

if TYPE_CHECKING:
    from ...World import World

class Sosnowski(Plant):

    def __init__(self, world: "World", position: Tuple[int]):
        super().__init__(world, position, 'B', 10)
        self._full_name = 'BarszczSosnowskiego'

    def Action(self):

        for neighbour in self._world.POSSIBLE_MOVES:
            pos = tuple(map(lambda x, y: x + y, self.GetPosition(), neighbour))

            if self._world.IsValidPosition(pos) and not self._world.IsEmptyPosition(pos):
                org = self._world.OrganismFromPosition(pos)
                if org.GetInitjative() != 0 and org.GetName() != 'O':
                    org.is_dead = True
                    self._world.ClearPosition(pos)
                    self._world.AddLog(f"{self.GetFullName()} removes {org.GetFullName()} from position {org.GetPosition()}")

        super().Action()