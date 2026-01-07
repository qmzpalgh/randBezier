"""
Animated bezier curve visualization.
Draws a bezier curve with anchor/control points that move using random acceleration.

Author: James Gibbons (original Processing sketch)
Python port using Pygame
"""

import pygame
import random
import sys


def bezier_point(t, p0, p1, p2, p3):
    """Calculate point on cubic bezier curve at parameter t (0-1)."""
    u = 1 - t
    return (
        u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1],
    )


def draw_bezier(surface, color, p0, p1, p2, p3, segments=50):
    """Draw a cubic bezier curve using line segments."""
    points = [bezier_point(t / segments, p0, p1, p2, p3) for t in range(segments + 1)]
    pygame.draw.lines(surface, color, False, points, 1)


def main():
    pygame.init()

    # Fullscreen display
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()
    pygame.display.set_caption("Random Bezier")

    clock = pygame.time.Clock()

    # Create surface for fade effect
    fade_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    fade_surface.fill((0, 0, 0, 10))

    # Initialize vectors: 4 points, each with position and velocity
    # positions[i] = [x, y], velocities[i] = [vx, vy]
    positions = [[random.uniform(0, width), random.uniform(0, height)] for _ in range(4)]
    velocities = [[0.0, 0.0] for _ in range(4)]

    # Fill screen with black initially
    screen.fill((0, 0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Apply fade effect (dim previous frame)
        screen.blit(fade_surface, (0, 0))

        # Update each point
        for i in range(4):
            # Boundary collision - reverse velocity
            if positions[i][0] > width or positions[i][0] < 0:
                velocities[i][0] = -velocities[i][0]
            if positions[i][1] > height or positions[i][1] < 0:
                velocities[i][1] = -velocities[i][1]

            # Random acceleration
            accel_x = random.uniform(-0.1, 0.1)
            accel_y = random.uniform(-0.1, 0.1)

            # Update velocity and position
            velocities[i][0] += accel_x
            velocities[i][1] += accel_y
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]

        # Draw bezier curve
        draw_bezier(
            screen,
            (255, 255, 255),
            positions[0],
            positions[1],
            positions[2],
            positions[3],
        )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
