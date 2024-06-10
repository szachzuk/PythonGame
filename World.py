from typing import Tuple, List, TYPE_CHECKING
from Organism import Organism
from json import dumps, load, JSONDecodeError
from random import randint

from Organisms.Animals.Wolf import Wolf
from Organisms.Animals.Sheep import Sheep
from Organisms.Animals.CyberSheep import CyberSheep
from Organisms.Animals.Antelope import Antelope
from Organisms.Animals.Turtle import Turtle
from Organisms.Animals.Fox import Fox
from Organisms.Animals.Human import Human

from Organisms.Plants.Belladonna import Belladonna
from Organisms.Plants.Grass import Grass
from Organisms.Plants.Guarana import Guarana
from Organisms.Plants.Milt import Milt
from Organisms.Plants.Sosnowski import Sosnowski

from Graphics import Graphics


if TYPE_CHECKING:
    from Organism import Organism


class World:

    def __init__(self, cols: int, rows: int) -> None:
        self.__cols:int = cols
        self.__rows:int = rows
        self.__plane: List[List[str]] = [[' ' for _ in range(self.__rows)] for _ in range(self.__cols)]
        self.__all_organisms: List["Organism"] = []
        self.__logs: List[str] = []
        self.POSSIBLE_MOVES: List[Tuple[int,int]] = [
            (-1, -1),
            (-1, 0),
            (-1, 1),

            (0, -1),
            (0, 1),

            (1, -1),
            (1, 0),
            (1, 1)
        ]
        self.graphics = Graphics(rows, cols)


    def GetCols(self) -> int:
        return self.__cols

    def GetRows(self) -> int:
        return self.__rows

    def GetAllOrganism(self) -> List[Organism]:
        return self.__all_organisms

    def OrganismFromPosition(self, position: Tuple[int, int]) -> 'Organism' :
        if self.__plane[position[0]][position[1]] != ' ':
            for organism in self.__all_organisms:
                if organism.GetPosition() == position and not organism.is_dead:
                    return organism
        else:
            return None

    def IsEmptyPosition(self, position: Tuple[int, int]) -> bool:
        return self.__plane[position[0]][position[1]] == ' '

    def ClearPosition(self, position: Tuple[int, int]) -> None:
        self.__plane[position[0]][position[1]] = ' '

    def FillPosition(self, position: Tuple[int, int], name: str) -> None:
        self.__plane[position[0]][position[1]] = name

    def ChangeCoordinates(self, position: Tuple[int, int], move: Tuple[int, int], name: str) -> None:
        self.ClearPosition(position)
        self.FillPosition((position[0] + move[0], position[1] + move[1]), name)

    def IsValidPosition(self, position: Tuple[int, int]) -> bool:
        return 0 <= position[0] < self.GetRows() and 0 <= position[1] < self.GetCols()

    def FirstFreePosition(self, position: Tuple[int, int]) -> Tuple[int, int]|None:
        for move in self.POSSIBLE_MOVES:
            candidate_move = (position[0] + move[0], position[1] + move[1])
            if self.IsValidPosition(candidate_move) and self.IsEmptyPosition(candidate_move):
                return candidate_move

        return None

    def AddOrganism(self, organism: 'Organism') -> None:
        self.__all_organisms.append(organism)
        self.FillPosition(organism.GetPosition(), organism.GetName())

    def Gravedigger(self) -> None:
        size = len(self.__all_organisms)
        i = 0
        while i < size:
            if self.__all_organisms[i].is_dead == True:
                self.__all_organisms.pop(i)
                size = size - 1
            else:
                i = i + 1

    def NewOgranismFromName(self, name: str, position: Tuple[int, int], strength: int = -1, turns_to_active:int = 0, is_active: bool = False) -> "Organism":
        org = None
        if name == "W":
            if strength == -1:
                org = Wolf(self, position)
            else:
                org = Wolf(self, position, strength=strength)
        elif name == "S":
            if strength == -1:
                org = Sheep(self, position)
            else:
                org = Sheep(self, position, strength=strength)
        elif name == "O":
            if strength == -1:
                org = CyberSheep(self, position)
            else:
                org = CyberSheep(self, position, strength=strength)
        elif name == "A":
            if strength == -1:
                org = Antelope(self, position)
            else:
                org = Antelope(self, position, strength=strength)
        elif name == "T":
            if strength == -1:
                org = Turtle(self, position)
            else:
                org = Turtle(self, position, strength=strength)
        elif name == "F":
            if strength == -1:
                org = Fox(self, position)
            else:
                org = Fox(self, position, strength=strength)
        elif name == 'H':
            if strength == -1:
                org = Human(self, position)
            else:
                org = Human(self, position, strength=strength, turns_to_active=turns_to_active, is_active=is_active)

        elif name == 'J':
            org = Belladonna(self, position)
        elif name == 'G':
            org = Grass(self, position)
        elif name == 'U':
            org = Guarana(self, position)
        elif name == 'M':
            org = Milt(self, position)
        elif name == 'B':
            org = Sosnowski(self, position)


        return org

    def AddLog(self, message: str) -> None:
        self.__logs.append(message)

    def PrintLogs(self):
        for log in self.__logs:
            print(log)
        print("\n\n")

    def PrintPlane(self):
        for row in self.__plane:
            print(row)

    def RandomizeWorld(self):
        organism_names = ['A', 'O', 'F', 'S', 'T', 'W', 'J', 'G', 'U', 'M', 'B']

        x = randint(0, self.__cols - 1)
        y = randint(0, self.__rows - 1)
        self.AddOrganism(self.NewOgranismFromName('H', (x, y)))

        for name in organism_names:
            for _ in range(3):
                attempt = 5
                while attempt > 0:
                    attempt -= 1
                    x = randint(0, self.__cols - 1)
                    y = randint(0, self.__rows - 1)
                    if self.IsEmptyPosition((x, y)):
                        self.AddOrganism(self.NewOgranismFromName(name, (x, y)))
                        break

    def GameLoop(self) -> None:

        self.__all_organisms.sort(key=lambda x:x.GetInitjative(), reverse=True)

        for organism in self.__all_organisms:
            if organism.is_dead == False:
                organism.Action()

        self.Gravedigger()
        self.PrintLogs()
        # self.PrintPlane()
        self.graphics.Draw(self.__all_organisms)

        self.__logs: List[str] = []

    def SaveState(self, file_name: str) -> None:
        try:
            with open(file_name, 'w') as file:
                data = {
                    'measurements': (self.__cols, self.__rows),
                    'organisms': []
                }

                for organism in self.__all_organisms:
                    organism_data = {
                        'name': organism.GetName(),
                        'position': organism.GetPosition(),
                        'strength': organism.GetStrength()
                    }
                    if isinstance(organism, Human):
                        organism_data['turns_to_active'] = organism.GetTurnsToActive()
                        organism_data['is_active'] = organism.GetIsActive()


                    data['organisms'].append(organism_data)

                file.write(dumps(data, indent=4))

        except IOError as e:
            print(f"Cannot open file {file_name} for writing: {e}")

    def LoadState(self, file_name: str) -> None:
        try:
            with open(file_name, 'r') as file:
                data = load(file)

                self.__cols, self.__rows = data['measurements']
                self.__plane = [[' ' for _ in range(self.__rows)] for _ in range(self.__cols)]
                self.graphics = Graphics(self.__rows, self.__cols)
                self.__all_organisms.clear()

                for org_data in data['organisms']:
                    org_name = org_data['name']
                    position = tuple(org_data['position'])
                    strength = org_data['strength']

                    if org_name == 'H':
                        turns_to_active = org_data['turns_to_active']
                        is_active = org_data['is_active']
                        organism = self.NewOgranismFromName(org_name, position, strength, turns_to_active, is_active)
                    else:
                        organism = self.NewOgranismFromName(org_name, position, strength)

                    self.AddOrganism(organism)

        except IOError as e:
            print(f"Cannot open file {file_name} for reading: {e}")
        except JSONDecodeError as e:
            print(f"Error parsing JSON from file {file_name}: {e}")
        except Exception as e:
            print(f"Error while loading state: {e}")

