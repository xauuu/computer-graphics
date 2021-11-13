from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# - Tỉ lệ với tâm tỉ lệ (x0, y0)

x = 30
y = 15
sx = 3
sy = 3


def init():
    glClearColor(0, 0, 0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-600, 600, -600, 600)


def drawTriangle(matrix):
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 1)
    glVertex2f(matrix[0, 0], matrix[0, 1])
    glColor3f(1, 1, 0)
    glVertex2f(matrix[1, 0], matrix[1, 1])
    glColor3f(0, 1, 1)
    glVertex2f(matrix[2, 0], matrix[2, 1])
    glEnd()


P = np.array([[15, 10, 1],
              [30, 30, 1],
              [45, 10, 1]])


def scale():
    M = np.eye(3)
    M[0, 0] = sx
    M[1, 1] = sy
    M[2, 0] = (1 - sx)*x
    M[2, 1] = (1 - sy)*y
    #[[ sx,  0.,  0.],
    #[ 0.,  sy,  0.],
    #[(1 - sx)*x, (1 - sy)*y,  1.]]
    drawTriangle(P@M)


def mouseWheel(button, dir,  x,  y):
    global sx, sy
    if dir > 0:
        sx += 1
        sy += 1
    else:
        sx -= 1
        sy -= 1
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    scale()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Xauuu")
    init()
    glutDisplayFunc(display)
    glutMouseWheelFunc(mouseWheel)
    glutMainLoop()
