from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
sys.setrecursionlimit(15000)

width = 600
height = 600
fillCol = [1, 1, 0]
fillCol1 = [1, 0, 1]
borderCol = [1, 1, 1]


def BoundaryFill(x, y, fillColor, boundaryColour):
    colour = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
    if (colour != boundaryColour).any() and (colour != fillColor).any():
        glBegin(GL_POINTS)
        glColor3f(fillColor[0], fillColor[1], fillColor[2])
        glVertex2f(x, y)
        glEnd()
        glFlush()
        BoundaryFill(x+1, y, fillColor, boundaryColour)
        BoundaryFill(x-1, y, fillColor, boundaryColour)
        BoundaryFill(x, y-1, fillColor, boundaryColour)
        BoundaryFill(x, y+1, fillColor, boundaryColour)


def MouseEventHandler(button, state, x, y):
    xi = x
    yi = height - y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        BoundaryFill(xi, yi, fillCol, borderCol)
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        BoundaryFill(xi, yi, fillCol1, borderCol)
    glutPostRedisplay()


def display():
    glLineWidth(2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(300, 301)
    glVertex2i(250, 250)
    glVertex2i(350, 250)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex2i(200, 200)
    glVertex2i(150, 150)
    glVertex2i(250, 150)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex2i(400, 400)
    glVertex2i(350, 350)
    glVertex2i(450, 350)
    glEnd()
    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 600, 0, 600)


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("xXau")
    glutDisplayFunc(display)
    init()
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
