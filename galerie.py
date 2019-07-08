#!/usr/bin/env python3

from choix_imprimante import printer
from choix_repertoire import directory
import os
import glob
import pygame
from pygame.locals import KEYDOWN, K_a, K_p, K_q, K_i, K_SPACE, K_ESCAPE, K_RIGHT, K_LEFT
import subprocess

def diaporama():
    def show_fond(image):
        screen.fill( (80,80,80))
        for (lettre, factor) in (("A", 225),("P", 1500),):
            screen.blit(
                pygame.transform.scale(
                    pygame.image.load(os.path.join(lettres_path, "%s.jpg" % lettre)).convert(),
                    (100, 100)
                ),
                (factor,
                (monitor_v-100)/2)
            )
        # for
        
        img = pygame.image.load(image)
        img = img.convert() 
        img = pygame.transform.scale(img, (900,600))
        screen.blit(img,((monitor_h-900)/2,(monitor_v-600)/2))
        pygame.display.flip()
    # show_fond
    
    imprimante=printer()

    file_path = str(os.path.dirname(os.path.abspath(__file__))+'/')
    lettres_path=file_path+"Lettres/"
    media_path=directory()
    if not media_path: return
    media_path=os.path.join(media_path,'')
    
    montages=sorted( glob.glob(media_path+ "*.jpg"))
    number_files = len(montages)
    if number_files ==0: return

    pygame.init()
    monitor_h, monitor_v = pygame.display.Info().current_w, pygame.display.Info().current_h
    pygame.mouse.set_visible(False) 
    pygame.display.set_mode((monitor_h, monitor_v))
    screen = pygame.display.get_surface()
    pygame.display.set_caption('Galerie photos')

    pygame.display.toggle_fullscreen()

    nb=0    
    show_fond(montages[nb])    
    pygame.event.clear()
    while True:
        event=pygame.event.wait()
        if event.type == KEYDOWN:
            #if event.key == K_i: subprocess.call('lp -d Canon_SELPHY_CP1300_USB '+montages[nb], shell = True)
            if event.key == K_i and imprimante: subprocess.call('lp -d '+imprimante+' '+montages[nb], shell = True)
            if event.key in (K_q, K_SPACE, K_ESCAPE): break
            if event.key in (K_p, K_RIGHT):
                nb=(nb + 1) % number_files
                show_fond(montages[nb])
            # if
            if event.key in (K_a, K_LEFT):
                nb=(nb - 1) % number_files
                show_fond(montages[nb])
            # if
        # if
    # while
    pygame.event.clear()
    pygame.quit()
# diaporama

if __name__ == "__main__":
    diaporama()
# if
