from typing import Tuple, TYPE_CHECKING

from ..Plant import Plant


if TYPE_CHECKING:
    from ...World import World

class Milt(Plant):

    def __init__(self, world: "World", position: Tuple[int, int]):
        super().__init__(world, position, 'M')
        self._full_name = 'Milt'

    def Action(self):
        super().Action()
        super().Action()
        super().Action()
        self._age -= 2