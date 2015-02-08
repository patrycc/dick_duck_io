import pygame
import os

felder = {
"feld1" : [0, 0, 200, 0, 200],
"feld2" : [1, 200, 400, 0, 200],
"feld3" : [2, 400, 600, 0, 200],
"feld4" : [3, 0, 200, 200, 400],
"feld5" : [4, 200, 400, 200, 400],
"feld6" : [5, 400, 600, 200, 400],
"feld7" : [6, 0, 200, 400, 600],
"feld8" : [7, 200, 400, 400, 600],
"feld9" : [8, 400, 600, 400, 600]
}

dicks = [0, 0, 0, 0, 0, 0, 0, 0, 0]

dran = 1

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def click_field(posi):
        x = posi[0]
        y = posi[1]

        for f in felder:
                a = felder[f]
                if x >= a[1] and x <= a[2] and y >= a[3] and y <= a[4] and dicks[a[0]] == 0:
                        dicks[a[0]] = dran
                        draw_dick(dran, screen)



def draw_dick(dran, screen):

        for f in felder:
                a = felder[f]
                if (dicks[a[0]] == 1):
                        screen.blit(get_image('dick.png'), (a[1], a[3]))
                elif (dicks[a[0]] == 2):
                        screen.blit(get_image('duck.png'), (a[1], a[3]))
        
def check_dick():
        if (dicks[0] == dran and dicks[1] == dran and dicks[2] == dran):
                return dran
        elif (dicks[3] == dran and dicks[4] == dran and dicks[5] == dran):
                return dran
        elif (dicks[6] == dran and dicks[7] == dran and dicks[8] == dran):
                return dran
        elif (dicks[0] == dran and dicks[3] == dran and dicks[6] == dran):
                return dran
        elif (dicks[1] == dran and dicks[4] == dran and dicks[7] == dran):
                return dran
        elif (dicks[2] == dran and dicks[5] == dran and dicks[8] == dran):
                return dran
        elif (dicks[0] == dran and dicks[4] == dran and dicks[8] == dran):
                return dran
        elif (dicks[2] == dran and dicks[4] == dran and dicks[6] == dran):
                return dran
        else:
                return 0


pygame.init()
screen = pygame.display.set_caption("Dick Duck Io [HOTSEAT EDITION]")
screen = pygame.display.set_mode((600, 600))

done = False
clock = pygame.time.Clock()

screen.blit(get_image('bg.png'), (0, 0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left click
                                print(event.pos)
                                click_field(event.pos)
                                print(check_dick())
                        if (dran == 1):
                                dran = 2
                        else:
                                dran = 1
        
        pygame.display.flip()
        clock.tick(60)    
                

