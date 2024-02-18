import pygame
from sys import exit
import random

def draw(Player,Player_R,bar_R,SPlayer,SPlayer_R):
    
    screen.blit(Player,Player_R)
    screen.blit(SPlayer,SPlayer_R)

    pygame.draw.rect(screen,"red",bar_R)
    
    pygame.display.update() 
    
def Remove_Shot(Shots,Shot,Shot_S,SShots,SShot):
    
    for Shot_R in Shots[:] :
            Shot_R.x += Shot_S
            screen.blit(Shot,Shot_R) 
            if Shot_R.x > S_W:
                Shots.remove(Shot_R) 
    
    for SShot_R in SShots[:] :
            SShot_R.x -= Shot_S
            screen.blit(SShot,SShot_R)
            if SShot_R.x < 0:
                SShots.remove(SShot_R)
    
def dm_green(Shots,PS_H): 
    for Shot_R in Shots[:] :
            if  Shot_R.colliderect(SPlayer_R):
                PS_H = True
                Shots.remove(Shot_R)
                print(PS_H)
                return PS_H
    pygame.display.update() 

def dm_blue(SShots,P_H): 
    for SShot_R in SShots[:] :
            if  SShot_R.colliderect(Player_R):
                P_H = True
                SShots.remove(SShot_R)
                print(P_H)
                return P_H
    pygame.display.update() 
            
def GAME_OVER( P_H_helth,PS_H_helth):         
        if PS_H_helth == 0 and P_H_helth > 0:
            game_over_text = FONT.render("Blue WIN",1,"red")
            screen.blit(game_over_text,(S_W/2 - game_over_text.get_width()/2 , S_H/2 - game_over_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            return True
       
        elif P_H_helth == 0 and PS_H_helth > 0:
            game_over_text = FONT.render("Green WIN",1,"red")
            screen.blit(game_over_text,(S_W/2 - game_over_text.get_width()/2 , S_H/2 - game_over_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            return True
          
        elif P_H_helth == 0 and PS_H_helth == 0:
            game_over_text = FONT.render("DRAW",1,"red")
            screen.blit(game_over_text,(S_W/2 - game_over_text.get_width()/2 , S_H/2 - game_over_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            return True

        else:
            return False
            
def Player_Movement(Player_R,Player_S,SPlayer_R):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and SPlayer_R.x > S_W/2:
            SPlayer_R.x -= Player_S
            
        if keys[pygame.K_RIGHT] and SPlayer_R.x < S_W - Player_W:
            SPlayer_R.x += Player_S
            
        if keys[pygame.K_UP] and SPlayer_R.y > 0:
            SPlayer_R.y -= Player_S
            
        if keys[pygame.K_DOWN] and SPlayer_R.y < S_H - Player_H:
            SPlayer_R.y += Player_S
            
            
        if keys[pygame.K_a] and Player_R.x > 0:
            Player_R.x -= Player_S
            
        if keys[pygame.K_d] and Player_R.x < S_W/2 - Player_W:
            Player_R.x += Player_S
            
        if keys[pygame.K_w] and Player_R.y > 0:
            Player_R.y -= Player_S
            
        if keys[pygame.K_s] and Player_R.y < S_H - Player_H:
            Player_R.y += Player_S
    
pygame.init()
FONT = pygame.font.SysFont("comicsans",30)
S_W = 800
S_H = 400
screen = pygame.display.set_mode((S_W,S_H))
clock = pygame.time.Clock()

# Player
Player_W = 50
Player_H = 50
Player_S = 5

Player = pygame.Surface((Player_W,Player_H))
Player_R = Player.get_rect(midbottom = (Player_W , S_H/2))
Player.fill("lightblue")

# Second Player
SPlayer = pygame.Surface((Player_W,Player_H))
SPlayer_R = Player.get_rect(midbottom = (S_W - Player_W , S_H/2))
SPlayer.fill("green")

# Shot
Shot_W = 15
Shot_H = 15
Shot_S = 10

Shot = pygame.Surface((Shot_W,Shot_H))
Shot.fill("lightblue")

SShot = pygame.Surface((Shot_W,Shot_H))
SShot.fill("green")

Shots = []
SShots = []
MAX_Shot = 3

bar_R = pygame.Rect(400,0,1,S_H)
PS_H_helth = 3

def main():
    P_H = False
    PS_H = False
    P_H_helth = 3
    PS_H_helth = 3
    run=True
    clock = pygame.time.Clock()
    
    while run:
        (clock.tick(60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f and len(Shots) < MAX_Shot:
                Shot_R = Shot.get_rect(center = (Player_R.x + Player_W/2 , Player_R.y + Player_H/2))
                Shots.append(Shot_R)
      
             
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and len(SShots) < MAX_Shot:
                SShot_R = SShot.get_rect(center = (SPlayer_R.x + Player_W/2 , SPlayer_R.y + Player_H/2))
                SShots.append(SShot_R)
                
        screen.fill("white")
        
        draw(Player,Player_R,bar_R,SPlayer,SPlayer_R)

        Player_Movement(Player_R,Player_S,SPlayer_R)
        
        Remove_Shot(Shots,Shot,Shot_S,SShots,SShot)
    
        if dm_blue(SShots,P_H):
            P_H_helth -= 1
            print(P_H_helth)

        if dm_green(Shots,PS_H):
            PS_H_helth -= 1
            print(PS_H_helth)
           
        if GAME_OVER( P_H_helth,PS_H_helth):
            break
               
    pygame.quit()
    
if __name__ == "__main__":
    main()