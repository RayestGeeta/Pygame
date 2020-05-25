# -*- coding: utf-8 -*-
"""
Created on Thu May 08 12:07:14 2020
CSE 30 Spring 2020 Program 3 starter code
@author: Fahim
"""
import random
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class Particle:
    def __init__(self, x=0, y=0, z=0, color=(0, 0, 0, 1), exploded = False, flag = 1):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.exploded = exploded
        self.lifetime = random.randint(200, 300)
        self.time = 0
        self.velocity = [random.uniform(-.01, .01), random.uniform(-.01, .01), random.uniform(-.01, .01), ]
        self.trail = []
        self.colors = []
        self.flag = flag

    def update(self):
        n = 10
        # if self.lifetime >= 0:
        for i in range(n):
            c = list(self.color)
            c[-1] = (n - i)/n
            self.colors.append(tuple(c))

        if self.y > 10:
            self.exploded = True
        if self.exploded:
            if len(self.trail) < n:
                self.trail.append([self.x, self.y, self.z])


            else:
                self.trail.append([self.x, self.y, self.z])
                self.trail.pop(0)

                # c3 = self.color[-1] - ((len(self.trail))/n)*n
                # c = list(self.color)
                # c[-1] = c3
                # self.colors.append(tuple(c))
                # self.colors.pop(0)


            self.x += self.velocity[0]
            self.y += self.velocity[1] - 10*self.time*0.00005 - 0.5* 10 * 0.01*0.01
            self.z += self.velocity[2]
            self.time += 1
        else:
            self.y += 0.1
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.miss()
        # self.second_exploder()
        # if self.lifetime

    def miss(self):
        n = 10
        self.color = (0, 0, 1, 0)
        for i in range(n):
            c = list(self.color)
            c[-1] = (n - i) / n
            self.colors.append((0, 0, 1, 0))
        self.y = 0
        self.x = 0
        self.z = 0

    # def second_exploder(self):
    #     if self.flag:
    #         f = Fire()
    #         plist = []
    #         for i in range(20):
    #             plist.append(Particle(self.x, self.y, self.z, (random.random(), random.random(), random.random(), 1)))
    #         Fire.fireworks(plist)
    #
    #         self.flag = 0






class Fire:
    def __init__(self):
        pass

    def terrain(self):
        ''' Draws a simple square as the terrain '''
        glBegin(GL_QUADS)
        glColor4fv((0, 0, 1, 1))  # Colors are now: RGBA, A = alpha for opacity
        glVertex3fv((10, 0, 10))  # These are the xyz coords of 4 corners of flat terrain.
        glVertex3fv((-10, 0, 10))  # If you want to be fancy, you can replace this method
        glVertex3fv((-10, 0, -10))  # to draw the terrain from your prog1 instead.
        glVertex3fv((10, 0, -10))
        glEnd()


    def fireworks(self, plist):
        ''' Accepts a list of particles then draws and updates each particle '''
        # glEnable(GL_POINT_SMOOTH)
        # glPointSize(3)
        # glBegin(GL_POINTS)
        self.render(plist)


        # glEnd()

    def render(self, plist):

        for p in range(len(plist)):
            glEnable(GL_BLEND)
            glDisable(GL_DEPTH_TEST)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE)
            glPointSize(3)
            glBegin(GL_POINTS)
            glColor4fv(plist[p].color)
            glVertex3fv((plist[p].x, plist[p].y, plist[p].z))
            glEnd()





            for i in range(len(plist[p].trail)):
                # if p == 0:
                #     print(plist[p].colors[i])
                glEnable(GL_BLEND)
                glDisable(GL_DEPTH_TEST)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE)
                glPointSize(2)
                glBegin(GL_POINTS)

                glColor4fv((plist[p].colors[len(plist[p].trail)-1-i]))
                glVertex3fv((plist[p].trail[i][0], plist[p].trail[i][1], plist[p].trail[i][2]))
                glEnd()
            plist[p].update()



def main(number , cs):

    fire = Fire()
    pygame.init()

    # Set up the screen
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Firework Simulation")
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, -5, -25)
    # glRotatef(10, 2, 1, 0)

    play = True
    sim_time = 0

    # A clock object for keeping track of fps
    clock = pygame.time.Clock()

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(-10, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(10, 0, 1, 0)

                if event.key == pygame.K_UP:
                    glRotatef(-10, 1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(10, 1, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)

                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glRotatef(0.10, 0, 1, 0)
        # glTranslatef(0, 0.1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # terrain()
        fire.terrain()
        if 0 < sim_time <= 1000:
            fire.fireworks(plist1)

        if 200<sim_time <= 1000:

            fire.fireworks(plist6)

        if 500 < sim_time <= 1500:
            fire.fireworks(plist2)
            fire.fireworks(plist3)

        if 700<sim_time <= 1500:
            fire.fireworks(plist7)
            fire.fireworks(plist8)

        if 1000 < sim_time <= 1500:
            fire.fireworks(plist4)
            fire.fireworks(plist5)

        if 1200 < sim_time <= 1500:
            fire.fireworks(plist9)
            fire.fireworks(plist10)

        if 1500 < sim_time:
            sim_time = 0

        if sim_time == 0:
            plist1 = []
            plist2 = []
            plist3 = []
            plist4 = []
            plist5 = []

            for i in range(number):
                plist1.append(Particle(0, 0, 0, (random.random(), random.random(), random.random(), 1)))
                plist2.append(Particle(-5, 0, 5, cs[1]))
                plist3.append(Particle(-5, 0, -5, (random.random(), random.random(), random.random(), 1)))
                plist4.append(Particle(5, 0, -5, cs[3]))
                plist5.append(Particle(5, 0, 5, (random.random(), random.random(), random.random(), 1)))
        if sim_time == 200:
            plist6 = []
            for i in range(len(plist1)):
                for j in range(number):
                    plist6.append(Particle(plist1[i].x, plist1[i].y, plist1[i].z, (random.random(), random.random(), random.random(), 1), True))
        if sim_time == 700:
            plist7 = []
            for i in range(len(plist2)):
                for j in range(number):
                    plist7.append(Particle(plist2[i].x, plist2[i].y, plist2[i].z, (random.random(), random.random(), random.random(), 1), True))
            plist8 = []
            for i in range(len(plist3)):
                for j in range(number):
                    plist8.append(Particle(plist3[i].x, plist3[i].y, plist3[i].z,
                                          (random.random(), random.random(), random.random(), 1), True))

        if sim_time == 1200:
            plist9 = []
            for i in range(len(plist4)):
                for j in range(number):
                    plist9.append(Particle(plist4[i].x, plist4[i].y, plist4[i].z,
                                          (random.random(), random.random(), random.random(), 1), True))

            plist10 = []
            for i in range(len(plist5)):
                for j in range(number):
                    plist10.append(Particle(plist5[i].x, plist5[i].y, plist5[i].z,
                                          (random.random(), random.random(), random.random(), 1), True))

        pygame.display.flip()
        sim_time += 1
        clock.tick(150)

    pygame.quit()
