import pygame time, sys

pygame.init()
pygame.time.delay(100)
screen=pygame.display.set_mode((1000,800))
white=[255,255,255]
red=[255,0,0]
green=[0,255,0]

screen.fill(white)
pygame.display.set_caption("My Shapes')
pygame.display.flip()
running = True
  x=200
  y=200
  w=50
  h=100
  r = 20
while running:

  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      running = False
  pygame.time.delay(100)
  pygame.draw.rect(screen,(10,123,10),(20,20,50,100))
  pygame.display.update()
  keyBoardKey.key.get_pressed()
  speed = 5
  if keyBoardKey[pygame.K_Left]:
    x -= speed
    r -= speed
  if keyBoardKey[pygame.K_Right]:
    x += speed
    r += speed
  if keyBoardKey[pygame.K_UP]:
    y -= speed
  if keyBoardKey[pygame.K_Left]:
    y += speed
   if keyBoardKey[pygame.K_W]:
    h += speed
   if keyBoardKey[pygame.K_S]:
    h-= speed
   if keyBoardKey[pygame.K_D]:
    w += speed
   if keyBoardKey{pygame.K_A]:
    w -= speed
    screen.fill(white)
  pygame.draw.circle(screen,(0,120,129),(100,100),50,4)
pygame.quit()
