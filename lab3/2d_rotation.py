from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# - Quay với tâm quay (x0, y0)

alpha = 90
x0 = 0
y0 = 0


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


P = np.array([[0, 200, 1],
              [300, -100, 1],
              [-300, -100, 1]])

M = np.eye(3)


def rotate(x, y):
    a = (3.14/180)*alpha
    M[0, 0] = np.cos(a)
    M[0, 1] = np.sin(a)
    M[1, 0] = -np.sin(a)
    M[1, 1] = np.cos(a)
    M[2, 0] = x
    M[2, 1] = y
    #[[ cos(alpha),  sin(alpha),  0.],
    #[ -sin(alpha),  cos(alpha),  0.],
    #[x, y,  1.]]

    Q = P@M
    drawTriangle(Q)


def control(key,  x,  y):
    global alpha
    if key == GLUT_KEY_DOWN:
        alpha -= 10
    if key == GLUT_KEY_UP:
        alpha += 10
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawTriangle(P)
    # rotate(0, 0)
    x = x0 * (1 - np.cos(alpha)) + y0 * np.sin(alpha)
    y = y0 * (1 - np.cos(alpha)) - x0 * np.sin(alpha)
    rotate(x, y)
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Xauu")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(control)
    glutMainLoop()
