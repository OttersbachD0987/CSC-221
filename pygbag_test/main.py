import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 120, 200))
    screen.fill((100, 100, 0), (200, 200, 150, 150))
    pygame.display.flip()
    clock.tick(60)