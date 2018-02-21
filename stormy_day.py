4# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
DARK_WHITE = (200,200,200)
GREEN = (0, 100, 0)
DARK_GRAY = (175,175,175)
CYAN = (25, 75, 100)
PURPLE = (50,50,75)
DARK_PURPLE = (35,35,50)
LIGHT_BLUE = (75, 200, 255)
BLUE = (75, 125, 200)
night = 0

# Cloud Parameters
num_cloud = 50
cloudy = 1
clouds = []

# Cloud Parameters 2
num_cloud2 = 50
clouds2 = []

#Umbrella Parameters
VEL = [0,0]
x_u = SIZE[0]/2
y_u = SIZE[1]/2
umbrella_day_1 = pygame.image.load('umbrella_day_1.png')
umbrella_day_2 = pygame.image.load('umbrella_day_2.png')
umbrella_night_1 = pygame.image.load('umbrella_night_1.png')
umbrella_night_2 = pygame.image.load('umbrella_night_2.png')

# Rain Parameters
num_rain = 250
rains = 1
flash = 0
lightningy = 1
rain = []
lightning_sound = pygame.mixer.Sound("thunder.wav")
pygame.mixer.music.load('rain_sounds.wav')
pygame.mixer.music.play(-1)

# Generates Clouds
for i in range(num_cloud):
    x = random.randrange(-100,900)
    y = random.randrange(-125,125)
    
    location = [x, y]
    clouds.append(location)

# Generates Clouds2
for i in range(num_cloud2):
    x = random.randrange(-100,900)
    y = random.randrange(-125,250)
    
    location2 = [x, y]
    clouds2.append(location2)

# Generates Rain
for i in range(num_rain):
    x = random.randrange(-100,1000)
    y = random.randrange(-500,50)
    
    location = [x, y]
    rain.append(location)

def draw_cloud(location):
    x = location[0]
    y = location[1]
    
    pygame.draw.ellipse(screen, DARK_GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARK_GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARK_GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DARK_GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DARK_GRAY, [x + 20, y + 20, 60, 40])

def umbrella(x_u,y_u):
    if rains > 0:
        if night == 0:
            if VEL[0] > 0:
                screen.blit(umbrella_day_2, (x_u,y_u))
            else:
                screen.blit(umbrella_day_1, (x_u,y_u))
        else:
            if VEL[0] > 0:
                screen.blit(umbrella_night_2, (x_u,y_u))
            else:
                screen.blit(umbrella_night_1, (x_u,y_u))

def draw_cloud2(location):
    x = location[0]
    y = location[1]
    
    pygame.draw.ellipse(screen, DARK_WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARK_WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARK_WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DARK_WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DARK_WHITE, [x + 20, y + 20, 60, 40])
    
def rainy(location):
    x = location[0]
    y = location[1]

    pygame.draw.circle(screen, LIGHT_BLUE, (x,y), 3)
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if night == 0:
                    night = 1
                else:
                    night = 0
                    
            if event.key == pygame.K_RIGHT:
                if VEL[0] == -3:
                    VEL[0] = 0
                else:
                    VEL[0] = 3
                VEL[1] = 0
                
            if event.key == pygame.K_LEFT:
                if VEL[0] == 3:
                    VEL[0] = 0
                else:
                    VEL[0] = -3
                VEL[1] = 0
                
            if event.key == pygame.K_UP:
                if VEL[1] == 3:
                    VEL[1] = 0
                else:
                    VEL[1] = -3
                VEL[0] = 0
                
            if event.key == pygame.K_DOWN:
                if VEL[1] == -3:
                    VEL[1] = 0
                else:
                    VEL[1] = 3
                VEL[0] = 0
                
            if event.key == pygame.K_l and lightningy > 0:
                pygame.mixer.Sound.play(lightning_sound)
                flash = 5
            if event.key == pygame.K_r:
                if rains > 0:
                    rains = 0
                    lightningy = 0
                    pygame.mixer.music.pause()
                else:
                    rains = 1
                    lightningy = 1
                    pygame.mixer.music.unpause()

    # Game logic
    if lightningy > 0:
        if random.randint(0,150) == 150:
            pygame.mixer.Sound.play(lightning_sound)
            flash = 5
        else:
            flash -= 1
    
    for c in clouds:
        c[0] -= 3

        if c[0] < -100:
            c[0] = 900
            c[1] = random.randrange(-125,125)
        
    for c2 in clouds2:
        c2[0] -= 1

        if c2[0] < -100:
            c2[0] = 900
            c2[1] = random.randrange(-100,250)

    for r in rain:
        r[0] -= 2
        r[1] += 5

        if r[1] > 400:
            if random.randint(0,10) == 10 or r[1] > 600:
                r[0] = random.randrange(0,1000)
                r[1] = random.randrange(-500,50)

    if VEL[0] != 0:
        x_u += VEL[0]
    if VEL[1] != 0:
        y_u += VEL[1]
            
    # Drawing code
    ''' sky '''
    if rains:        
        if night == 0:
            if flash <= 0:
                screen.fill(CYAN)
            else:
                screen.fill(DARK_WHITE)
        else:
            if flash <= 0:
                screen.fill(DARK_PURPLE)
            else:
                screen.fill(DARK_WHITE)
    else:
        if night == 0:
            screen.fill(BLUE)
        else:
            screen.fill(PURPLE)

    ''' umbrella '''
    umbrella(x_u,y_u)

    if x_u < -100:
            x_u = 800
    if x_u > 800:
        x_u = -100
        
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, DARK_WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, DARK_WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, DARK_WHITE, [0, 410], [800, 410], 5)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    ''' rain '''
    for r in rain:
        if rains > 0:            
            rainy(r)

    ''' clouds2 '''
    for c2 in clouds2:
        draw_cloud2(c2)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
