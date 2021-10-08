from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# - Tịnh tiến
# - Tỉ lệ với tâm tỉ lệ (x0, y0)
# - Quay với tâm quay (x0, y0)
# - Đối xứng qua đường thẳng y=ax+b

tx = 0
ty = 0

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-320, 320, -320, 320, -1, 1)

def drawPolygon(matrix):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(matrix[0, 0], matrix[0, 1])
    glVertex2f(matrix[1, 0], matrix[1, 1])
    glVertex2f(matrix[2, 0], matrix[2, 1])
    glEnd()
    glFlush()


def trans():
    P = np.array([[75, 50, 1],
                 [150, 150, 1],
                 [225, 50, 1]])
    
    midX = (P[0, 0] + P[1, 0]) / 2
    midY = (P[0, 1] + P[1, 1]) / 2

    M = np.eye(3)
    M[2, 0] = tx - midX
    M[2, 1] = ty - midY
    drawPolygon(P.dot(M))


def control(key,  x,  y):
    
    global tx 
    global ty 
    if key == GLUT_KEY_DOWN:
        ty -= 10
    if key == GLUT_KEY_UP:
        ty += 10
    if key == GLUT_KEY_RIGHT:
        tx += 10
    if key == GLUT_KEY_LEFT:
        tx -= 10
    glutPostRedisplay()

def MouseEventHandler(button, state, x, y):
    global tx 
    global ty 
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        tx = x - 320
        ty = 320 - y


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    trans()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 640)
    glutInitWindowPosition(320, 320)
    glutCreateWindow("Xauu")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(control)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
