#Name:M. Dusome
#Date: Dec 11 2023
#Main Game Screen
import pygame,sys
from custom_objects.static import stillimage
from custom_objects.background import Background
import custom_objects.buttons as buttons
import settings
from custom_objects.player import Player


# Sprint Setup
Player_group = pygame.sprite.Group()
toolbar_group = pygame.sprite.Group()
lifeline_group = pygame.sprite.Group()
#Button Methods
def exit_prg():
    global done
    done=True

font = pygame.font.Font('fonts/gamefont.ttf', 20)
font2 = pygame.font.Font('fonts/gamefont.ttf', 25)

#All the buttons for this page
inv1 = stillimage(550,715,75,75,"toolbar/empty_invslot.png")
inv2 = stillimage(700,715,75,75,"toolbar/empty_invslot.png")
inv3 = stillimage(850,715,75,75,"toolbar/empty_invslot.png")
toolbar = stillimage(0,0,1000,800,"toolbar/toolbar.png")
heart = stillimage(0,703,30,30,"images/heart.png")
stam_bolt = stillimage(5,735,20,25,"images/stamina_logo.png")
ragelogo = stillimage(0,763,30,30,"images/ragelogo.png")
goldcoins = stillimage(130,730,40,40,"images/goldcoin.png")
Playerguy= Player(100,100,100,100,"images/redbox.jpg",2)
Player_group.add(Playerguy)
toolbar_group.add(toolbar,inv1,inv2,inv3)
lifeline_group.add(heart,stam_bolt,ragelogo,goldcoins)


health = 100
stamina = 50
rage = 0
coins = 0


def output(window):
    window.fill((255,255,255))
    Player_group.draw(window)
    toolbar_group.draw(window)
    lifeline_group.draw(window)
    window.blit(font.render(f"{health}/100", True, (255, 0, 0)), (35, 705))
    window.blit(font.render(f"{stamina}/50", True, (52,164,235)), (35, 733))
    window.blit(font.render(f"{rage}/100", True, (227,95,18)), (35, 763))
    window.blit(font2.render(f"{coins}", True, (255, 213, 0)), (170, 732))
done = False
def display(window):  
    pygame.display.set_caption("Dreadside")
    while not done:
        output(window)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        output(window)
        Playerguy.move()
        if Playerguy.check_hit(toolbar_group):
            Playerguy.back()
    
        
        pygame.display.update() 
        settings.fpsClock.tick(settings.fps) 