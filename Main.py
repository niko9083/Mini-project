import pygame

pygame.init()
done = False

windowWidth = 1080
windowHeight = 760
clock = pygame.time.Clock()

titleFont = pygame.font.SysFont("Arial", 100, True)
font = pygame.font.SysFont("Arial", 50)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
            continue

        screen = pygame.display.set_mode((windowWidth, windowHeight))

        mouseX, mouseY = pygame.mouse.get_pos()

        titleText = titleFont.render("DuoPython", False, (255, 255, 255))

        if mouseX <= 245 and 210 >= mouseY >= 150:
            levelSelectText = font.render(" Level Select ", False, (0, 0, 0), (255, 255, 255))
        else:
            levelSelectText = font.render(" Level Select ", False, (255, 255, 255))

        if mouseX <= 120 and 285 >= mouseY > 225:
            quitText = font.render(" QUIT ", False, (0, 0, 0), (255, 255, 255))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                done = True
                continue
        else:
            quitText = font.render(" QUIT ", False, (255, 255, 255))

        screen.fill((0, 0, 0))

        screen.blit(titleText, (0, 0))
        screen.blit(levelSelectText, (0, 150))
        screen.blit(quitText, (0, 225))

        pygame.display.flip()
        clock.tick(60)
