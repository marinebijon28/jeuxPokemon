import pygame
from pygame.locals import *

white = 255, 255, 255

#initialisation
pygame.init()


#creation de la fenetre
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pokemon")

#affichage du menu
font = pygame.font.Font(None, 36)
text = font.render("Nouvelle partie", True, white)
textpos = text.get_rect()
textpos.centerx = window.get_rect().centerx
textpos.centery = window.get_rect().centery
window.blit(text, textpos)

window.blit(window, (0, 0))
pygame.display.flip()

#boucle infinie
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
pygame.quit()
quit()
