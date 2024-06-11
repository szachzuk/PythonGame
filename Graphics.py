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


    def GetNewOrganism(self, window):
        list_of_all_organisms = {
            "Cyber_owca": "O",
            "Wilk": "W",
            "Owca": "S",
            "Lis": "F",
            "Antylopa": "A",
            "Zolw": "T",
            "Wilcze_jagody": "J",
            "Barszcz_sosnowskiego": "B",
            "Trawa": "G",
            "Guarana": "U",
            "Mlecz": "M",
        }

        menu_active = True
        while menu_active:
            window.fill((255, 255, 255))
            y_poz = 20
            font = pygame.font.Font(None, 36)
            organism_rects = []

            for i, nazwa in enumerate(list_of_all_organisms.keys()):
                text = font.render(nazwa, True, (0, 0, 0))
                text_rect = window.blit(text, (20, y_poz))
                organism_rects.append((text_rect, list_of_all_organisms[nazwa]))
                y_poz += 40

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mysz_x, mysz_y = event.pos
                    for rect, symbol in organism_rects:
                        if rect.collidepoint(mysz_x, mysz_y):
                            return symbol

    def AddOrg(self, world, position: Tuple[int, int]):
        pos = self.MouseClickCoordinates(position)
        print(f"Clicked Position: {position}, Translated Position: {pos}")
        if world.IsEmptyPosition(pos):
            name = self.GetNewOrganism(self.__window)
            print(f"Selected Organism: {name}")
            if name is not None:
                new_org = world.NewOgranismFromName(name, pos)
                world.AddOrganism(new_org)
                print(f'Organism {name} added on position {pos}')
        else:
            print(f"Position {pos} is not empty.")
        self.Draw(world.GetAllOrganism())

