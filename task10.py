import pygame
import math

# Параметры окна
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
COLOR_BACKGROUND = (240, 248, 255)  
COLOR_CURVE = (75, 0, 200) 

def compute_snail_point(param_a, param_b, angle, center_coords):
    rad = param_b + 2 * param_a * math.cos(angle)
    x_coord = rad * math.cos(angle)
    y_coord = rad * math.sin(angle)
    return int(x_coord + center_coords[0]), int(center_coords[1] - y_coord)

def draw_snail_curve(surface, center_coords, param_a, param_b, curve_color, total_steps=2000, angle_step=0.015):
    points = []
    for step in range(total_steps):
        angle = step * angle_step
        points.append(compute_snail_point(param_a, param_b, angle, center_coords))
    if len(points) > 1:
        pygame.draw.lines(surface, curve_color, False, points, 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pascal Snail Visualization")
    screen.fill(COLOR_BACKGROUND)

    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2
    center = (center_x, center_y)

    snail_param_a = 100
    snail_param_b = 50

    draw_snail_curve(screen, center, snail_param_a, snail_param_b, COLOR_CURVE)

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
