# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:50:29 2021

@author: imrini
"""

import numpy as np
import matplotlib.pyplot as plt


xmin, xmax = plt.xlim(-10, 10)  # pour délimiter la fenêtre
ymin, ymax = plt.ylim(-7, 7)


def trace_cercle(a, b, r):
    t = np.linspace(0, np.pi*2,100)
    x = a + np.cos(t)*r
    y = b + np.sin(t)*r
    plt.plot(x,y,'black')
    
def visu_point(matPoint,style):
    # matPoint contient les coordonnées des points 
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)
    
def mat_Translation_h(tx,ty):
    mat = np.array([[1, 0, tx],
                    [0, 1, ty],
                    [0, 0, 1]])
    return mat

def mat_Scale_h(sx,sy):
    mat = np.array([[sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]])
    return mat
    
def mat_Rotation_h(theta):
    mat = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    return mat
    


def visu_BezierQuad(matPointControl,str):
    
    n=50
    mt = np.linspace(0,1.,n)  
    matt = np.ones((3,n))  # que des 1
    matt[1,:] = mt  # ligne avec les t
    matt[2,:] = mt*mt  # ligne avec les t*t

    matBezier3 = np.array([[1, 0, 0], 
                           [-2, 2, 0], 
                           [1, -2, 1]])

    matPointligne = np.dot(np.dot(matt.T,matBezier3),matPointControl.T)
    matPoint=matPointligne.T  # on transpose

    visu_point(matPointControl,'r.')
    visu_point(matPointControl,'b:')
    visu_point(matPoint,str)
    
def dessin_oeil():
    rayon= 6
    trace_cercle(-1,0,rayon)
    
    rp = 0.5
    trace_cercle(-1,0,rp)
    
def trace_tomoe(tab1,tab2):         
    visu_BezierQuad(tab1, 'black')
    visu_BezierQuad(tab2, 'black')



def rotation_tomoe(tab,teta):
    ro = np.dot(mat_Rotation_h(teta), tab)
    return ro

def trans_tomoe(tab,tx,ty):
    sc = np.dot(mat_Translation_h(tx, ty), tab)
    return sc



#Methode qui nous permettera de dessiner le tomoé en bas a droite
def trace_tomoe2(tab1,tab2):
    #on fais une transformation géométriques une rotation pour le 2e tomoe
    rtomoe1_deux = rotation_tomoe(tab1,4*np.pi/3) 
    rtomoe2_deux = rotation_tomoe(tab2,4*np.pi/3)
                   
    #on translate afin que les deux tomoe se collent
    ttomoe1_deux = trans_tomoe(rtomoe1_deux,-1.60,-0.90)
    ttomoe2_deux = trans_tomoe(rtomoe2_deux,-1.60,-0.90)
    

    #on dessine apres la rotation et la translation
    trace_tomoe(ttomoe1_deux,ttomoe2_deux)
    
def trace_tomoe3(tab1,tab2):
    rtomoe1_trois = rotation_tomoe(tab1,2*np.pi/3) 
    rtomoe2_trois = rotation_tomoe(tab2,2*np.pi/3)
    
    ttomoe1_trois = trans_tomoe(rtomoe1_trois,-1.57,1.0)
    ttomoe2_trois = trans_tomoe(rtomoe2_trois,-1.57,1.0)
    
    trace_tomoe(ttomoe1_trois, ttomoe2_trois)
    
#on initialise le tomoe de base
tomoe1 = np.array([[-2.5 ,-1.5 , 0.75],[1 ,5.5 ,5.45],[1 ,1 ,1]])
tomoe2 = np.array([[0.75 ,-1.25 , 0.5],[5.45 ,3 ,0.75], [1 ,1 ,1]])  
   

#Dessin des tomoe
trace_tomoe(tomoe1,tomoe2)
trace_tomoe2(tomoe1,tomoe2);
trace_tomoe3(tomoe1, tomoe2)

dessin_oeil()

