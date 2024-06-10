from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from World import World

class Organism:

    def __init__(self, world: "World", position: Tuple[int, int], name:str = "Organism", strength: int = 0, initjative = 0) -> None:
        self._world: "World" = world
        self.__initjative: int = initjative
        self.__position: Tuple[int, int] = position
        self._age: int = 0
        self._strength: int = strength
        self.is_dead: bool = False
        self.__name: str = name

    def GetPosition(self) -> Tuple[int, int]:
        return self.__position

    def GetStrength(self) -> int:
        return self._strength

    def GetInitjative(self) -> int:
        return self.__initjative

    def GetAge(self) -> None:
        return self._age

    def GetName(self) -> str:
        return self.__name

    def GetFullName(self) -> str:
        return self._full_name

    def IncrementAge(self) -> None:
        self._age += 1


    def Birth(self) -> None:
        print("Something went wrong; Bearth of Organism")

    def Move(self, move_vector: Tuple[int, int]) -> None:
        self._world.ChangeCoordinates(self.GetPosition(), move_vector, self.GetName())
        self.__position = tuple(map(lambda x, y: x + y, self.GetPosition(), move_vector))

    def Collision(self, defender: 'Organism', move_vector: Tuple[int, int]) -> None:
        if self.GetName() == defender.GetName():
            self.Birth()
        else:
            defender.ReactionOnCollision(self, move_vector)

    def ReactionOnCollision(self, attacker: "Organism", move_vector: Tuple[int, int]):
        if attacker.GetStrength() >= self.GetStrength():
            self._world.AddLog(f'{self.GetFullName()} was eaten by {attacker.GetFullName()}, on position {self.GetPosition()}')
            self.is_dead = True
            self._world.ClearPosition(self.GetPosition())
            attacker.Move(move_vector)
        else:
            self._world.AddLog(f'{attacker.GetFullName()} was eaten by {self.GetFullName()}, on position {self.GetPosition()}')
            attacker.is_dead = True
            attacker._world.ClearPosition(attacker.GetPosition())
            self._world.ClearPosition(attacker.GetPosition())