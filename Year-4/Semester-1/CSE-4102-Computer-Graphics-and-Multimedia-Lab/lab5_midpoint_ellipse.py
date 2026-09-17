import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

XC, YC, RX, RY = 250, 250, 200, 100


def ellipse():
    points = []

    def add(x, y):
        points.extend([
            (XC+x, YC+y), (XC-x, YC+y),
            (XC+x, YC-y), (XC-x, YC-y)
        ])

    rx2, ry2 = RX*RX, RY*RY
    x, y = 0, RY
    px, py = 0, 2*rx2*y
    p = ry2 - rx2*RY + 0.25*rx2

    while px < py:
        add(x, y)
        x += 1
        px += 2*ry2

        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= 2*rx2
            p += ry2 + px - py

    p = ry2*(x+0.5)**2 + rx2*(y-1)**2 - rx2*ry2

    while y >= 0:
        add(x, y)
        y -= 1
        py -= 2*rx2

        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += 2*ry2
            p += rx2 - py + px

    return points


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glPointSize(4)

    glBegin(GL_POINTS)
    for x, y in ellipse():
        glVertex2f(x, y)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Mid-Point Ellipse")

    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 500, 0, 500)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()

