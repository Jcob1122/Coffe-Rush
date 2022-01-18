import sys
import math
import os
import random
import time
from telnetlib import GA
from tracemalloc import stop

import pygame

pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)


FPS = 80
KUBEK_WIDTH, KUBEK_HEIGHT = 120 , 100
KAWA_WIDTH, KAWA_HEIGHT = 40, 50
KAWA1_WIDTH, KAWA1_HEIGHT = 40, 50 
KAWA2_WIDTH, KAWA2_HEIGHT = 40, 50 
KAWA3_WIDTH, KAWA3_HEIGHT = 40, 50 

Vel = 4
Vel1 = 2
Vel2 = 3
Vel3 = 6
Vel4 = 4

SCORE_FOFT = pygame.font.SysFont("comicsans", 50)
GO_FONT = pygame.font.SysFont("comicsans", 100)


KUBEK_IMAGE = pygame.image.load(os.path.join('coffe rush','Assets','Kubeczek.png'))
KAWA_IMAGE = pygame.image.load(os.path.join('coffe rush','Assets','drawing.png'))
KUBEK = pygame.transform.scale(KUBEK_IMAGE, (KUBEK_WIDTH, KUBEK_HEIGHT))
KAWA = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
KAWA1 = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
KAWA2 = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
KAWA3 = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))


score = 0
hscore = 0



WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coffe Rush!")


def draw_window(kubek, kawa, kawa1, kawa2, score, kawa3, hscore ):

    WIN.fill(WHITE)
    WIN.blit(KUBEK, (kubek.x, kubek.y))
    WIN.blit(KAWA, (kawa.x, kawa.y ) )
    WIN.blit(KAWA1, (kawa1.x, kawa1.y ) )
    WIN.blit(KAWA2, (kawa2.x, kawa2.y ) )
    if score > 100:
        WIN.blit(KAWA3, (kawa3.x, kawa3.y ) )
    score_text = SCORE_FOFT.render("Score: " + str(score), 1, BLACK)
    WIN.blit(score_text, (0,0))
    if score > hscore:
        hscore = score
    hscore_text = SCORE_FOFT.render("High Score: " + str(hscore), 1, BLACK)
    WIN.blit(hscore_text, (600,0))
    if score < 0:
        go_text = GO_FONT.render("Game Over! ", 1, BLACK)
        go_text2 = GO_FONT.render(" Kliknij SPACE,", 1, BLACK)
        go_text3 = GO_FONT.render(" aby zacząc od nowa", 1, BLACK)
        WIN.fill(WHITE) 
        WIN.blit(go_text, (WIDTH/2 -  go_text.get_width()/2,HEIGHT/2 - go_text.get_height()/2))
        WIN.blit(go_text2, (WIDTH/2 -  go_text2.get_width()/2,600 - go_text2.get_height()/2))
        WIN.blit(go_text3, (WIDTH/2 -  go_text3.get_width()/2,800 - go_text3.get_height()/2)) 
        score_text = SCORE_FOFT.render("Score: " + str(score), 1, BLACK)
        WIN.blit(score_text, (0,0))
        WIN.blit(hscore_text, (600,0))
    
    
    pygame.display.update()

def main():

    kubek = pygame.Rect(450, 900, KUBEK_WIDTH, KUBEK_HEIGHT)
    kawa = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    kawa1 = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    kawa2 = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    kawa3 = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)

    score = 0
    hscore = 0
    
    clock = pygame.time.Clock()
    
    run = True
    while run:
        
        pygame.time.delay(1)
        if kubek.colliderect(kawa):
            kawa.y = (0)
            kawa.x = random.randint(20, 980)
            score += 5
            if score > hscore:
                hscore = score
        if kubek.colliderect(kawa1):
            kawa1.y = (0)
            kawa1.x = random.randint(20, 980)
            score += 5
            if score > hscore:
                hscore = score
        if kubek.colliderect(kawa2):
            kawa2.y = (0)
            kawa2.x = random.randint(20, 980)
            score += 5
            if score > hscore:
                hscore = score
        if kubek.colliderect(kawa3):
            kawa3.y = (0)
            kawa3.x = random.randint(20, 980)
            score += 10 
            if score > hscore:
                hscore = score
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_a] and kubek.x - Vel3 > 0:
            kubek.x -= Vel3
        if keys_press[pygame.K_d] and kubek.x + Vel3 + KUBEK_WIDTH < 1000:
            kubek.x += Vel3

        if kawa.y + KAWA_HEIGHT >1000:
            kawa.y = 0
            score -= 10

        if kawa1.y + KAWA1_HEIGHT >1000:
            kawa1.y = 0
            score -= 10
        if kawa2.y + KAWA1_HEIGHT >1000:
            kawa2.y = 0
            score -= 10
        if kawa3.y + KAWA1_HEIGHT >1000:
            kawa3.y = 0
            score -= 5
        
        
        draw_window(kubek, kawa, kawa1, kawa2, score, kawa3, hscore )
        kawa.y += Vel1
        
        kawa1.y += Vel2
        
        kawa2.y += Vel
        if score >= 100:
            kawa3.y +=Vel4
        if score < 0:
            kawa.y = 0       
            kawa1.y = 0       
            kawa2.y = 0
            kawa3.y = 0           
            if keys_press[pygame.K_SPACE]:
                if score > hscore:
                    hscore = score
                score = 0
                kawa.y += Vel1
        
                kawa1.y += Vel2
        
                kawa2.y += Vel
                if score >= 100:
                    kawa3.y +=Vel4
                       
    pygame.quit
    

if __name__ == "__main__":
    main()

