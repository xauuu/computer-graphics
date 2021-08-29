from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def myInit():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 600.0, 0.0, 600.0)


def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def draw_8_pixel(xc, yc, x, y):
    draw_pixel(x+xc, y+yc)
    draw_pixel(y+xc, x+yc)
    draw_pixel(y+xc, -x+yc)
    draw_pixel(x+xc, -y+yc)
    draw_pixel(-x+xc, -y+yc)
    draw_pixel(-y+xc, -x+yc)
    draw_pixel(-y+xc, x+yc)
    draw_pixel(-x+xc, y+yc)


def draw_cricle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2*r
    while x <= y:
        draw_8_pixel(xc, yc, x, y)
        if p < 0:
            p += 4*x+6
        else:
            p += 4*(x-y)+10
            y -= 1
        x +=1


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_cricle(200, 200, 100)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow("Breshnam's Cricle Drawing Algorithm")
glutDisplayFunc(display)
myInit()
glutMainLoop()
