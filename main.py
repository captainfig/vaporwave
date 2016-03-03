# import pygame module
import pygame, time, constants, player, plat

pygame.init()
screen = pygame.display.set_mode((constants.SCR_WIDTH,constants.SCR_HEIGHT))

class Menu():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('courier', 32)
        self.color = (0, 0, 0)
        self.titleScreen = pygame.image.load("titlescreen.png")
        self.directions = self.font.render("Press Any Key", 1, self.color)
        self.running = True

    def run(self):
        running = True
        createGame(screen)
        
        while self.running:
            screen.blit(self.titleScreen, (0, 0))
            screen.blit(self.directions, (190, 335))
            
            pygame.display.update()

            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP:
                    main()
            

def createGame(display):
    # load and set logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Good Cop, Dad Cop")
    # create a surface on screen with size 240 x 180, white background
    display.fill((255, 255, 255))
    
def keyDown(event, player):
    # if key is pressed, do something
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            player.moveLeft()
            player.image = pygame.image.load("goodcopflip.png")
        if event.key == pygame.K_d:
            player.image = pygame.image.load("goodcop.png")
            player.moveRight()
        if event.key == pygame.K_SPACE:
            player.jump()

def keyUp(event, player):
    # if key is released, stop doing something    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            player.stop()
        if event.key == pygame.K_d:
            player.stop()

# define main function
def main():
    createGame(screen)

    player_sprites = pygame.sprite.RenderPlain()
    platform_sprites = pygame.sprite.RenderPlain()
    active_sprites = pygame.sprite.RenderPlain()
    # create sprite and add it sprite group
    face = player.Player(50, 0)
    player_sprites.add(face)
    active_sprites.add(face)
    
    # generate platforms
    for i in range(0,4):
        platpos = 0 + (i  * 24)
        platform = plat.Platform(0, constants.SCR_HEIGHT - platpos)
        platform_sprites.add(platform)

    for i in range(0, 3):
        platpos = 0 + (i  * 32)
        platform = plat.Platform(100 + platpos, constants.SCR_HEIGHT - 72)
        platform_sprites.add(platform)

    face.walls = platform_sprites # give player class wall list for collision
    
    # define variable for tick speed
    clock = pygame.time.Clock()
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        
        for event in pygame.event.get():
            keyDown(event, face)
            keyUp(event, face)
            # break loop if game is quit
            if event.type == pygame.QUIT:
                running = False
                
                
        active_sprites.update() # run update method of sprites in group

        #Draw Everything
        screen.fill((255, 255, 255)) # create blank screen for every frame
        platform_sprites.draw(screen)
        active_sprites.draw(screen) # draw updated sprites

        pygame.display.flip() # update the screen

        # tick clock to keep constant framerate
        clock.tick(60)
    menu.running = False
    pygame.quit()

# run the main function only if this module is executed as the main script
if __name__=="__main__":
    # call the main function
    menu = Menu()
    menu.run()
    pygame.quit()
