from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time

time_1 = time.time()

# Updated camera and window parameters
c_x, c_y, c_z = 0, 100, 300  # Elevated and pulled back
camera_pos = (c_x, c_y, c_z)
fovY = 120  # Field of view for perspective
p_x,p_y=0,0
x_r,y_r,z_r = False,False,False
# Game flags
start_game = False
wlc = True
over = False
angle  = 0
fpview = False
scaling  = True


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 720)  # Updated for new window size
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def game_begin():
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 720)
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    box_x, box_y = 490, 400
    box_width, box_height = 300, 70

    glColor3f(1,1,1) 
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(box_x, box_y)
    glVertex2f(box_x + box_width, box_y)
    glVertex2f(box_x + box_width, box_y + box_height)
    glVertex2f(box_x, box_y + box_height)
    glVertex2f(box_x, box_y)
    glVertex2f(box_x, box_y + box_height)
    glVertex2f(box_x + box_width, box_y)
    glVertex2f(box_x + box_width, box_y + box_height)
    
    glEnd()

    
    draw_text(box_x + 100, box_y + 25, "Start Game", GLUT_BITMAP_TIMES_ROMAN_24)
    draw_text(box_x + 30, box_y - 25, "Welcome to Space Shooter!", GLUT_BITMAP_HELVETICA_18)
    draw_text(box_x + 100, box_y - 50, "Press 'g' to Start", GLUT_BITMAP_HELVETICA_12)

    
    # Restore previous projection/modelview states
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def fighter_spaceship():
    global over,p_x,p_y,angle,x_r,y_r,z_r,scaling
    
    glPushMatrix()
    if scaling: #if use  time function
        glScalef (1.05, 1.05, 1.05) 
    else:
        glScalef (.95, .95, .95) 
    glTranslatef(p_x,p_y,0)
    if x_r:
        glRotatef(angle, 1, 0, 0)
    elif y_r:
        glRotatef(angle, 0, 1, 0)
    else:
        glRotatef(angle, 0, 0, 1)


    glColor3f(1, 0, 0)
    glPushMatrix()
    glScalef(1.5, .5, 1) 
    glutSolidCube(60)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(-55, 0, 0)
    gluCylinder(gluNewQuadric(), 13, 9, 60, 10, 10)
    glPopMatrix()

    
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(55, 0, 0)
    gluCylinder(gluNewQuadric(), 13, 9, 60, 10, 10)
    glPopMatrix()


    glPushMatrix()
    glColor3f(0, 1, 1)
    glTranslatef(0, 0, -40)  
    gluCylinder(gluNewQuadric(), 5, 25, 100, 10, 10)
    glPopMatrix()

    
    glPushMatrix()
    glColor3f(0, 1, 1)
    glTranslatef(0, 0, 40) 
    gluCylinder(gluNewQuadric(), 5, 5, 20, 10, 10)
    glPopMatrix()

    glPopMatrix()



def keyboardListener(key, x, y):
    global wlc,start_game,over,x_r,y_r,z_r
    global p_x,p_y,angle
    
    if key == b'w' and not over:
        p_y+=5
        
    elif key == b's' and not over:
        p_y-=5
    
            
    elif key == b'x' and not over:
        x_r = True
        angle+=5
        y_r,z_r = False,False

    elif key == b'y' and not over:
        y_r = True
        angle+=5
        x_r,z_r = False,False

    elif key == b'z' and not over:
        z_r = True
        angle+=5
        y_r,x_r = False,False

    elif key == b'd' and not over:
        if p_x<540:
            p_x+=5
    
    elif key == b'a' and not over:
        if p_x>-540:
            p_x-=5
    
    if key == b'g' and wlc:
        wlc = False
        start_game = True

    elif key == b'v':
        global fpview
        fpview = not fpview


def specialKeyListener(key, x, y):
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """
    global camera_pos
    x, y, z = camera_pos
    if key == GLUT_KEY_LEFT:
        x -= 5
    elif key == GLUT_KEY_RIGHT:
        x += 5
    elif key == GLUT_KEY_UP:
        y += 5
    elif key == GLUT_KEY_DOWN:
        y -= 5
    camera_pos = (x, y, z)

def mouseListener(button, state, x, y):
    """
    Handles mouse inputs for firing bullets (left click) and toggling camera mode (right click).
    """
    pass  # To be implemented

def setupCamera():
    global fpview
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1280 / 720, 0.1, 2000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if fpview:
        # Eye slightly above and behind the front of the ship
        eye_x = p_x
        eye_y = p_y + 40  # Elevated view
        eye_z = 60        # Pull back to reduce zoom effect

        center_x = p_x
        center_y = p_y + 10
        center_z = -200   # Look far into the distance

        gluLookAt(eye_x, eye_y, eye_z,
                  center_x, center_y, center_z,
                  0, 1, 0)
    else:
        x, y, z = camera_pos
        gluLookAt(x, y, z,
                  0, 0, 0,
                  0, 1, 0)



def idle():
    global scaling, time_1
    ftime = time.time()

    if ftime - time_1 >= .7:
        scaling = not scaling
        time_1 = ftime
    glutPostRedisplay()

def showScreen():
    global start_game,wlc
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1280, 720)
    setupCamera()

   
    if wlc:
        game_begin()
    else:
        fighter_spaceship()


    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1280, 720)  # Updated window size
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Space Shooter")

    glEnable(GL_DEPTH_TEST)  # Enable depth for 3D rendering

    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
