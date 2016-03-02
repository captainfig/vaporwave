import pygame

class Platform(pygame.sprite.Sprite):
    #constructor method that takes x, y position as parameters
    def __init__(self, x, y):
        # call parent constructor
        pygame.sprite.Sprite.__init__(self)
        # set image and rect
        self.image = pygame.image.load("platform.png")
        self.rect = self.image.get_rect()
        # set position
        self.rect.x = x
        self.rect.y = y
