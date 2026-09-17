import os

os.environ.setdefault("PYOPENGL_PLATFORM", "glx")

import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

XC = YC = 15
R = 8


def circle():
    points = []

    steps = 360

    for i in range(steps):

        t = 2 * math.pi * i / steps

        x = XC + R * math.cos(t)
        y = YC + R * math.sin(t)

        points.append((x, y))

    return points


print(circle())


def display():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glPointSize(2)
    glBegin(GL_POINTS)

    for x, y in circle():

        glVertex2f(x, y)

    glEnd()
    glFlush()


def main():

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Circle Drawing")

    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0, 30, 0, 30)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()