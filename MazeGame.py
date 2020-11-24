import pygame
WIDTH = 800
HEIGHT = 800
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0, 0, 0]
screen.fill(white)
pygame.display.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def GridGame(a):
    b = int(WIDTH/a)
    c = int(HEIGHT/a)
    for x in range(0, WIDTH, b):
        for y in range(0, HEIGHT, c):
            pygame.draw.line(screen, (0,0,0), (WIDTH/(x+b), HEIGHT/(y+c)), (WIDTH/(x+b), HEIGHT))
            pygame.draw.line(screen, (0,0,0), (WIDTH/(x+b), HEIGHT/(y+c)), (WIDTH, HEIGHT/(y+c)))

GridGame(4)



