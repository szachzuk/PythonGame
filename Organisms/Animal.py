from typing import Tuple, TYPE_CHECKING
from Organism import Organism
from random import randint

if TYPE_CHECKING:
    from World import World

class Animal(Organism):

    def __init__(self, world: 'World', position: Tuple[int, int], name:str, strength: int, initjative: int) -> None:
        super().__init__(world, position, name, strength, initjative)

    def RandomMovement(self) -> Tuple[int, int]:
        MOVES = self._world.POSSIBLE_MOVES
        END = len(MOVES)
        used = set()

        while len(used) < END:
            index = randint(0, END - 1)
            if index in used:
                continue
            used.add(index)

            move_attempt = tuple(map(lambda x, y: x + y, self.GetPosition(), MOVES[index]))

            if self._world.IsValidPosition(move_attempt):
                return MOVES[index]

        return None

    def Action(self, move_vector: Tuple[int, int]) -> None:
        self.IncrementAge()
        move_attempt = tuple(map(lambda x, y: x + y, self.GetPosition(), move_vector))

        if self._world.IsEmptyPosition(move_attempt):
            self.Move(move_vector)
            print(f'Animal - {self.GetFullName()} - moved to {self.GetPosition()}')
        else:
            defender = self._world.OrganismFromPosition(move_attempt)
            self.Collision(defender, move_vector)

    def Birth(self) -> None:
        if  self.GetAge() >= 3:
            free_square = self._world.FirstFreePosition(self.GetPosition())

            if free_square == None:
                return

            name = self.GetName()
            animal_to_be_added = self._world.NewOgranismFromName(name, free_square)
            self._world.AddOrganism(animal_to_be_added)
            print(f'Animal - {self.GetFullName()} - copulated at square {self.GetPosition()}')
        else:
            print(f"{self.GetFullName()} at {self.GetPosition()} is too young to reproduce")
