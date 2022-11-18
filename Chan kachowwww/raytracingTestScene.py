#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def create_Ray(O, D):
    # Remplissez ici 
    return

def create_Sphere(P, r, i):
    # Remplissez ici
    return
    
def create_Plane(P, n, i):
    # Remplissez ici 
    return

def normalize(x):
    # Remplissez ici 
    return

def rayAt(ray,t):
    # Remplissez ici 
    return

def get_Normal(obj, M):
    # Remplissez ici 
    return 

def intersect_Plane(ray, plane):
    # Remplissez ici 
    return

def intersect_Sphere(ray, sphere):
    # Remplissez ici 
    return

def intersect_Scene(ray, obj):
    # Remplissez ici 
    return

def Is_in_Shadow(obj_min,P,N):
    # Remplissez ici 
    return 


def eclairage(obj,light,P) : 
    # Remplissez ici 
    return 

def reflected_ray(dirRay,N):
    # Remplissez ici 
    return

def compute_reflection(rayTest,depth_max,col):
    # Remplissez ici 
    return col 

def trace_ray(ray):
    # Remplissez ici 
    return 


# Taille de l'image
w = 800
h = 600
acne_eps = 1e-4
materialShininess = 50


img = np.zeros((h, w, 3)) # image vide : que du noir
#Aspect ratio
r = float(w) / h
# coordonnées de l'écran : x0, y0, x1, y1.
S = (-1., -1. / r , 1., 1. / r )


# Position et couleur de la source lumineuse
Light = { 'position': np.array([5, 5, 0]),
          'ambient': np.array([0.05, 0.05, 0.05]),
          'diffuse': np.array([1, 1, 1]),
          'specular': np.array([1, 1, 1]) }

L = Light['position']


col = np.array([0.2, 0.2, 0.7])  # couleur de base
C = np.array([0., 0.1, 1.1])  # Coordonée du centre de la camera.
Q = np.array([0,0.3,0])  # Orientation de la caméra
img = np.zeros((h, w, 3)) # image vide : que du noir
materialShininess = 50
skyColor = np.array([0.321, 0.752, 0.850])
whiteColor = np.array([1,1,1])
depth_max = 10

scene = [create_sphere([.75, -.3, -1.], # Position
                         .6, # Rayon
                         #np.array([1. , 0.6, 0. ]), # ambiant
                         #np.array([1. , 0.6, 0. ]), # diffuse
                         #np.array([1, 1, 1]), # specular
                         #0.2, # reflection index
                         1), # index
          create_plane([0., -.9, 0.], # Position
                         [0, 1, 0], # Normal
                         #np.array([0.145, 0.584, 0.854]), # ambiant
                         #np.array([0.145, 0.584, 0.854]), # diffuse
                         #np.array([1, 1, 1]), # specular
                         #0.7, # reflection index
                         2), # index
         ]

# Loop through all pixels.
for i, x in enumerate(np.linspace(S[0], S[2], w)):
    if i % 10 == 0:
        print(i / float(w) * 100, "%")
    for j, y in enumerate(np.linspace(S[1], S[3], h)):
        #Remplisssez votre code ici
        img[h - j - 1, i, :] = np.clip(col, 0, 1) # la fonction clip permet de "forcer" col a être dans [0,1]

plt.imsave('figRaytracing.png', img)