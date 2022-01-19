import sys
import math
import os
from os import path
import random
import time
import pygame
pygame.mixer.init()

pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
COLORF = (255,204,128)

FPS = 80
CIASTKO_WIDTH, CIASTKO_HEIGHT = 60, 60
KUBEK_WIDTH, KUBEK_HEIGHT = 150 , 100
KAWA_WIDTH, KAWA_HEIGHT = 40, 50
KAWA1_WIDTH, KAWA1_HEIGHT = 40, 50 
KAWA2_WIDTH, KAWA2_HEIGHT = 40, 50 
KAWA3_WIDTH, KAWA3_HEIGHT = 40, 50 
ROCK_WIDTH , ROCK_HEIGHT = 50, 50

Vel = 4
Vel1 = 2
Vel2 = 3    
Vel3 = 6
Vel4 = 4

SCORE_FOFT = pygame.font.SysFont("Book Antiqua", 50)
GO_FONT = pygame.font.SysFont("Gill Sans", 60)
XD_FONT = pygame.font.SysFont("Book Antiqua", 70)


KUBEK_IMAGE = pygame.image.load(os.path.join('coffe rush','Assets','Kubeczek.png'))
KAWA_IMAGE = pygame.image.load(os.path.join('coffe rush','Assets','bean.png'))
ROCK_IMAGE = pygame.image.load(os.path.join('coffe rush','Assets','dwayne.png'))
CIASTKO_IMAGE = pygame.image.load(os.path.join('coffe rush','Assets','bitmap.png'))
KUBEK = pygame.transform.scale(KUBEK_IMAGE, (KUBEK_WIDTH, KUBEK_HEIGHT))
KAWA = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
KAWA1 = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
KAWA2 = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
KAWA3 = pygame.transform.scale(KAWA_IMAGE, (KAWA_WIDTH, KAWA_HEIGHT))
CIASTKO = pygame.transform.scale(CIASTKO_IMAGE, (CIASTKO_WIDTH, CIASTKO_HEIGHT))
ROCK = pygame.transform.scale(ROCK_IMAGE, (ROCK_WIDTH, ROCK_HEIGHT))
COLLECT_SOUND = pygame.mixer.Sound(os.path.join('coffe rush','Assets','collect.wav'))
LOSE_SOUND = pygame.mixer.Sound(os.path.join('coffe rush','Assets','lose.wav'))


score = 0
hscore = 0
health = 2



WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coffe Rush!")


def draw_window(kubek, kawa, kawa1, kawa2, score, kawa3, hscore, rock , health, ciastko):

    WIN.fill(COLORF)
    WIN.blit(KUBEK, (kubek.x, kubek.y))
    WIN.blit(KAWA, (kawa.x, kawa.y ) )
    WIN.blit(KAWA1, (kawa1.x, kawa1.y ) )
    WIN.blit(KAWA2, (kawa2.x, kawa2.y ) )
    WIN.blit(ROCK, (rock.x, rock.y ) )
    if score >= 100 and health <2:
        WIN.blit(CIASTKO, (ciastko.x, ciastko.y ) )
    if score > 100:
        WIN.blit(KAWA3, (kawa3.x, kawa3.y ) )
    score_text = SCORE_FOFT.render("Score: " + str(score), 1, BLACK)
    WIN.blit(score_text, (0,0))
    if score > hscore:
        hscore = score
    hscore_text = SCORE_FOFT.render("High Score: " + str(hscore), 1, BLACK)
    WIN.blit(hscore_text, (600,0))
    if score < 0 or health ==0:
        go_text2 = GO_FONT.render(" Kliknij SPACE, aby zacząć od nowa", 1, BLACK)

        go_text4 = GO_FONT.render("Kliknij ESC, aby wyjść do menu", 1, BLACK)

        WIN.blit(COFFEE1, (0,0))
        WIN.blit(go_text2, (WIDTH/2 -  go_text2.get_width()/2,850 - go_text2.get_height()/2))

        WIN.blit(go_text4, (WIDTH/2 -  go_text4.get_width()/2,950 - go_text4.get_height()/2))


        WIN.blit(hscore_text, (WIDTH/2 - hscore_text.get_width()/2,0))
    
    
    pygame.display.update()

COFFEE = pygame.transform.scale(pygame.image.load(os.path.join('coffe rush', 'Assets', 'Rush.png' )), (WIDTH, HEIGHT))
COFFEE1 = pygame.transform.scale(pygame.image.load(os.path.join('coffe rush', 'Assets', 'Coffee1.png' )), (WIDTH, HEIGHT))
COFFEE2 = pygame.transform.scale(pygame.image.load(os.path.join('coffe rush', 'Assets', 'bcg.png' )), (WIDTH, HEIGHT))
def draw_menu():
    WIN.blit(COFFEE, (0,0))
    menu_text = XD_FONT.render("Kliknij Space aby zacząć :)", 1, BLACK)
    WIN.blit(menu_text, (WIDTH/2 - menu_text.get_width()/2, HEIGHT/2 - menu_text.get_height()/2))
    pygame.display.update()

