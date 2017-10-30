import pygame
from pygame import*
from pygame.locals import*
def main():
    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    screen.fill((255,255,255))
    pygame.display.set_caption("Main Menu")
    while True:
        screen.fill((255,255,255))
        Exit = pygame.draw.rect(screen,(0,155,0),(150,500,180,70))
        Play = pygame.draw.rect(screen,(155,0,0),(650,500,180,70))
        myfont = pygame.font.SysFont('Times New Roman',25)
        exittext = myfont.render('Exit',False,(0,0,0))
        screen.blit(exittext,(160,520))
        playfont = pygame.font.SysFont("Times New Roman", 25)
        playtext = playfont.render('Play', False, (0, 0, 0))
        screen.blit(playtext,(650, 520))
        titlefont = pygame.font.SysFont('Times New Roman',40)
        titletext = titlefont.render('Welcome to "Escape the snowflake army"',False,(0,0,0))
        screen.blit(titletext,(175,0))
        pygame.display.update()
        e = event.wait()
        if e.type == QUIT:
            exit()
        if Exit.collidepoint(mouse.get_pos()):
            red = pygame.draw.rect(screen,(255,0,0),(150,500,180,70))
            display.flip()
            red = pygame.draw.rect(screen,(255,0,0),(150,500,180,70))
            display.flip()

        if Play.collidepoint(mouse.get_pos()):
            green = pygame.draw.rect(screen,(0,255,0),(650,500,180,70))
            display.flip()
            green = pygame.draw.rect(screen,(0,255,0),(650,500,180,70))
            display.flip()

        pos = pygame.mouse.get_pos()
        (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
        if Exit.collidepoint(pos) and pressed1 ==1:
            if e.type == MOUSEBUTTONDOWN:
                exit()
        if Play.collidepoint(pos) and pressed1 == 1:
            if e.type == MOUSEBUTTONDOWN:
                import FinalProject
                FinalProject.fproject()
main()

