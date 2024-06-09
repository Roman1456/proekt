import pygame
from pygame import *
from Um_yum import Um_yum
from Сandies import Сandies

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartunka/fon.jpg"),(700,500)
)

um_yum = Um_yum(280,360,100,100, "kartunka/player.png",10)

candies1 = []
candies1.append(Сandies(50,50,100,50,"kartunka/candies.png",5))


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


    window.blit(backround, (0, 0))
    for candies in candies1:
        candies.draw(window)
        candies.move()

        um_yum.move()
        um_yum.draw(window)

    if um_yum.hitbox.colliderect(candies.hitbox):
        pygame.display.flip()



    pygame.display.flip()
    fps.tick(60)