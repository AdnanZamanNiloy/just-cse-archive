import os
os.environ.setdefault("PYOPENGL_PLATFORM", "glx")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def triangle():
    glBegin(GL_LINE_LOOP)
    glVertex2f(5, 5)
    glVertex2f(15, 5)
    glVertex2f(10, 12)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Original triangle
    glColor3f(0, 1, 0)
    triangle()

    # Composite transformation
    glPushMatrix()

    glTranslatef(5, 3, 0)
    glRotatef(30, 0, 0, 1)
    glScalef(1.5, 1.5, 1)

    glColor3f(1, 0, 0)
    triangle()

    glPopMatrix()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Composite Triangle Transformation")

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 30, 0, 30)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
