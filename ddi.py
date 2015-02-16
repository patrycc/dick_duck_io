import pygame
import os

#felder contains information about the position of the different fields. first position is a key so it can be compared with dicks.
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

#represents the state of the different felders.
dicks = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#1 or 2, represents the players turn
dran = 1

#I was copying the following function from this site:
#http://www.nerdparadise.com/tech/python/pygame/basics/part2/
'''
If the image has been loaded already, then it returns the initialized image. If not, it does the initialization.
The beauty of this is that it is fast and it removes the clutter of initializing images at the beginning of key areas of your game logic.
You can also use it to centralize the abstraction of directory separators for different operating systems.
'''
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

#'click_field' gets handed over the click position, and then checks if the player can set on that field
#if win conditons are given (checked via calling 'check_dick'), set 'dicks' to display the winning screen
#if a player clicks on the 'again' io, then reset 'dicks'
#in the end, redraw display
def click_field(posi):
        global dicks
        global dran
        x = posi[0]
        y = posi[1]

        for f in felder:
                a = felder[f]
                if x >= a[1] and x <= a[2] and y >= a[3] and y <= a[4] and dicks[a[0]] == 0:
                        dicks[a[0]] = dran
                        if (check_dick() == 1 or check_dick() == 2):
                                dicks = [dran * 10, dran * 10, dran * 10, dran * 10, dran * 10, dran * 10, dran * 10, dran * 10, 3]
                        set_dran()
                elif x >= a[1] and x <= a[2] and y >= a[3] and y <= a[4] and dicks[a[0]] == 3:
                        dicks = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        dran = 0
                        set_dran()
                draw_dick()

#set next players id 
def set_dran():
        global dran
        if (dran == 1):
                dran = 2
        elif (dran == 2):
                dran = 1
        elif (dran == 0):
                dran = 1

# redraws the display
# loops through the felder items and checks if the according dicks meet a certain id to display an image
def draw_dick():
        global dicks
        screen.fill((0, 0, 0))
        screen.blit(get_image('img/bg.png'), (0, 0))
        for f in felder:
                a = felder[f]
                if (dicks[a[0]] == 1):
                        screen.blit(get_image('img/dick.png'), (a[1], a[3]))
                elif (dicks[a[0]] == 2):
                        screen.blit(get_image('img/duck.png'), (a[1], a[3]))
                elif (dicks[a[0]] == 10):
                        screen.blit(get_image('img/dick_win.png'), (a[1], a[3]))
                elif (dicks[a[0]] == 20):
                        screen.blit(get_image('img/duck_win.png'), (a[1], a[3]))
                elif (dicks[a[0]] == 3):
                        screen.blit(get_image('img/io.png'), (a[1], a[3]))
                        
#this function checks if win conditions set. then give back the current players id.
def check_dick():
        global dicks
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
#check if the last field is currently 'play again'
        elif (dicks[8] == 3):
                return 3
        else:
                return 0

#initialize pygame and screen
pygame.init()
screen = pygame.display.set_caption("Dick Duck Io [HOTSEAT EDITION] v1.0.0")
screen = pygame.display.set_icon(get_image('img/dick.ico') )
screen = pygame.display.set_mode((600, 600))
screen.blit(get_image('img/bg.png'), (0, 0))

done = False

#main loop
while not done:
        #event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left click
                                click_field(event.pos)
        
        pygame.display.flip()   
                

