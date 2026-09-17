# 5: Mid-point ellipse algorithm (region 1 + region 2, 4-way symmetry)
from OpenGL.GL import *
from OpenGL.GLUT import *

W = H = 700
P = []

def ellipse(xc, yc, rx, ry):
    x, y = 0, ry
    a2, b2 = rx*rx, ry*ry
    d2x, d2y = 2*b2*x, 2*a2*y

    d1 = b2 - a2*ry + a2/4                 # region 1: slope < 1
    while d2x < d2y:
        P.extend([(xc+x, yc+y), (xc-x, yc+y), (xc+x, yc-y), (xc-x, yc-y)])
        x += 1; d2x += 2*b2
        if d1 < 0: d1 += d2x + b2
        else: y -= 1; d2y -= 2*a2; d1 += d2x - d2y + b2

    d2 = b2*(x+0.5)**2 + a2*(y-1)**2 - a2*b2   # region 2: slope > 1
    while y > 0:
        P.extend([(xc+x, yc+y), (xc-x, yc+y), (xc+x, yc-y), (xc-x, yc-y)])
        y -= 1; d2y -= 2*a2
        if d2 > 0: d2 += a2 - d2y
        else: x += 1; d2x += 2*b2; d2 += d2x - d2y + a2

ellipse(350, 350, 250, 150)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3); glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    for x, y in P: glVertex2i(x, y)
    glEnd(); glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(W, H)
glutCreateWindow(b"5 Midpoint Ellipse")
glClearColor(0, 0, 0, 1)
glOrtho(0, W, 0, H, -1, 1)
glutDisplayFunc(display)
glutKeyboardFunc(lambda k, *a: exit() if k == b"\x1b" else None)
glutMainLoop()
