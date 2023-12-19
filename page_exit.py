#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys
import custom_objects.buttons as buttons
import settings



btn_open =  pygame.sprite.Group()
btn_next = buttons.no_background(100,400,'Consolas',30,(0,0,0),(210,110,121),"Exit",exit)
btn_open.add(btn_next)
done = False

def display(window):
    pygame.display.set_caption("Thanks for Playing")
    while not done:
        window.fill((255,0,255))
        font = pygame.font.SysFont('Consolas', 30)
        window.blit(font.render("Thanks for Playing", True, (0, 0, 0)), (50, settings.WINDOW_HEIGHT/2))
        btn_open.draw(window)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            btn_next.update(pos,event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update() 
        settings.fpsClock.tick(settings.fps) 
        

