import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def bresenham(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx

    for _ in range(dx + 1):
        points.append((x1, y1))

        if p < 0:
            x1 += 1
            p += 2 * dy
        else:
            x1 += 1
            y1 += 1
            p += 2 * dy - 2 * dx

    return points


print(bresenham(50, 50, 550, 350))


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)

    glBegin(GL_LINE_STRIP)
    for x, y in bresenham(50, 50, 550, 350):
        glVertex2f(x, y)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutCreateWindow(b"Bresenham Line")

    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 400)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()