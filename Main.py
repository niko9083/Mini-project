import pygame

pygame.init()
done = False

windowWidth = 800
windowHeight = 500
clock = pygame.time.Clock()

font =pygame.font.SysFont("Arial", 20)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE):
            done = True

    screen = pygame.display.set_mode((windowWidth, windowHeight))

    mouseX, mouseY = pygame.mouse.get_pos()

    xText = font.render(f"x: {mouseX}", False, (0, 0, 255))
    yText = font.render(f"y: {mouseY}", False, (0, 255, 0))

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 255), (mouseX, 0, 1, windowHeight))
    pygame.draw.rect(screen, (0, 255, 0), (0, mouseY, windowWidth, 1))
    screen.blit(xText, (0, 0))
    screen.blit(yText, (0, 20))

    pygame.display.flip()
    clock.tick(60)
