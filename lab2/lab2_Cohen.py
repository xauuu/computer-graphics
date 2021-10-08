from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width = 600
height = 600
xmin, xmax, ymin, ymax = -100, 200, -100, 200
listPoint = []

def Ma(x, y):
    m = 0
    if x < xmin:
        m |= 1
    if x > xmax:
        m |= 2
    if y < ymin:
        m |= 4
    if y > ymax:
        m |= 8
    return m


def CohenClip(xA, yA, xB, yB):
    escape, draw = 0, 1
    while escape == 0:
        if (Ma(xA, yA) | Ma(xB, yB) == 0):
            escape = 1
        elif (Ma(xA, yA) & Ma(xB, yB) != 0):
            escape, draw = 1, 0
        else:
            if Ma(xA, yA) == 0:
                xA, yA, xB, yB = xB, yB, xA, yA
            if xA == xB:
                if yA > ymax:
                    yA = ymax
                else:
                    yA = ymin
            else:
                m = (yB - yA) / (xB - xA)
                if xA < xmin:
                    yA += (xmin - xA) * m
                    xA = xmin
                elif xA > xmax:
                    yA += (xmax - xA) * m
                    xA = xmax
                elif yA < ymin:
                    xA += (ymin - yA) * m
                    yA = ymin
                elif yA > ymax:
                    xA += (ymax - yA) * m
                    yA = ymax
    if draw:
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        glVertex2d(xA, yA)
        glVertex2d(xB, yB)
        glEnd()

def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()
    if len(listPoint) == 2:
        CohenClip(listPoint[0][0], listPoint[0][1],
                  listPoint[1][0], listPoint[1][1])
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Xauu")
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glutInitWindowPosition(10, 10)
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
