import os
os.environ.setdefault("PYOPENGL_PLATFORM", "glx")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def rectangle():
    glBegin(GL_LINE_LOOP)
    glVertex2f(5, 5)
    glVertex2f(15, 5)
    glVertex2f(15, 10)
    glVertex2f(5, 10)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Original rectangle
    glColor3f(0, 1, 0)
    rectangle()

    # Translated rectangle
    glPushMatrix()
    glTranslatef(10, 8, 0)

    glColor3f(1, 0, 0)
    rectangle()

    glPopMatrix()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Rectangle Translation")

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 30, 0, 30)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()