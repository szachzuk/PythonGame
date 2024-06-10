from typing import Tuple, TYPE_CHECKING
from ..Plant import Plant

if TYPE_CHECKING:
    from ...World import World

class Grass(Plant):

    def __init__(self, world: "World", position: Tuple[int, int]):
        super().__init__(world, position, 'G')
        self._full_name = 'Grass'

