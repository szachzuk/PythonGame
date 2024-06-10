from typing import Tuple, TYPE_CHECKING
from random import randint
from ..Animal import Animal
from Organism import Organism

if TYPE_CHECKING:
    from ...World import World

class Turtle(Animal):

    def __init__(self, world: 'World', position: Tuple[int, int], strength:int = 2) -> None:
        super().__init__(world, position, 'T', strength, 1)
        self._full_name = 'Turtle'


    def Action(self, move_vector = None) -> None:
        if move_vector is None:
            chance = randint(0, 4)

            if not chance:
                move_vector = self.RandomMovement()
                super().Action(move_vector)
            else:
                self._world.AddLog(f'Turtle waits')
        else:
            super().Action(move_vector)



    def ReactionOnCollision(self, attacker: Organism, move_vector: Tuple[int]):
        if attacker.GetStrength() < 5:
            self._world.AddLog(f'Turtle shields')
        else:
            super().ReactionOnCollision(attacker, move_vector)