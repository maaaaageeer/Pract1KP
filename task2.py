import pygame
import numpy as np

# Размеры окна
WIDTH = 900
HEIGHT = 700
BACKGROUND_COLOR = (240, 240, 240)
LINE_COLOR_1 = (0, 128, 255)
LINE_COLOR_2 = (128, 255, 0)
CIRCLE_COLOR = (255, 0, 128)
TEXT_COLOR = (0, 0, 0)
FONT_SIZE = 30


def draw_shapes(surface, center_position):
    pygame.draw.circle(surface, CIRCLE_COLOR, (int(center_position[0]), int(center_position[1])), 60, 3)
    pygame.draw.line(surface, LINE_COLOR_1, 
                     (center_position[0] - 150, center_position[1] - 150), 
                     (center_position[0] + 150, center_position[1] + 150), 4)
    pygame.draw.line(surface, LINE_COLOR_2, 
                     (center_position[0] + 150, center_position[1] - 150), 
                     (center_position[0] - 150, center_position[1] + 150), 4)

    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("Фигуры", True, TEXT_COLOR)
    surface.blit(text, (center_position[0] - 50, center_position[1] + 80))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Отображение примитивов")
    screen.fill(BACKGROUND_COLOR)

    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    draw_shapes(screen, center)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
