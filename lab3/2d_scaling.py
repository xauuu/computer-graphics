from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# - Tỉ lệ với tâm tỉ lệ (x0, y0)

x = 5
y = 2
sx = 3
sy = 3


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 600, 0, 600)


def drawPolygon(matrix):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(matrix[0, 0], matrix[0, 1])
    glVertex2f(matrix[1, 0], matrix[1, 1])
    glVertex2f(matrix[2, 0], matrix[2, 1])
    glEnd()
    glFlush()


def scale():
    p = np.array([[15, 10, 1],
                 [30, 30, 1],
                 [45, 10, 1]])

    m1 = np.eye(3)
    m1[2, 0] = -x
    m1[2, 1] = -y


    m2 = np.array([[sx, 0, 0],
                 [0, sy, 0],
                 [0, 0, 1]])

    m = m1.dot(m2)

    m1[2, 0] = x
    m1[2, 1] = y

    m = m1.dot(m)

    print (p.dot(m))
    drawPolygon(p.dot(m))


def mouseWheel(button, dir,  x,  y):
    global sx
    global sy
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


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Xauu")
    glutInitWindowPosition(10, 10)
    init()
    glutDisplayFunc(display)
    glutMouseWheelFunc(mouseWheel)
    glutMainLoop()
