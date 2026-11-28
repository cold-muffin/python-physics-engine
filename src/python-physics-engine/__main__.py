import pygame

from classes.particle import Particle

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

p0 = Particle(pos=[screen.get_width()/2, screen.get_height()/2], vel=[1, .2])

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("black")

  p0.tick()
  pygame.draw.circle(screen, "red", p0.pos.tolist(), 10)

  pygame.display.flip()

  clock.tick(60)