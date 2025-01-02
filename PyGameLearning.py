import pygame 


pygame.init() # IMPORTANT - Starts pygame and intiates all subparts of pygame 

# Colors 

RED = (255,0,0)
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

circle_x = 600
circle_y = 450



# importing images (Image Surface)

ground_image_surface = pygame.image.load('Resources/ground.jpg').convert()
sky_surface = pygame.image.load('Resources/sky.jpg').convert()  # making pictures easier for pygame to run program quicker.

# Creating Test > Create an image of text > Place on surface 
# Create Font > Write text on surface > Blit text 

test_font = pygame.font.Font(None,50) # font type & font size
text_surface = test_font.render('My PyGame', False, 'Green') # AA means smoothing edges of the text
text_rect = text_surface.get_rect(midbottom = (400, 50))

# Rectangles - Precise positioning of surfaces and basic collisions 

# Image information is placed on a surface > position information is placed in a rectangle. (Have to change both but there is also a sprite class)

player_surf = pygame.image.load('Resources/player.png').convert_alpha() # converts image but also gets rid of alpha particles (clear background)
player_surf = pygame.transform.scale(player_surf, (50,120))
player_rect = player_surf.get_rect(midbottom = (80,500)) # takes a surface anfd draws rectangle arouind it 

# tedious ^ Later sprite class 


# The Player Character
# 1. Keyboard input


# Gravity for player 
player_gravity = 0
jump = False


game_active = True
running = True 

while running: 
    for event in pygame.event.get(): # loops through all events in pygame (Should use this instead of inside the while running loop)
        if event.type == pygame.QUIT:
            running = False
        if game_active:
            if event.type == pygame.MOUSEMOTION: # when moving mouse
                print(event.pos) # obtaining mouse position
            
            if event.type == pygame.MOUSEBUTTONDOWN: # button pressed
                print("Mouse down")
                if(player_rect.collidepoint(event.pos)): # checks for collision on rectangle created within a specific point 
                    print("Collision!")
                    if(jump==False):
                        player_gravity = -20
                        jump = True

            if event.type == pygame.MOUSEBUTTONDOWN: # button pressed
                print("Mouse down")
            if event.type == pygame.MOUSEBUTTONUP: # button released
                print("Mouse down")
            if event.type == pygame.KEYDOWN: # button presses
                print("Key down")
                if event.key == pygame.K_SPACE:
                    print("Jump 2")
                    if(jump==False):
                        player_gravity = -20
                        jump = True
                if event.key == pygame.K_s:
                    game_active = False
            if event.type == pygame.KEYUP: # button releases
                print("Key Up")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        posx -= 5
    elif key[pygame.K_RIGHT]:
        posx += 5
    elif key[pygame.K_UP]:
        posy -= 5
    elif key[pygame.K_DOWN]:
        posy += 5 

    if game_active:
        # displaying images - surface 
        screen.blit(pygame.transform.scale(sky_surface, (800,500)), (0,0))
        screen.blit(pygame.transform.scale(ground_image_surface, (800,100)), (0, 500)) 
        screen.blit(test_surface, (posx, posy)) # blit = block image transfer fancy way of saying putting one surface on another
        # screen.blit(text_surface, (300, 50)) # text surface place
        pygame.draw.rect(screen, 'pink', text_rect, 10) # draw a rectangle with border
        pygame.draw.rect(screen, 'pink', text_rect) # draw a full rectangle 
        screen.blit(text_surface, text_rect) 

        if(circle_x<0):
            circle_x = 800
        else:
            circle_x -= 5
        pygame.draw.circle(screen, RED, (circle_x, circle_y), 50)


    #    player_rect.left += 1 # moving the player (Move rectangle NOT surface)



        player_gravity+=1
        player_rect.y += player_gravity
        if player_rect.bottom > 500:
            player_rect.bottom = 500
            jump = False
        screen.blit(player_surf, player_rect) # taking player surface and placing it in position of rectangle

        

    #    mouse_pos = pygame.mouse.get_pos()
    #    if player_rect.collidepoint((mouse_pos)):
    #        print(pygame.mouse.get_pressed())

        pygame.draw.line(screen, 'white', (0,600), (800,0), width=2)

        # pygame.draw.line(screen, 'Gold', (0,600), pygame.mouse.get_pos(), width=10) # get a line that follows your mouse 

        pygame.draw.ellipse(screen, 'brown', pygame.Rect(50, 200,100,100))  # creating a rectangle inside of a ellipse 

    
        # keyboard input 

    #    keys = pygame.key.get_pressed() # returns an array of 1's and zeros for which key was pressed 
    #    if keys[pygame.K_SPACE]:
    #        print("Jump")

        
    else:
        screen.fill('yellow')

        # entire game will run inside while true loop // also update everything
    pygame.display.update() # updates display suface
    clock.tick(60) # this while loop shouldn't run faster than 60 frames per second 
    


pygame.QUIT





# Controlling FRAME RATE 
 
# animation speed depends on how fast we are updating the game. 

# keep frame rate constant so that there is a fixed frame rate. 



