# import pygame module
import pygame, time, player

# define main function
def main():

    # initialize pygame module
    pygame.init()
    # load and set logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen with size 240 x 180
    screen = pygame.display.set_mode((240,180))
    screen.fill((255, 255, 255))

    # create sprite and sprite group
    face = player.Player(50, 0)
    player_sprites = pygame.sprite.RenderPlain((face))
    

    pygame.display.flip()
    
    
    clock = pygame.time.Clock()
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        clock.tick(30)
        # event handling, gets all events from the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    face.moveX(2, "left")
                if event.key == pygame.K_RIGHT:
                    face.moveX(2, "right")
                if event.key == pygame.K_UP:
                    face.moveY(5)
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    face.stop()
                if event.key == pygame.K_RIGHT:
                    face.stop()
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, exiting the main loop
                running = False
                pygame.quit()

        screen.fill((255, 255, 255))
        player_sprites.update()
        player_sprites.draw(screen)
        
        pygame.display.update()

# run the main function only if this module is executed as the main script
if __name__=="__main__":
    # call the main function
    main()
