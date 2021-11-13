from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


kieuchieu = 1


def projective(type, P):
    p = Point2D(0, 0)
    if type == 1:
        p.x = P.x
        p.y = P.y
    elif type == 2:
        p.x = P.x
        p.y = P.z
    elif type == 3:
        p.x = P.y
        p.y = P.z
    return p


def DrawToroid(R, a):
    P = Point3D(0, 0, 0)
    Delta_U = 0.1
    Delta_V = 0.1
    v = -math.pi/2
    while v < math.pi/2:
        u = 0
        while u < 2*math.pi:
            P.x = (R+a*math.cos(v))*math.cos(u)
            P.y = (R+a*math.cos(v))*math.sin(u)
            P.z = a*math.sin(v)
            p = projective(kieuchieu, P)
            glVertex2f(p.x, p.y)
            u += Delta_U
        v += Delta_V


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    glBegin(GL_LINE_LOOP)
    DrawToroid(80, 50)
    glEnd()
    glFlush()


def keyPressed(key, x, y):
    global kieuchieu
    if key == b'1':
        kieuchieu = 1
    if key == b'2':
        kieuchieu = 2
    if key == b'3':
        kieuchieu = 3
    glutPostRedisplay()


glutInit()
glutInitWindowSize(600, 600)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow("Lab5")
gluOrtho2D(-600/2, 600/2, -600/2, 600/2)
glMatrixMode(GL_PROJECTION)
glutDisplayFunc(display)
glutKeyboardFunc(keyPressed)
glutMainLoop()
