import pygame

pygame.init()
pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  clock.tick(60)