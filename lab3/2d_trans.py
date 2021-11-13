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
    glClearColor(0, 0, 0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-320, 320, -320, 320, -1, 1)

def drawTriangle(matrix):
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 1)
    glVertex2f(matrix[0, 0], matrix[0, 1])
    glColor3f(1, 1, 0)
    glVertex2f(matrix[1, 0], matrix[1, 1])
    glColor3f(0, 1, 1)
    glVertex2f(matrix[2, 0], matrix[2, 1])
    glEnd()


def trans():
    P = np.array([[75, 50, 1],
                 [150, 150, 1],
                 [225, 50, 1]])
    
    midGx = (P[0, 0] + P[1, 0] + P[2, 0] ) /3
    midGy = (P[0, 1] + P[1, 1] + P[2, 1] ) /3
    M = np.eye(3)
    M[2, 0] = tx - midGx
    M[2, 1] = ty - midGy
    #[[ 1.,  0.,  0.],
    #[ 0.,  1.,  0.],
    #[tx, ty,  1.]]
    drawTriangle(P@M)


def control(key,  x,  y):  
    global tx, ty 
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
    global tx, ty 
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        tx = x - 320
        ty = 320 - y


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    trans()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 640)
    glutCreateWindow("Xauuu")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(control)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
