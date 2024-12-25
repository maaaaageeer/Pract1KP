import pygame
import numpy as np

# Параметры окна и цвета
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_BACKGROUND = (240, 248, 255)  # Светло-голубой фон
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (200, 0, 50)
COLOR_GREEN = (50, 205, 50)  # Ярко-зелёный
COLOR_BLUE = (70, 130, 180)  # Стальной голубой
COLOR_ORANGE = (255, 165, 0)
COLOR_VIOLET = (138, 43, 226)
TEXT_SIZE = 24


def request_line_coordinates():
    """Запрос координат отрезка от пользователя."""
    while True:
        try:
            x_start = float(input("Введите x1 начальной точки: "))
            y_start = float(input("Введите y1 начальной точки: "))
            x_end = float(input("Введите x2 конечной точки: "))
            y_end = float(input("Введите y2 конечной точки: "))
            return np.array([[x_start, y_start], [x_end, y_end]])
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числа!")


def apply_transformation(line_coords, transformation_matrix):
    """Применение трансформации к координатам отрезка."""
    return np.dot(line_coords, transformation_matrix)


def render_line(surface, midpoint, line_color, start, end):
    """Отрисовка отрезка на экране."""
    x_start, y_start = int(start[0] + midpoint[0]), int(midpoint[1] - start[1])
    x_end, y_end = int(end[0] + midpoint[0]), int(midpoint[1] - end[1])
    pygame.draw.line(surface, line_color, (x_start, y_start), (x_end, y_end), 4)


def display_text(surface, text, x, y, text_color=COLOR_BLACK):
    """Отображение текста на экране."""
    font = pygame.font.Font(None, TEXT_SIZE)
    rendered_text = font.render(text, True, text_color)
    surface.blit(rendered_text, (x, y))


def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Визуализация преобразования отрезка")
    screen.fill(COLOR_BACKGROUND)

    # Центр координат
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    midpoint = np.array([center_x, center_y])

    # Ввод данных
    original_line = request_line_coordinates()
    transformation_matrix = np.array([[2, -1], [-1, 2]])  # Новая матрица преобразования
    transformed_line = apply_transformation(original_line, transformation_matrix)

    # Отрисовка
    screen.fill(COLOR_BACKGROUND)
    render_line(screen, midpoint, COLOR_ORANGE, original_line[0], original_line[1])  # Оригинальный отрезок
    render_line(screen, midpoint, COLOR_VIOLET, transformed_line[0], transformed_line[1])  # Преобразованный отрезок

    # Текстовая информация
    text_original = f"Оригинальный отрезок: ({original_line[0][0]:.2f}, {original_line[0][1]:.2f}) - ({original_line[1][0]:.2f}, {original_line[1][1]:.2f})"
    text_transformed = f"Преобразованный отрезок: ({transformed_line[0][0]:.2f}, {transformed_line[0][1]:.2f}) - ({transformed_line[1][0]:.2f}, {transformed_line[1][1]:.2f})"
    display_text(screen, text_original, 20, 20)
    display_text(screen, text_transformed, 20, 60)

    pygame.display.update()

    # Основной цикл программы
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
