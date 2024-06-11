from World import World
import pygame


# world.AddOrganism(world.NewOgranismFromName('B', (5,5)))
# world.AddOrganism(world.NewOgranismFromName('B', (6,6)))
# world.AddOrganism(world.NewOgranismFromName('B', (0,6)))
# world.AddOrganism(world.NewOgranismFromName('B', (0,4)))
# world.AddOrganism(world.NewOgranismFromName('B', (6,0)))
# world.AddOrganism(world.NewOgranismFromName('O', (0,3)))

# world.AddOrganism(world.NewOgranismFromName('S', (1,2)))
# world.AddOrganism(world.NewOgranismFromName('S', (0,1)))
# world.AddOrganism(world.NewOgranismFromName('S', (0,2)))




FPS = 60

def Game(world: "World"):
    world.graphics.Start()
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save = input("Czy chcesz zapisac gre Y/N: ")
                if save == "Y":
                    file_name = input("Podaj nazwe pliku do zapisu: ")
                    world.SaveState(file_name)
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    world.GameLoop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                world.graphics.AddOrg(world, pos)
                world.graphics.Draw(world.GetAllOrganism())
            else:
                world.graphics.Draw(world.GetAllOrganism())


    pygame.quit()

def main():
    choice = input("Czy chcesz wczytac gre? Y/N: ")
    if choice == 'Y':
        world = World(1,1)
        file_name = input("Podaj nazwe zapisu: ")
        world.LoadState(file_name)
    else:
        cols = int(input("podaj ilosc kolumn: "))
        rows = int(input("podaj ilosc wierszy: "))
        world = World(cols, rows)
        world.RandomizeWorld()

    Game(world)

main()