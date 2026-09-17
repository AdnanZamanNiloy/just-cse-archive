import os
os.environ.setdefault("PYOPENGL_PLATFORM", "glx")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

XC = YC = 250
R = 200


def circle():
    points = []
    x, y = 0, R
    p = 1 - R

    def add_symmetric(x, y):
        points.extend([
            (XC+x, YC+y), (XC-x, YC+y),
            (XC+x, YC-y), (XC-x, YC-y),
            (XC+y, YC+x), (XC-y, YC+x),
            (XC+y, YC-x), (XC-y, YC-x)
        ])

    while x <= y:
        add_symmetric(x, y)

        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2*x - 2*y + 1

    return points

print (circle())

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
    glutCreateWindow(b"Mid-Point Circle")

    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 600, -1, 1)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()