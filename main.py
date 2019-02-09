import pygame

#initialisation
pygame.init


#creation de la fenetre
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pokemon")

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.quit()
quit()
