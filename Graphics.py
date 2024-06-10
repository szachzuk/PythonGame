import pygame
from typing import Tuple, List, TYPE_CHECKING


if TYPE_CHECKING:
    from Organism import Organism


OUTLINE_COLOR = (46, 139, 87)
OUTLINE_THICKNESS = 6
BACKGROUND_COLOR = (135, 206, 235)
FONT_COLOR = (0,0,0)


class Graphics:

    def __init__(self, rows, cols) -> None:
        self.__ROWS = rows
        self.__COLS = cols
        self.__WIDTH, self.__HEIGHT = 900, 900
        self.__SQUARE_HEIGHT = self.__HEIGHT // self.__ROWS
        self.__SQUARE_WIDTH = self.__WIDTH // self.__COLS

    def Start(self):
        pygame.init()
        pygame.font.init()

        self.__window = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption("Piotr Bekier s198173")
        self.FONT = pygame.font.SysFont("comicsans", 60, bold=True)


    def MouseClickCoordinates(self, position: Tuple[int, int]) -> Tuple[int, int]:
        x, y = position
        return (x * self.__COLS // self.__WIDTH, y * self.__ROWS // self.__HEIGHT)

    def ToWindowCoordinates(self, position: Tuple[int, int]) -> Tuple[int, int]:
        x, y = position
        OFFSET = (self.__SQUARE_WIDTH // 2, self.__SQUARE_HEIGHT // 2)

        return (x * self.__SQUARE_WIDTH + OFFSET[0], y * self.__SQUARE_HEIGHT + OFFSET[1])

    def DrawGrid(self):
        for row in range(1, self.__ROWS):
            y = row * self.__SQUARE_HEIGHT
            pygame.draw.line(self.__window, OUTLINE_COLOR, (0, y), (self.__WIDTH, y), OUTLINE_THICKNESS)

        for col in range(1, self.__COLS):
            x = col * self.__SQUARE_WIDTH
            pygame.draw.line(self.__window, OUTLINE_COLOR, (x, 0), (x, self.__HEIGHT), OUTLINE_THICKNESS)

        pygame.draw.rect(self.__window, OUTLINE_COLOR, (0,0, self.__WIDTH, self.__HEIGHT), OUTLINE_THICKNESS)

    def AddOrg(self, world, position: Tuple[int, int]):
        pos = self.MouseClickCoordinates(position)
        if world.IsEmptyPosition(pos):
            name = input("Podaj nazwe organismu: ")
            org = world.NewOgranismFromName(name, pos)
            if org is not None:
                world.AddOrganism(org)
            else:
                print("Taki organizm nie istnieje")


    def DrawOrganisms(self, all_ogranisms: List["Organism"]):
        for org in all_ogranisms:
            text = self.FONT.render(org.GetName(), 1, FONT_COLOR)
            window_coordinates = self.ToWindowCoordinates(org.GetPosition())
            text_rect = text.get_rect(center=window_coordinates)
            self.__window.blit(text, text_rect)

    def Draw(self, all_organisms: List["Organism"]):
        self.__window.fill(BACKGROUND_COLOR)
        self.DrawGrid()
        self.DrawOrganisms(all_organisms)
        pygame.display.update()

