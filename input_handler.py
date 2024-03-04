import pygame

class InputHandler:
    def __init__(self) -> None:
        pass
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return "LEFT"
        elif keys[pygame.K_RIGHT]:
            return "RIGHT"
        elif keys[pygame.K_UP]:
            return "UP"
        elif keys[pygame.K_DOWN]:
            return "DOWN"
        elif keys[pygame.K_ESCAPE]:
            return "ESCAPE"
        
        mouse = pygame.mouse.get_pressed()
        if mouse[0] == True:
            return 'LEFT_BUTTON', pygame.mouse.get_pos()
        
        return None



