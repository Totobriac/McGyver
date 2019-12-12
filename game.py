import pygame
from pygame.locals import *
from constants import *
from classes import *

pygame.init()

mac = Player()

window = pygame.display.set_mode((900, 900), RESIZABLE)
jeu = Level()
jeu.generate()
jeu.draw(window)






to_continue = True

while to_continue:
	for event in pygame.event.get():   
		if event.type == QUIT:     
			to_continue = False
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT:
				mac.deplacer('droite')

	# jeu.draw(window)
	window.blit(mac_pic,(mac.x,mac.y))
	pygame.display.flip()