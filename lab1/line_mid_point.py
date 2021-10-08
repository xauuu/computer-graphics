from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listPoint = []
width = 600
height = 600

def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex3i(x, y, 0)
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
    if len(listPoint) == 2:
        draw_line(listPoint[0][0], listPoint[0][1],
                  listPoint[1][0], listPoint[1][1])
    glFlush()

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Breshnam's Line Drawing Algorithm")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
