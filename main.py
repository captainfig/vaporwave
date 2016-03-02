# import pygame module
import pygame, time, constants, player, plat

def createGame(display):
     # initialize pygame module
    pygame.init()
    # load and set logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Good Cop, Dad Cop")
    # create a surface on screen with size 240 x 180, white background
    display.fill((255, 255, 255))
    
def keyDown(event, player):
    # if key is pressed, do something
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.moveX(4, "left")
        if event.key == pygame.K_RIGHT:
            player.moveX(4, "right")
        if event.key == pygame.K_UP:
            player.moveY(7)

def keyUp(event, player):
    # if key is released, stop doing something    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            player.stop()
        if event.key == pygame.K_RIGHT:
            player.stop()

# define main function
def main():
    screen = pygame.display.set_mode((constants.SCR_WIDTH,constants.SCR_HEIGHT))
    createGame(screen)

    player_sprites = pygame.sprite.RenderPlain()
    platform_sprites = pygame.sprite.RenderPlain()
    # create sprite and add it sprite group
    face = player.Player(50, 0)
    player_sprites.add(face)
    
    
    for i in range(0,5):
        platpos = 0 + (i  * 32)
        platform = plat.Platform(300 + platpos, 500)
        platform_sprites.add(platform)
    
    # define variable for tick speed
    clock = pygame.time.Clock()
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # tick clock to keep constant framerate
        clock.tick(30)
        # event handling, gets all events from the event queue
        for event in pygame.event.get():
            keyDown(event, face)
            keyUp(event, face)
            # beark loop if game is quit
            if event.type == pygame.QUIT:
                # change the value to False, exiting the main loop
                running = False
        screen.fill((255, 255, 255)) # create blank screen for every frame
        player_sprites.update() # run update method of sprites in group
        platform_sprites.draw(screen)
        player_sprites.draw(screen) # draw updated sprites

        pygame.display.flip() # update the screen
        
    pygame.quit()

# run the main function only if this module is executed as the main script
if __name__=="__main__":
    # call the main function
    main()
