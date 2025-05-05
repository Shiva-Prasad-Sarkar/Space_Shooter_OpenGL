from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import random

# Game flags
x_r,y_r,z_r = False,False,False
start_game = False
wlc = True
over = False
fpview = False
scaling  = True

#variables
time_1 = time.time()
camera_pos = (0,5, 500 )
fovY = 120  
p_x,p_y= 0, 0
angle  = 0
gr_len = 90

def space():
    global gr_len
    for r in range(12):
        begin_y =gr_len*6 - r*gr_len
        for j in range(12):
            begin_x = gr_len*6 - j*gr_len
            glBegin(GL_QUADS)
            glColor3f(0.4, 0.4, 0.95)
            glVertex3f(begin_x,begin_y,0)
            glVertex3f(begin_x - gr_len, begin_y, 0)
            glVertex3f(begin_x - gr_len, begin_y - gr_len, 0)
            glVertex3f(begin_x, begin_y - gr_len, 0)
            glEnd()


def draw_star():
    for x in range(-500, 501, 100): 
        for y in range(-500, 501, 100): 
            glPointSize(2.5)
            glBegin(GL_POINTS)
            glColor3f(1.0, 1.0, 1.0)
            glVertex3f(x + 20, y + 40, 2) 
            glEnd()


def space_boarder():
    global gr_len
    ht = 7

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-540, -540, 0)
    glVertex3f(-540,  540, 0)
    glVertex3f(-540,  540, ht)
    glVertex3f(-540, -540, ht)

    glColor3f(1, 1, 1)
    glVertex3f(540, -540, 0)
    glVertex3f(540,  540, 0)
    glVertex3f(540,  540, ht)
    glVertex3f(540, -540, ht)

    glColor3f(1, 1, 1)
    glVertex3f(-540, -540, 0)
    glVertex3f( 540, -540, 0)
    glVertex3f( 540, -540, ht)
    glVertex3f(-540, -540, ht)

    glColor3f(1, 1, 1)
    glVertex3f(-540, 540, 0)
    glVertex3f( 540, 540, 0)
    glVertex3f( 540, 540, ht)
    glVertex3f(-540, 540, ht)

    glEnd()

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 720) 
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

    
    draw_text(box_x + 80, box_y + 25, "Start Game", GLUT_BITMAP_TIMES_ROMAN_24)
    draw_text(box_x , box_y - 25, "Welcome to Space Shooter!", GLUT_BITMAP_HELVETICA_18)
    draw_text(box_x + 85, box_y - 50, "Press 'g' to Start", GLUT_BITMAP_HELVETICA_12)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def fighter_spaceship():
    global over,p_x,p_y,angle,x_r,y_r,z_r,scaling

    glPushMatrix()
    glTranslatef(p_x,p_y,30)
    glRotatef(-90, 1, 0, 0)

    if scaling:
        glScalef (.9, .9, 1) 
    else:
        glScalef (.8, .8, 1) 

    if x_r:
        glRotatef(angle, 1, 0, 0)
    elif y_r:
        glRotatef(angle, 0, 1, 0)
    else:
        glRotatef(angle, 0, 0, 1)


    glPushMatrix()
    glColor3f(1, .4, .4)
    glScalef(1.5, .6, 1) 
    glutSolidCube(60)
    glPopMatrix()
    
    glPushMatrix()
    glColor3f(.7, .8, .8)
    glTranslatef(0, 0, -90)  
    gluCylinder(gluNewQuadric(), 3, 20, 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(2, 1, 0)
    glTranslatef(-55, 0, 0)
    gluCylinder(gluNewQuadric(), 10, 15, 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslatef(55, 0, 0)
    gluCylinder(gluNewQuadric(), 10, 15, 60, 10, 10)
    glPopMatrix()
    

    glPopMatrix()


def keyboardListener(key, x, y):
    global wlc,start_game,over,x_r,y_r,z_r
    global p_x,p_y,angle
    
    if key == b'w' and not over:
        if p_y>-480:
            p_y-=5
        
    elif key == b's' and not over:
        if p_y<480:
            p_y+=5
    
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
        if p_x>-500:
            p_x-=5
    
    elif key == b'a' and not over:
        if p_x<500:
            p_x+=5
    
    if key == b'g' and wlc:
        wlc = False
        start_game = True

    elif key == b'f':
        global fpview
        fpview = not fpview


def specialKeyListener(key, x, y):
    global camera_pos
    x, y, z = camera_pos
    if key == GLUT_KEY_LEFT:
        if x>-450:
            x -= 5
    elif key == GLUT_KEY_RIGHT:
        if x<450:
            x += 5
    elif key == GLUT_KEY_UP:
        if y<550:
            y += 5
    elif key == GLUT_KEY_DOWN:
        if y>5:
            y -= 5
    camera_pos = (x, y, z)
    

def mouseListener(button, state, x, y):
    pass  # To be implemented


def setupCamera():
    global fpview, p_x, p_y, angle

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if fpview:
        n_x = p_x
        n_y = p_y - 40   # behind
        n_z = 50        # above
        x = p_x
        y = p_y + 90
        z = 50         # downward a bit

        gluLookAt(n_x, n_y, n_z, 
                x, -y, z, 
                0, 0, 1)
        
    
    else:
        x, y, z = camera_pos
        gluLookAt(x, y, z, 
                  0, 0, 0, 
                  0, 0, 1)


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
    glClearColor(.1,.2,.3,.5)	
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)
    setupCamera()
   
    if wlc:
        game_begin()
        
    else:
        space()
        space_boarder()
        draw_star()
        fighter_spaceship()
       
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800) 
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"3D Space Shooter")
     
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)
    glutMainLoop()
    

if __name__ == "__main__":
    main()
