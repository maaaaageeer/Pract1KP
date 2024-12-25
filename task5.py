import pygame
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)

TRANSFORMATION_MATRIX = np.array([[1, 2], [3, 1]])
LINE_SEGMENTS = np.array([[50, 100], [250, 200], [50, 200], [250, 300]], dtype=float)

def apply_transformation(segment, matrix):
    reshaped_segment = segment.reshape(2, 2)
    transformed = np.dot(reshaped_segment, matrix)
    return transformed.reshape(2, 2)

def compute_slope(segment):
    x_start, y_start = segment[0]
    x_end, y_end = segment[1]
    if x_end - x_start == 0:
        return float('inf')
    return (y_end - y_start) / (x_end - x_start)

def render_line(surface, origin, color, start, end, thickness=3):
    x_start, y_start = int(start[0] + origin[0]), int(origin[1] - start[1])
    x_end, y_end = int(end[0] + origin[0]), int(origin[1] - end[1])
    pygame.draw.line(surface, color, (x_start, y_start), (x_end, y_end), thickness)

def render_text(surface, message, x, y, color=COLOR_BLACK, font_size=20):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(message, True, color)
    surface.blit(text_surface, (x, y))

def main():
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Parallel Line Transformation")
    display.fill(COLOR_WHITE)

    origin_x = 100
    origin_y = 700
    origin = np.array([origin_x, origin_y])

    transformed_segment1 = apply_transformation(LINE_SEGMENTS[:2], TRANSFORMATION_MATRIX)
    transformed_segment2 = apply_transformation(LINE_SEGMENTS[2:], TRANSFORMATION_MATRIX)

    slope_original1 = compute_slope(LINE_SEGMENTS[:2])
    slope_original2 = compute_slope(LINE_SEGMENTS[2:])
    slope_transformed1 = compute_slope(transformed_segment1)
    slope_transformed2 = compute_slope(transformed_segment2)

    render_line(display, origin, COLOR_YELLOW, LINE_SEGMENTS[0], LINE_SEGMENTS[1])
    render_line(display, origin, COLOR_YELLOW, LINE_SEGMENTS[2], LINE_SEGMENTS[3])
    render_line(display, origin, COLOR_BLUE, transformed_segment1[0], transformed_segment1[1])
    render_line(display, origin, COLOR_BLUE, transformed_segment2[0], transformed_segment2[1])

    render_text(display, f"Initial Slope L1: {slope_original1:.2f}", 10, 10)
    render_text(display, f"Initial Slope L2: {slope_original2:.2f}", 10, 40)
    render_text(display, f"Transformed Slope L1: {slope_transformed1:.2f}", 10, 70)
    render_text(display, f"Transformed Slope L2: {slope_transformed2:.2f}", 10, 100)

    pygame.display.update()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
