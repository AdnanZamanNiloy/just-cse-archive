import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

W = H = 600
GW, GH = 30, 20
EMPTY, OLD, NEW = 0, 1, 2


def flood_fill(grid, x, y):
    old = grid[y][x]
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if grid[y][x] != old:
            continue

        grid[y][x] = NEW

        for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= nx < GW and 0 <= ny < GH:
                stack.append((nx, ny))


def rectangle(grid):
    for x in range(5, 26):
        grid[3][x] = grid[17][x] = OLD

    for y in range(3, 18):
        grid[y][5] = grid[y][25] = OLD


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    grid = [[EMPTY] * GW for _ in range(GH)]
    rectangle(grid)

    flood_fill(grid, 15, 10)

    for y in range(GH):
        for x in range(GW):
            if grid[y][x] == OLD:
                glColor3f(1, 1, 1)
            elif grid[y][x] == NEW:
                glColor3f(0, 1, 0)
            else:
                continue

            glBegin(GL_QUADS)
            glVertex2f(x, y)
            glVertex2f(x+1, y)
            glVertex2f(x+1, y+1)
            glVertex2f(x, y+1)
            glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(W, H)
    glutCreateWindow(b"Flood Fill")

    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, GW, 0, GH)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()