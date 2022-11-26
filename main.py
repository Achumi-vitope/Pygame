import pygame, sys
from pygame.locals import *
from pygame import mixer
import random


def display_score():
    score = pygame.time.get_ticks()
    score = score - final_score
    score_text = pygame.font.Font(None,40)
    score_count = score_text.render(f'{score}',False,'white')
    screen.blit(score_count,(0,0))

pygame.init()
FPS = 60
clock = pygame.time.Clock()
width = 1900
height = 1000
ground = 900
game_active = True
final_score = 0
settled = 0

#sounds
jump = mixer.Sound('jump.mp3')
over = mixer.Sound('game_over.mp3')
playing = mixer.Sound('playing.mp3')
win = mixer.Sound('win.mp3')
volume = mixer.music.set_volume(0.2)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Destroyer")
font = pygame.font.Font('title.ttf', 100)
text = font.render('LGBTQ+ President Destroyer', True,'white')
winner = font.render('You Win!', True, 'white')

re_font = pygame.font.Font(None,40)
restart = re_font.render('Restart Game?\n Press \'ESC\' to continue!', True, 'white')


#positions 
zavung_x = 1800-120
zavung_y = 900
text_x = 1800/4
text_y = 60
background_x = background_y = 0
main_x = 100
main_y = 900
cloud1_x = 0
cloud1_y = 400
cloud2_x = 1800
cloud2_y = 300
cage_x = 1800/2
cage_y = 10

magic_x = 1800-130
magic_y = 900


#objects and characters
zavung = pygame.image.load('zavung.png').convert_alpha()
zavung_rect = zavung.get_rect(bottomleft= (zavung_x, zavung_y))

main = pygame.image.load('main.png').convert_alpha()
main_rect = main.get_rect(bottomleft= (main_x, main_y))
main_gravity = 0

background = pygame.image.load('bg.png').convert_alpha()
cloud1 = pygame.image.load('cloud1.png').convert_alpha()
cloud2 = pygame.image.load('cloud2.png').convert_alpha()
magic = pygame.image.load('magic.png').convert_alpha()
magic_rect = magic.get_rect(topright = (magic_x, magic_y))

cage = pygame.image.load('cage.png').convert_alpha()
cage_rect = cage.get_rect(midtop = (cage_x, cage_y))




while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #main char movement
    if events.type == pygame.KEYDOWN:
        if events.key == K_LEFT:
            main_rect.x -=10
            if main_rect.x <= 0:
                main_rect.x = 0
        if events.key == K_RIGHT:
            main_rect.x +=10
            if main_rect.x >= 1900:
                main_rect.x = 1900
        #jump
        if events.key == K_UP and main_rect.bottom == 900:
            main_gravity = -20
            jump.play()
        
            
        #game restart
        if events.key == K_ESCAPE:
            game_active = True
            final_score = pygame.time.get_ticks()
            
    #Cloud Movements
    #Right and left
    cloud_speed = random.randint(5,8)
    cloud1_x += cloud_speed
    cloud2_x -= cloud_speed
    if cloud1_x > 1900:
        speed = 0
        cloud1_x = 0
        cloud1_y = random.randint(200,500)
    if cloud2_x < 0:
        speed = 0
        cloud2_x = 1800
        cloud2_y = random.randint(100,400)
    
    
    #cage spawn
    cage_x_pos = random.randint(10, 1700)
    cage_rect.y += 40
    if cage_rect.y > 900:
        cage_rect.y = 0
        cage_rect.x = cage_x_pos
        
    #magic spawn

        
    game_over = font.render('Game Over',False, 'white')
    
    #placements
    if game_active:
        playing.play()
        screen.blit(background,(background_x, background_y))
        screen.blit(text,(text_x,text_y))
        screen.blit(zavung,zavung_rect)
        
        main_gravity += 1
        main_rect.y += main_gravity
        if main_rect.bottom >= ground:
            main_rect.bottom = ground
        screen.blit(main,main_rect)
        
        screen.blit(cloud1,(cloud1_x,cloud1_y))
        screen.blit(cloud2,(cloud2_x, cloud2_y))
        screen.blit(cage, cage_rect)
        
        
        magic_rect.x -= 10
        magic_rect.y = 800
        if magic_rect.x < 10:
            magic_rect.x = 1800
        screen.blit(magic, magic_rect)
        
        display_score()
        
        
        
        #win
        if main_rect.colliderect(zavung_rect):
            playing.stop()
            win.play()
            game_active = False
            screen.blit(background,(background_x, background_y))
            screen.blit(winner,(800, 100))
            screen.blit(restart,(750, 300))
            settle_score = pygame.font.Font(None,40)
            settled = pygame.time.get_ticks() - final_score
            settle = settle_score.render(f'Your Score = {settled}',False, 'white')
            screen.blit(settle,(700,500))
            main_rect.x = 0
        
        #Game over 
        if magic_rect.colliderect(main_rect):
            playing.stop()
            over.play()
            game_active = False
            screen.blit(background,(background_x, background_y))
            screen.blit(game_over,(800, 100))
            screen.blit(restart,(750, 300))
            settle_score = pygame.font.Font(None,40)
            settled = pygame.time.get_ticks() - final_score
            settle = settle_score.render(f'Your Score = {settled}',False, 'white')
            screen.blit(settle,(700,500))
            main_rect.x = 0
        
        if main_rect.colliderect(cage_rect):
            playing.stop()
            over.play()
            game_active = False
            screen.blit(background,(background_x, background_y))
            screen.blit(game_over,(800, 100))
            screen.blit(restart,(750, 300))
            settle_score = pygame.font.Font(None,40)
            settled = pygame.time.get_ticks() - final_score
            settle = settle_score.render(f'Your Score = {settled}',False, 'white')
            screen.blit(settle,(700,500))
            main_rect.x = 0
            
    pygame.display.update()
    clock.tick(FPS)
