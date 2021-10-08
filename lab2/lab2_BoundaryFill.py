from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

width = 600
height = 600
fillCol = [0.4, 0.0, 0.0]
borderCol = [0.0, 0.0, 0.0]


def BoundaryFill(x, y, fillColor, boundaryColour):
    color = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
    if (color[0][0][0] != fillColor[0] and color[0][0][1] != fillColor[1] and color[0][0][2] != fillColor[2]) and (color[0][0][0] != boundaryColour[0] and color[0][0][1] != boundaryColour[1] and color[0][0][2] != boundaryColour[2]):
        glBegin(GL_POINTS)
        glColor3f(fillColor[0], fillColor[1], fillColor[2])
        glVertex2i(x, y)
        glEnd()
        glFlush()
        BoundaryFill(x-1, y, fillColor, boundaryColour)
        BoundaryFill(x+1, y, fillColor, boundaryColour)
        BoundaryFill(x, y-1, fillColor, boundaryColour)
        BoundaryFill(x, y+1, fillColor, boundaryColour)


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        xi = x
        yi = height - y
        BoundaryFill(xi, yi, fillCol, borderCol)
        # glutPostRedisplay()


def drawPolygon():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(150, 100)
    glVertex2i(300, 300)
    glVertex2i(450, 100)
    glEnd()
    glFlush()


def display():
    glLineWidth(3)
    glPointSize(2)
    glClearColor(0.6, 0.8, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawPolygon()
    glFlush()


def init():
    glClearColor(0.6, 0.8, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 600, 0, 600)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("xXau")
    glutDisplayFunc(display)
    init()
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
