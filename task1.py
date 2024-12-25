import pygame
import numpy as np

# Параметры окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ORIGINAL = (200, 100, 0)  # Цвет исходной точки
COLOR_TRANSFORMED = (0, 200, 200)  # Цвет трансформированной точки
DEFAULT_FONT_SIZE = 18


def prompt_user_for_coordinates():
    while True:
        try:
            x_coord = float(input("Введите значение X: "))
            y_coord = float(input("Введите значение Y: "))
            return np.array([x_coord, y_coord])
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числа.")


def apply_transformation(input_point, matrix):
    result = np.dot(matrix, input_point)
    return result


def display_points(window, original, transformed, midpoint):
    x_orig, y_orig = int(original[0] + midpoint[0]), int(midpoint[1] - original[1])
    x_trans, y_trans = int(transformed[0] + midpoint[0]), int(midpoint[1] - transformed[1])

    pygame.draw.circle(window, COLOR_ORIGINAL, (x_orig, y_orig), 5)
    pygame.draw.circle(window, COLOR_TRANSFORMED, (x_trans, y_trans), 5)

    pygame.display.update()


def render_text(window, message, x, y, color=COLOR_BLACK, size=DEFAULT_FONT_SIZE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(message, True, color)
    window.blit(text_surface, (x, y))


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Визуализация преобразований")
    window.fill(COLOR_WHITE)

    mid_x = WINDOW_WIDTH / 2
    mid_y = WINDOW_HEIGHT / 2
    midpoint = np.array([mid_x, mid_y])

    user_point = prompt_user_for_coordinates()
    transformation_matrix = np.array([[1, 3], [4, 1]])  # Преобразование
    transformed_point = apply_transformation(user_point, transformation_matrix)

    display_points(window, user_point[:2], transformed_point, midpoint)

    msg1 = f"Исходная точка: ({user_point[0]:.2f}, {user_point[1]:.2f})"
    msg2 = f"Трансформированная точка: ({transformed_point[0]:.2f}, {transformed_point[1]:.2f})"
    render_text(window, msg1, 10, 10)
    render_text(window, msg2, 10, 40)
    pygame.display.update()

    app_running = True
    while app_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False
        pygame.display.flip()  # Перерисовка экрана
    pygame.quit()


if __name__ == "__main__":
    main()
