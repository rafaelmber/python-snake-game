import pygame

class View:
    def __init__(self) -> None:
        pass

    def draw(self, screen: pygame.Surface, score: int):
        window_size = screen.get_size()

        screen.fill((0,0,0,0.2))

        font = pygame.font.Font(None, 32)
        text = f'You lose, Score: {score}'
        text_surface = font.render(text, True, (255, 255, 255))

        text_xcord = (window_size[0] - text_surface.get_width()) // 2
        text_ycord = (window_size[1] - text_surface.get_height()) // 2

        screen.blit(text_surface, (text_xcord, text_ycord))

        text_esc = 'press ESC to exit'
        text_esc_surface = font.render(text_esc, True, (255, 255, 255))

        screen.blit(text_esc_surface, (text_xcord, window_size[1]- 50))