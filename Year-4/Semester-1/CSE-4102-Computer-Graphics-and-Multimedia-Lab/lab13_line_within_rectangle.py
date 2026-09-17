import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Rectangle
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(5, 5)
    glVertex2f(25, 5)
    glVertex2f(25, 15)
    glVertex2f(5, 15)
    glEnd()

    # Line inside rectangle
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex2f(8, 7)
    glVertex2f(22, 13)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Line Within Rectangle")

    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 30, 0, 20)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()