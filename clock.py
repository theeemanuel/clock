from math import sqrt
import pygame
pygame.init()

WIDTH = 600
HEIGHT = 400

win = pygame.display.set_mode((600, 400))
win.fill((255,255,255))
pygame.display.set_caption("CLOCK")
clock = pygame.time.Clock()

h = 300
k = 200

secondx = 300
secondradius = 150
secondleft = False
secondright = True
seconds = 0
secondquarter = 0

minutex = 300
minuteradius = 120
minuteleft = False
minuteright = True
minutesign = 1
minutes = 0
minutequarter = 0

hourx = 300
hourradius = 90
hourleft = False
hourright = True
hoursign = 1
hours = 0

tiktok = (4*secondradius)/60

while True:
    clock.tick(tiktok)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if secondx == (h + secondradius):
        secondleft = True
        secondright = False   
    elif secondx == (h - secondradius):
        secondleft = False
        secondright = True

    if secondleft == True:
        secondy = int(k + (sqrt((secondradius**2)-((secondx-h)**2))))
        secondx -= 1
        seconds += 1
    elif secondright == True:
        secondy = int(k - (sqrt((secondradius**2)-((secondx-h)**2))))
        secondx += 1
        seconds += 1

    if seconds == ((secondradius*60)/minuteradius):
        minutex += minutesign
        minutes += 1
        secondquarter += 1
        seconds = 0
    if secondquarter == ((4*secondradius)/((secondradius*60)/minuteradius)):
        pygame.draw.circle(win, (255,255,255), (h, k), secondradius+12, 24)
        secondquarter = 0

    if minutex == (h + minuteradius):
        minuteleft = True
        minuteright = False
        minutesign = -1
    elif minutex == (h - minuteradius):
        minuteleft = False
        minuteright = True
        minutesign = 1

    if minuteleft == True:
        minutey = int(k + (sqrt((minuteradius**2)-((minutex-h)**2))))                                  
    elif minuteright == True:
        minutey = int(k - (sqrt((minuteradius**2)-((minutex-h)**2))))

    if minutes == ((minuteradius*12)/hourradius):
        hourx += hoursign
        hours += 1
        minutequarter += 1
        minutes = 0
    if minutequarter == ((4*minuteradius)/((minuteradius*12)/hourradius)):
        pygame.draw.circle(win, (255,255,255), (h, k), minuteradius+12, 24)
        minutequarter = 0

    if hourx == (h + hourradius):
        hourleft = True
        hourright = False
        hoursign = -1
    elif hourx == (h - hourradius):
        hourleft = False
        hourright = True
        hoursign = 1

    if hourleft == True:
        houry = int(k + (sqrt((hourradius**2)-((hourx-h)**2))))
    elif hourright == True:
        houry = int(k - (sqrt((hourradius**2)-((hourx-h)**2))))

    if hours == 360:
        pygame.draw.circle(win, (255,255,255), (h, k), hourradius+12, 24)
        hours = 0

    #print(secondx,"   ",minutex,"   ",hourx)
    pygame.draw.circle(win, (255,192,203), (secondx, secondy), 10)
    pygame.draw.circle(win, (128,0,128), (minutex, minutey), 10)
    pygame.draw.circle(win, (0,255,0), (hourx, houry), 10)
    pygame.display.update()

    
