import pygame
import time

class PygameStrategy:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        print("pygame strategy has been initialized")
        print("note that the pygame strategy is intentionally slowed down...")

    def duty_cycle(self, channel, value):
        self.current_duty_cycle = value
        self.current_channel = channel
        self.render_color()

    def render_color(self):
        color_intensity = int((self.current_duty_cycle / 0xFFFF) * 255)
        if color_intensity > 0 and self.current_channel % 3 == 0:
            r, g, b = 0, color_intensity, 0
            print('green')
        elif color_intensity > 0 and self.current_channel % 3 == 1:
            r, g, b = color_intensity, 0, 0
            print('red')
        elif color_intensity > 0 and self.current_channel % 3 == 2:
            r, g, b = 0, 0, color_intensity
            print('blue')
        else:
            r, g, b = 0, 0, 0
            print('black')

        self.screen.fill((r, g, b))
        pygame.display.flip()

        time.sleep(1)  # Pause for 1 second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
