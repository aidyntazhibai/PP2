import pygame
import random
import math

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

def eraser(canvas, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(canvas, color, rect, 2)

def draw_circle(canvas, color, center, radius):
    pygame.draw.circle(canvas, color, center, radius)

def draw_rectangle(canvas, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(canvas, color, rect, 2)

def draw_triangle(canvas, color, start, end):
    x1, y1 = start
    x2, y2 = end
    x3 = x1
    y3 = y2
    pygame.draw.polygon(canvas, color, [(x1, y1), (x2, y2), (x3, y3)])

try :
    while True :
        e = pygame.event.wait()

        if e.type == pygame.QUIT :
            raise StopIteration

        if e.type == pygame.MOUSEBUTTONDOWN :
            # Selecting random Color Code
            color = (random.randrange(256), random.randrange(256), random.randrange(256))
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True

            # if e.type == pygame.KEYDOWN :
            #     start_pos = e.pos
            #     shape_type = 'circle'
            # if e.type == pygame.KEYUP :
            #     start_pos = e.pos
            #     shape_type = 'eraser'
            # if e.type == pygame.K_LEFT :
            #     start_pos = e.pos
            #     shape_type = 'rectangle'
            # if e.type == pygame.K_RIGHT:
            #     start_pos = e.pos
            #     shape_type = 'triangle'


             # Start drawing shapes
            if e.button == 1: 
                start_pos = e.pos
                shape_type = 'circle'
            elif e.button == 3: # Right mouse button
                start_pos = e.pos
                shape_type = 'rectangle'
            elif e.button == 2: # Middle mouse button
                start_pos = e.pos
                shape_type = 'triangle'

            elif e.type == pygame.K_UP: # Middle mouse button
                start_pos = e.pos
                shape_type = 'eraser'

        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP :
            draw_on = False

            # Finish drawing shapes
            if shape_type == 'circle':
                end_pos = e.pos
                distance = math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                draw_circle(screen, color, start_pos, int(distance))
            elif shape_type == 'rectangle':
                end_pos = e.pos
                draw_rectangle(screen, color, start_pos, end_pos)
            elif shape_type == 'triangle':
                end_pos = e.pos
                draw_triangle(screen, color, start_pos, end_pos)
            elif shape_type == 'eraser':
                end_pos = e.pos
                draw_rectangle(screen, (0, 0, 0), start_pos, end_pos)

        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION :
            if draw_on :
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        pygame.display.flip()

except StopIteration :
    pass

# Quit
pygame.quit()