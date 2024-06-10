from typing import Tuple, TYPE_CHECKING
from Organism import Organism
from random import randint

if TYPE_CHECKING:
    from World import World

class Plant(Organism):

    def __init__(self,world: 'World', position: Tuple[int, int], name: str, strength: int = 0):
        super().__init__(world, position, name, strength)

    def Birth(self) -> None:
        if  self.GetAge() >= 3:
            free_square = self._world.FirstFreePosition(self.GetPosition())

            if free_square == None:
                return

            name = self.GetName()
            plant_to_be_added = self._world.NewOgranismFromName(name, free_square)
            self._world.AddOrganism(plant_to_be_added)
            self._world.AddLog(f'Plant - {self.GetFullName()} - spread itself at square {self.GetPosition()}')
        else:
            self._world.AddLog("Too young to spread")



    def Action(self):
        self.IncrementAge()
        chance = randint(0, 20)

        if chance == 0:
            self.Birth()
        else:
            self._world.AddLog(f'{self.GetFullName()} do not spread')
