import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def dda(x1, y1, x2, y2):
    points = []
    dx, dy = x2-x1, y2-y1
    steps = max(abs(dx), abs(dy))
    xi, yi = dx/steps, dy/steps

    for _ in range(steps + 1):
        points.append((x1, y1))
        x1 += xi
        y1 += yi

    return points
print(dda(2, 3, 28, 17))

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)

    glBegin(GL_LINE_STRIP)
    for x, y in dda(2, 3, 28, 17):
        glVertex2f(x, y)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"DDA Line")

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 30, 0, 20)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()