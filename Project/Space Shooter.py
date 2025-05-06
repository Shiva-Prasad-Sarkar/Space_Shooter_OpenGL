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
scaling2 = True

#variables
enim = []
time_1 = time.time()
time_2 = time_1
camera_pos = (0,5, 500 )
fovY = 120  
p_x,p_y= 0, 0
angle  = 0
gr_len = 90
enemy = 5


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
    global scaling2
    for x in range(-500, 501, 100): 
        for y in range(-500, 501, 100): 
            if scaling2:
                glPointSize(3)
                glColor3f(1.0, 1.0, 1.0)
            else:
                glPointSize(1.5)
                glColor3f(0, 0, 0)
            glBegin(GL_POINTS)

            glVertex3f(x , y , 2) 
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

    box_x, box_y = 530, 400
    box_width, box_height = 330, 70

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
    draw_text(box_x+15 , box_y - 25, "Welcome to Space Shooter!", GLUT_BITMAP_HELVETICA_18)
    draw_text(box_x + 105, box_y - 50, "Press 'g' to Start", GLUT_BITMAP_HELVETICA_12)

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


def draw_enemy(e):
    global scaling
    x,y = e[0],e[1]
    glPushMatrix()
    glTranslatef(x, y, 0)
    
    if scaling: 
        glScalef (1, 1, 1) 
    else:
        glScalef (.8, .8, .8) 

    glColor3f(.7, .6, .6)
    glTranslatef(0, 0, 0)
    glutSolidCube(40)
    
    glColor3f(0.4,0,0.5)
    glTranslatef(0, 0, 0)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 10, 2, 40, 10, 10)
    glPopMatrix()

def pos_maker():
    global gr_len,enemy
    min = int(12*gr_len/2) #to check if pos crosses boundary
    while True:
        x,y = random.randint(-(min-55),(min-55)),-500
        if abs(x) > 150 or abs(y) > 150: 
            break
    return [x,y,0]

#assigning x and y pos of enemies
for i in range(enemy):
    enim.append(pos_maker())

def keyboardListener(key, x, y):
    global wlc,start_game,over,x_r,y_r,z_r,fpview
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
    global fpview, p_x, p_y

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if fpview:
       
        cam_x = p_x
        cam_y = p_y + 20   
        cam_z = 70     

       
        look_x = p_x
        look_y = p_y
        look_z = 40

        gluLookAt(cam_x, cam_y, cam_z,
                  look_x, look_y, look_z,
                  0, 0, 1)  

    else:
        x, y, z = camera_pos
        gluLookAt(x, y, z, 
                  0, 0, 0, 
                  0, 0, 1)


def idle():
    global scaling,scaling2, time_1, time_2
    ftime = time.time()
    

    if ftime - time_1 >= .7:
        scaling = not scaling
        time_1 = ftime
    
    if ftime - time_2 >= .4:
        scaling2 = not scaling2
        time_2 = ftime

    
    glutPostRedisplay()

def showScreen():
    global start_game,wlc,over

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
        for i in enim:
            draw_enemy(i)
        if not over:
            draw_text(1110, 690, f"Life Remainig: jibon",GLUT_BITMAP_HELVETICA_12)
            draw_text(10, 690, f"Match Score : murder ",GLUT_BITMAP_HELVETICA_12)
            draw_text(10, 670, f"Fire Missed : {0} ",GLUT_BITMAP_HELVETICA_12)
        else:
            draw_text(450, 690, f"Game is Over. Score is murder.",GLUT_BITMAP_TIMES_ROMAN_24)
            draw_text(480, 660, f'Press <r> to RESTART',GLUT_BITMAP_TIMES_ROMAN_24)


       
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
