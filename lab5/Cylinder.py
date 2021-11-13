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


def DrawCylinder(R, h):
    P = Point3D(0, 0, 0)
    Delta_U = 0.06
    Delta_V = 0.03
    u = 0
    while u < 2*math.pi:
        v = 0
        while v < 1:
            P.x = R*math.cos(u)
            P.y = R*math.sin(u)
            P.z = v*h
            p = projective(kieuchieu, P)
            glVertex2f(p.x, p.y)
            v += Delta_V
        u += Delta_U
        
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    glBegin(GL_LINE_LOOP)
    DrawCylinder(40,120)
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

