import pygame

pygame.init()
done = False

windowWidth = 800
windowHeight = 500
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE):
            done = True

    screen = pygame.display.set_mode((windowWidth, windowHeight))

    mouseX, mouseY = pygame.mouse.get_pos()

    print(mouseX, ",", mouseY)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (0, mouseY, windowWidth, 1))
    pygame.draw.rect(screen, (255, 255, 255), (mouseX, 0, 1, windowHeight))

    pygame.display.flip()
    clock.tick(60)
