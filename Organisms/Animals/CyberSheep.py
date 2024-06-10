from typing import List, Tuple, TYPE_CHECKING
from random import randint
from .Sheep import Sheep

if TYPE_CHECKING:
    from ...World import World
    from Organism import Organism

def Distance(position1: Tuple[int, int], position2: Tuple[int, int]) -> int:
    temp = tuple(map(lambda x,y: abs(x-y), position1, position2))

    if temp[0] > temp[1]:
        return temp[0]
    else:
        return temp[1]

class CyberSheep(Sheep):

    def __init__(self, world: "World", position: Tuple[int, int], strength: int = 11) -> None:
        super().__init__(world, position, 'O', strength)
        self._full_name = 'CyberSheep'


    def Action(self, move_vector = None) -> None:
        if move_vector is None:
            all_sosnowski: List["Organism"] = [org for org in self._world.GetAllOrganism() if org.GetName() == 'B']

            if not all_sosnowski:
                super().Action()
                return

            closest = min(all_sosnowski, key=lambda org: Distance(self.GetPosition(), org.GetPosition()))

            min_distance = Distance(self.GetPosition(), closest.GetPosition())

            possible_moves = []

            for move in self._world.POSSIBLE_MOVES:
                temp_position = tuple(map(lambda x,y: x+y, move, self.GetPosition()))
                if Distance(temp_position, closest.GetPosition()) == min_distance - 1 and self._world.IsValidPosition(temp_position):
                    possible_moves.append(move)

            if possible_moves == 0:
                super().Action()
                return
            elif len(possible_moves) == 1:
                move_vector = possible_moves[0]
            else:
                move_vector = possible_moves[randint(0, len(possible_moves) - 1)]

        super().Action(move_vector)