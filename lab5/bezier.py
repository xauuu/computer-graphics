from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


n = -1
P = []


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


def Bernstein(t, n, k):
    ckn = fact(n)/(fact(k)*fact(n-k))
    kq = ckn * ((1-t)**(n-k))*(t**k)
    return kq


def Tpt(p, n, t):
    pt = Point(0, 0)
    for k in range(n+1):
        B = Bernstein(t, n, k)
        pt.x = (long)(pt.x+p[k].x*B)
        pt.y = (long)(pt.y+p[k].y*B)
    return pt


def veBezier(p, n):
    t = 0
    m = 10000
    dt = 1/float(m)
    glBegin(GL_LINE_STRIP)
    for i in range(m+1):
        pt = Tpt(p, n, t)
        glVertex2i(pt.x, pt.y)
        t += dt
    glVertex2i((int)(p[n].x), (int)(p[n].y))
    glEnd()


def VeDaGiacKiemSoat(P, n):
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(1, 0xAAA)
    glBegin(GL_LINE_STRIP)
    for i in range(n+1):
        glVertex2i(P[i].x, P[i].y)
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def Mydisplay():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    VeDaGiacKiemSoat(P, n)
    glColor3f(1.0, 1.0, 0.0)
    if len(P) > 1:
        veBezier(P, n)
    glFlush()


def MouseEventHandler(button, state, x, y):
    global n
    if(button == GLUT_LEFT_BUTTON and state == GLUT_UP):
        n += 1
        p = Point(x-300, 300-y)
        P.append(p)
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(10, 10)
glutCreateWindow("Ve duong cong Bezier")
gluOrtho2D(-300, 300, -300, 300)
glClearColor(0, 0, 0, 0)
glutMouseFunc(MouseEventHandler)
glutDisplayFunc(Mydisplay)
glutMainLoop()
