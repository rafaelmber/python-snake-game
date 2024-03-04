import pygame
from controller import Controller
from input_handler import InputHandler

def main():
    pygame.init()

    screen_size = (500, 500)

    screen: pygame.Surface = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    game_controller = Controller(screen_size[0], screen_size[1], 20)
    input_handler = InputHandler()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # User Input Handler
        direction = input_handler.get_input()


        # Game controller update
        game_controller.update(direction)

        # Draw elements on the screen
        game_controller.draw(screen)

        # Update display
        pygame.display.flip()

        # Control the game speed
        clock.tick(10)

    pygame.quit()


if __name__ == '__main__':
    main()