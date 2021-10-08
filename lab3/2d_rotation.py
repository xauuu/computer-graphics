from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# - Quay với tâm quay (x0, y0)

alpha = 0
x0 = 0
y0 = 0


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-250, 500, -250, 500)


def drawTriangle(matrix):
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(matrix[0, 0], matrix[0, 1])
    glColor3f(0, 1, 0)
    glVertex2f(matrix[1, 0], matrix[1, 1])
    glColor3f(0, 0, 1)
    glVertex2f(matrix[2, 0], matrix[2, 1])
    glEnd()


P = np.array([[105, 70, 1],
              [210, 210, 1],
              [315, 70, 1]])

M = np.eye(3)


def rotate(x, y):
    M[0, 0] = np.cos(alpha)
    M[0, 1] = np.sin(alpha)
    M[2, 1] = x
    M[1, 0] = -np.sin(alpha)
    M[1, 1] = np.cos(alpha)
    M[2, 2] = y

    Q = P@M
    drawTriangle(Q)


def control(key,  x,  y):
    global alpha
    if key == GLUT_KEY_DOWN:
        alpha += 0.5
    if key == GLUT_KEY_UP:
        alpha -= 0.5
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
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Xauu")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(control)
    glutMainLoop()
