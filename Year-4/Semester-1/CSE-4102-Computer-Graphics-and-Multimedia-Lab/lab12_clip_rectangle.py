import os
os.environ["PYOPENGL_PLATFORM"] = "glx"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

clip = (8, 5, 22, 15)
rect = [(3, 7), (27, 7), (27, 13), (3, 13)]


def clip_rect(p):
    xmin, ymin, xmax, ymax = clip

    for edge in range(4):
        q = []

        for i in range(len(p)):
            a = p[i - 1]
            b = p[i]

            if edge == 0:
                ina, inb = a[0] >= xmin, b[0] >= xmin
            elif edge == 1:
                ina, inb = a[0] <= xmax, b[0] <= xmax
            elif edge == 2:
                ina, inb = a[1] >= ymin, b[1] >= ymin
            else:
                ina, inb = a[1] <= ymax, b[1] <= ymax

            if inb:
                if not ina:
                    q.append(intersect(a, b, edge))
                q.append(b)
            elif ina:
                q.append(intersect(a, b, edge))

        p = q

    return p


def intersect(a, b, edge):
    xmin, ymin, xmax, ymax = clip
    x1, y1 = a
    x2, y2 = b

    if edge == 0:
        x = xmin
        y = y1 + (y2-y1)*(xmin-x1)/(x2-x1)
    elif edge == 1:
        x = xmax
        y = y1 + (y2-y1)*(xmax-x1)/(x2-x1)
    elif edge == 2:
        y = ymin
        x = x1 + (x2-x1)*(ymin-y1)/(y2-y1)
    else:
        y = ymax
        x = x1 + (x2-x1)*(ymax-y1)/(y2-y1)

    return x, y


def draw(p, color):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for x, y in p:
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Clipping window
    x1, y1, x2, y2 = clip
    draw([(x1,y1),(x2,y1),(x2,y2),(x1,y2)], (1,1,0))

    # Original rectangle
    draw(rect, (1,0,0))

    # Clipped rectangle
    draw(clip_rect(rect), (0,1,0))

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Rectangle Clipping")

    glClearColor(0,0,0,1)
    gluOrtho2D(0,30,0,20)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()