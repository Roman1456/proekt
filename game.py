import pygame
from pygame import *
from Um_yum import Um_yum

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartunka/fon.jpg"),(700,500)
)

um_yum = Um_yum(50,50,100,100, "kartunka/download.jpg",10)





game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


    window.blit(backround, (0, 0))
    um_yum.move()
    um_yum.draw(window)
    pygame.display.flip()
    fps.tick(60)