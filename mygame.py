import pygame, sys
# Sys: Access to system functionality

pygame.init() # Starts Pygame Modules(sounds, graphics, etc)

screen = pygame.display.set_mode((400, 500)) #Width, Height of Window
# When run, window shown for breif time

clock = pygame.time.Clock() # Helps influence time (control fps)

test_surface = pygame.Surface((100, 200))   # Create Surface
test_surface.fill(pygame.Color("Blue")) # Set Color to Surface
test_rect1 = pygame.Rect(100, 200, 100, 100) # Create Rectangle
test_rect2 = test_surface.get_rect(center=(200, 250)) # Create Rect around Surface
# When run, surface is center, center position 200, 250

while True: # Main game loop to keep windown open and run each frame
    
    for event in pygame.event.get(): # Event loop tracking all actions
        if event.type == pygame.QUIT:    # Checks if X on window clicked 
            pygame.quit()   # Closes all Modules (opposite of pygame.init())
            sys.exit()  # Successfully exits code
    
    screen.fill((175, 215, 70)) # Set Colour to Display
    pygame.draw.rect(screen, pygame.Color("red"), test_rect1) # Update Rectangle on Display
    pygame.draw.ellipse(screen, pygame.Color("green"), test_rect1) # Different shape : Elipse
    test_rect2.right += 1   # Moves Rect one pixel right each interation
    screen.blit(test_surface, test_rect2)   # Update Surface on Display
    pygame.display.update() # Displays all elements
    clock.tick(60) # Set Fps



 
