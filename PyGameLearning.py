import pygame 


pygame.init() # IMPORTANT - Starts pygame and intiates all subparts of pygame 

# creating a window (display surface)

width = 800
height = 600

screen = pygame.display.set_mode((width,height)) 
pygame.display.set_caption('TESTING PYGAME')

clock = pygame.time.Clock() # controlling frame rate 

surface_width = 100
surface_height = 200
posx = 200
posy = 100

# Plane Color Surface

test_surface = pygame.Surface((surface_width, surface_height)) # creates a surface 
test_surface.fill('White')

# importing images (Image Surface)

ground_image_surface = pygame.image.load('Resources/ground.jpg')
sky_surface = pygame.image.load('Resources/sky.jpg')

# Creating Test > Create an image of text > Place on surface 
# Create Font > Write text on surface > Blit text 

test_font = pygame.font.Font(None,50) # font type & font size
text_surface = test_font.render('My PyGame', False, 'Green') # AA means smoothing edges of the text

running = True 

while running:
    for event in pygame.event.get(): # loops through all events in pygame
        if event.type == pygame.QUIT:
            running = False
        

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        posx += 5

    # displaying images - surface 
    screen.blit(pygame.transform.scale(sky_surface, (800,500)), (0,0))
    screen.blit(pygame.transform.scale(ground_image_surface, (800,100)), (0, 500)) 
    screen.blit(test_surface, (posx, posy)) # blit = block image transfer fancy way of saying putting one surface on another
    screen.blit(text_surface, (300, 50))



    
    # entire game will run inside while true loop // also update everything
    pygame.display.update() # updates display suface
    clock.tick(60) # this while loop shouldn't run faster than 60 frames per second 
 
pygame.QUIT





# Controlling FRAME RATE 
 
# animation speed depends on how fast we are updating the game. 

# keep frame rate constant so that there is a fixed frame rate. 



