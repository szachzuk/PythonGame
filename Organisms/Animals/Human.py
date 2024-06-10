from typing import Tuple, TYPE_CHECKING

from Organism import Organism

from ..Animal import Animal
import pygame

if TYPE_CHECKING:
    from ...World import World


class Human(Animal):

    def __init__(self, world: "World", position: Tuple[int, int], strength: int = 5, turns_to_active: int = 0, is_active:False = False) -> None:
        super().__init__(world, position, 'H', strength, 4)
        self._full_name = 'Human'
        self.__turns_to_active = turns_to_active
        self.__is_active = is_active

    def GetTurnsToActive(self) -> int:
        return self.__turns_to_active

    def GetIsActive(self) -> bool:
        return self.__is_active

    def UpdateMoveVector(self, move_vector: Tuple[int, int], move_update: Tuple[int, int]) -> Tuple[int, int]:
        original_vector = move_vector

        move_vector = tuple(map(sum, zip(move_vector, move_update)))

        if move_vector in self._world.POSSIBLE_MOVES or move_vector == (0, 0):
            return move_vector

        potential_moves = [
            (move_vector[0], move_vector[1] - move_update[1]),
            (move_vector[0] - move_update[0], move_vector[1] + move_update[1]),
            (original_vector[0] + move_update[0], original_vector[1])
        ]

        for mv in potential_moves or move_vector == (0, 0):
            if mv in self._world.POSSIBLE_MOVES:
                return mv

        return original_vector


    def Active(self):
        if self.__turns_to_active != 0:
            print(f'You will be able to use Alzur shield in {self.__turns_to_active} turns')
        else:
            self.__turns_to_active = 10
            self.__is_active = True

    def PlayerMove(self) -> Tuple[int, int]:
        direction_map = {
            pygame.K_UP: (0, -1),    # Up
            pygame.K_DOWN: (0, 1),   # Down
            pygame.K_LEFT: (-1, 0),  # Left
            pygame.K_RIGHT: (1, 0),  # Right
        }

        move_vector = (0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in direction_map:
                        change = direction_map[event.key]
                        move_vector = self.UpdateMoveVector(move_vector, change)
                        print(f"Moving {pygame.key.name(event.key)}")
                    elif event.key == pygame.K_a:
                        self.Active()
                    elif event.key == pygame.K_RETURN:  # Enter key
                        temp_position = tuple(map(lambda x, y: x + y, move_vector, self.GetPosition()))
                        if self._world.IsValidPosition(temp_position) and temp_position != self.GetPosition():
                            print("Ending turn")
                            return move_vector


    def Action(self) -> None:

        if self.__turns_to_active != 0:
            self.__turns_to_active -= 1

        if self.__turns_to_active < 5:
            self.__is_active = False

        if self.__is_active:
            print(f'Active is active still and it will last for {self.__turns_to_active - 5}')

        self._world.graphics.Draw(self._world.GetAllOrganism())
        super().Action(self.PlayerMove())

    def ReactionOnCollision(self, attacker: "Animal", move_vector: Tuple[int, int]):
        if not self.__is_active:
            super().ReactionOnCollision(attacker, move_vector)
            return

        new_pos = self._world.FirstFreePosition(self.GetPosition())
        if new_pos == None:
            return

        move_vector = tuple(map(lambda x, y: x - y, new_pos, attacker.GetPosition()))

        self._world.AddLog(f'{self.GetFullName()} shields agnist {attacker.GetFullName()} at position {self.GetPosition()}')
        attacker.Action(move_vector)
