import pygame as pg
import random
import math
import time


def draw_circle(dis, x_cen, y_cen, rad):
    pg.draw.circle(dis, (0, 255, 0), (x_cen,  y_cen), rad)


# Draw Quit Box
def draw_button():
    pg.draw.rect(screen, (255, 0, 0), [width/2, height-(height/8), 140, 40])
    screen.blit(text, (width/2 + 40, (height-height/8) + 5))


def update_count(up_count):
    count_text = button_font.render("SCORE: " + str(up_count), True, (0, 0, 0))
    screen.blit(count_text, ((width - 250), 20))


pg.init()

# Base Window Details
screen = pg.display.set_mode((1920, 1080), flags=pg.FULLSCREEN)
pg.display.set_caption('Circle Game')
screen.fill((255, 255, 255))

# Get Screen Info
width = screen.get_width()
height = screen.get_height()

# Define Font
button_font = pg.font.SysFont('Corbel', 35)
text = button_font.render('Quit', True, (0, 0, 0))

# Score Info
count = 0

# Base Data Setup
draw_button()
update_count(0)
current_circle = False
x_pos = 0
y_pos = 0
Interval = 0

while True:
    # Get Mouse Positions Every Frame, Get Squares for Determining Circle Locations
    mouse = pg.mouse.get_pos()
    sqx = (mouse[0] - x_pos) ** 2
    sqy = (mouse[1] - y_pos) ** 2

    # Draw Circle
    if not current_circle:
        current_circle = True
        radius = random.randint(15, 100)

        # Ensure Entire Circles Are Within Bounds of the Screen
        x_pos = random.randint(0 + radius, width - radius)
        y_pos = random.randint(0 + radius, height - radius)

        draw_circle(screen, x_pos, y_pos, radius)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        # While Mouse Is Held Down
        if event.type == pg.MOUSEBUTTONDOWN:
            # Button Location
            if width / 2 <= mouse[0] <= width / 2 + 140 and height-(height/8) <= mouse[1] <= height-(height/8) + 40:
                pg.quit()
                quit()
            # Circle Location, Fill After and Replace Button
            # Uses Circle Distance Formula For Finding Bounds of Circle
            if math.sqrt(sqx + sqy) < radius:
                screen.fill((255, 255, 255))
                current_circle = False
                draw_button()
                count = count + 1
                update_count(count)

    # If 15 Seconds have passed...
    if pg.time.get_ticks() >= 15000:
        # Run "End Game" Phase
        screen.fill((255, 0, 0))
        update_count(count)
        pg.display.update()
        # Pause So User Can See Score
        time.sleep(5)
        pg.quit()
        quit()

    # Post Updates
    pg.display.update()