def menu():
    clock = pygame.time.Clock()
    runm = True
    while runm:
        pygame.time.delay(1)


        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runm = False

        draw_menu()
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_SPACE]:

            main()



def main():


    kubek = pygame.Rect(450, 900, KUBEK_WIDTH, KUBEK_HEIGHT)
    kawa = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    kawa1 = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    kawa2 = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    kawa3 = pygame.Rect(random.randint(20, 980),0, KAWA_WIDTH, KAWA_HEIGHT)
    rock = pygame.Rect(random.randint(20, 980),0, ROCK_WIDTH, ROCK_HEIGHT)
    ciastko = pygame.Rect(random.randint(20, 980),0, CIASTKO_WIDTH, CIASTKO_HEIGHT)

    score = 0 
    hscore = 0
    health = 2
    
    clock = pygame.time.Clock()
    
    run = True


    while run:

        
        pygame.time.delay(1)


        if kubek.colliderect(ciastko):
            COLLECT_SOUND.play()
            ciastko.y = random.randint(-5000, -3000)
            ciastko.x = random.randint(20, 980)
            health += 1 
            if score > hscore:
                hscore = score
        if kubek.colliderect(kawa):
            COLLECT_SOUND.play()
            kawa.y = (0)
            kawa.x = random.randint(20, 980)
            score += 5 
            if score > hscore:
                hscore = score
            
        if kubek.colliderect(kawa1):
            COLLECT_SOUND.play()
            kawa1.y = (0)
            kawa1.x = random.randint(20, 980)
            score += 5
            if score > hscore:
                hscore = score
        if kubek.colliderect(kawa2):
            COLLECT_SOUND.play()
            kawa2.y = (0)
            kawa2.x = random.randint(20, 980)
            score += 5
            if score > hscore:
                hscore = score
        if kubek.colliderect(kawa3):
            COLLECT_SOUND.play()
            kawa3.y = (0)
            kawa3.x = random.randint(20, 980)
            score += 10 
            if score > hscore:
                hscore = score
        if kubek.colliderect(rock):
            
            rock.y = (0)
            rock.x = random.randint(20, 980)
            health -= 1
            if score > hscore:
                hscore = score
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_a] and kubek.x - Vel3 > 0:
            kubek.x -= Vel3
        if keys_press[pygame.K_d] and kubek.x + Vel3 + KUBEK_WIDTH < 1000:
            kubek.x += Vel3

        if kawa.y + KAWA_HEIGHT >1000:

            kawa.y = 0
            kawa.x = random.randint(20, 980)
            score -= 10

        if kawa1.y + KAWA1_HEIGHT >1000:
            kawa1.y = 0
            kawa1.x = random.randint(20, 980)
            score -= 10
        if kawa2.y + KAWA1_HEIGHT >1000:
            kawa2.y = 0
            kawa2.x = random.randint(20, 980)
            score -= 10
        if kawa3.y + KAWA1_HEIGHT >1000:
            kawa3.y = 0
            kawa3.x = random.randint(20, 980)
            score -= 10
        if rock.y + ROCK_HEIGHT >1000:
            rock.y = 0
            rock.x = random.randint(20, 980)
        if ciastko.y + ROCK_HEIGHT >1000:
            ciastko.y = random.randint(-5000, -3000)
            ciastko.x = random.randint(20, 980)
   
        



            
        
        draw_window(kubek, kawa, kawa1, kawa2, score, kawa3, hscore, rock, health, ciastko)
        kawa.y += Vel1
        
        kawa1.y += Vel2
        
        kawa2.y += Vel
        
        rock.y += Vel3
        if score >= 100:
            kawa3.y +=Vel4
        if score >= 100 and health <2:
            ciastko.y += Vel4


        

        if score < 0 or health == 0:
            
            kawa.y = 0       
            kawa1.y = 0       
            kawa2.y = 0
            kawa3.y = 0 
            rock.y = 0 
            ciastko.y = 0  
            if keys_press[pygame.K_ESCAPE]:
                run = False
            if keys_press[pygame.K_SPACE]:
                if score > hscore:
                    hscore = score
                health = 2
                score = 0
                kawa.y += Vel1
        
                kawa1.y += Vel2
        
                kawa2.y += Vel

                rock.y += Vel3
                if score >= 100:
                    kawa3.y +=Vel4

                       
    pygame.quit
    


menu()

