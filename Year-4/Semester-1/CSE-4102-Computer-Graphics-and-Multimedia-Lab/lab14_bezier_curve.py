import os
os.environ.setdefault("PYOPENGL_PLATFORM", "glx")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


CONTROL_POINTS = [(0, 0), (30, 60), (70, 60), (100, 0)]


def de_casteljau(points, t):
    pts = [(x, y) for x, y in points]
    while len(pts) > 1:
        pts = [
            (
                (1 - t) * pts[i][0] + t * pts[i + 1][0],
                (1 - t) * pts[i][1] + t * pts[i + 1][1],
            )
            for i in range(len(pts) - 1)
        ]
    return pts[0]

def bezier_curve(segments=100):
    return [
        de_casteljau(CONTROL_POINTS, i / segments)
        for i in range(segments + 1)
    ]


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Control points
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    for x, y in CONTROL_POINTS:
        glVertex2f(x, y)
    glEnd()

    # Bezier curve
    glColor3f(0, 1, 0)
    glBegin(GL_LINE_STRIP)
    for x, y in bezier_curve():
        glVertex2f(x, y)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Bezier Curve")

    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-10, 110, -10, 70)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()