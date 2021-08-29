from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def myInit():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.0);
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,600.0,0.0,600.0)

def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    

def draw_line(x0, y0, xEnd, yEnd):
    dx = xEnd - x0
    dy = yEnd - y0
    d = dy - (dx/2)
    x = x0
    y = y0

    while (x < xEnd):
        x = x+1
        if(d < 0):
            d = d + dy
 
        else:
            d = d + (dy - dx)
            y=y+1
        
        draw_pixel(x, y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line(100, 100, 400, 400)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutInitWindowPosition(0,0)
glutCreateWindow("Mid Point's Line Drawing Algorithm");
glutDisplayFunc(display)
myInit()
glutMainLoop()
