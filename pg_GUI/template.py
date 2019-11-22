import pygame,sys
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(30)
