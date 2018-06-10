# -*- coding: utf-8 -*-

import numpy as np
from numpy import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def Rx(phi):
    return np.array([[1, 0, 0],
                     [0, np.cos(phi), -np.sin(phi)],
                     [0, np.sin(phi), np.cos(phi)]])

def Ry(theta):
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])

def Rz(psi):
    return np.array([[np.cos(psi), -np.sin(psi), 0],
                     [np.sin(psi), np.cos(psi), 0],
                     [0, 0, 1]])

def axisEqual3D(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

def plot_points_and_vectors(dict_tubavectors,dict_tubapoints):

    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111, projection='3d') 
    
    x=[]
    y=[]
    z=[]
       
    for point in dict_tubapoints:     
        x.append(point.pos.x)
        y.append(point.pos.y)            
        z.append(point.pos.z)
        
        if "center" not in point.name: 
            ax.text(point.pos.x, point.pos.y, point.pos.z, point.name,
                    color='white',size="medium",
                    horizontalalignment='center',
                    verticalalignment='center')
    ax.plot(x,y,z, 'o', markersize=15, color='g')
    
    
    x=[]
    y=[]
    z=[]
    Fx=[]
    Fy=[]
    Fz=[]
    for point in dict_tubapoints:
         
        for i,force in enumerate(point.force):
            x.append(point.pos.x)
            y.append(point.pos.y)            
            z.append(point.pos.z)
            Fx.append(force.x)
            Fy.append(force.y)    
            Fz.append(force.z) 
    ##Draw Force Arrows
    for i in range(0,len(x)):    
        b = Arrow3D([x[i], x[i]+Fx[i]], [y[i], y[i]+Fy[i]],[z[i], z[i]+Fz[i]], mutation_scale=20,lw=3,arrowstyle="-|>", color="r")   
        ax.add_artist(b)    
    
    
    
    x_lin=[]
    y_lin=[]
    z_lin=[]
    Fx_lin=[]
    Fy_lin=[]
    Fz_lin=[]



#------------------------------------------------------------------------------
#               Forces
#------------------------------------------------------------------------------
    for vector in dict_tubavectors:    
        for i, force in enumerate(vector.linear_force):
            x_lin=[]
            y_lin=[]
            z_lin=[]    
    
            for p in range(0,10): 
                x_lin.append(vector.start_tubapoint.pos.x+vector.vector.x/10*p)
                y_lin.append(vector.start_tubapoint.pos.y+vector.vector.y/10*p)            
                z_lin.append(vector.start_tubapoint.pos.z+vector.vector.z/10*p)          
            Fx_lin=force.x
            Fy_lin=force.y
            Fz_lin=force.z
    
            for p in range(0,10):    
                b = Arrow3D([x_lin[p], x_lin[p]+Fx_lin],
                            [y_lin[p], y_lin[p]+Fy_lin],
                            [z_lin[p], z_lin[p]+Fz_lin], 
                            mutation_scale=20,lw=3,arrowstyle="-|>", color="y")   
                ax.add_artist(b)

#------------------------------------------------------------------------------
#               Vectors / Piping
#------------------------------------------------------------------------------
    x_V_Start=[]
    y_V_Start=[]
    z_V_Start=[]
    x_V_Mid=[]
    y_V_Mid=[]
    z_V_Mid=[]
    x_V_End=[]
    y_V_End=[]
    z_V_End=[]

   #Draw Piping
    for vector in dict_tubavectors:
        x_V_Start.append(vector.start_tubapoint.pos.x)
        y_V_Start.append(vector.start_tubapoint.pos.y)
        z_V_Start.append(vector.start_tubapoint.pos.z)

        x_V_End.append(vector.end_tubapoint.pos.x)
        y_V_End.append(vector.end_tubapoint.pos.y)
        z_V_End.append(vector.end_tubapoint.pos.z)

        ax.text(vector.start_tubapoint.pos.x+0.5*vector.vector.x,
                vector.start_tubapoint.pos.y+0.5*vector.vector.y,
                vector.start_tubapoint.pos.z+0.5*vector.vector.z,
                vector.name, color='blue',size="large")


    for i in range(0,len(x_V_Start)):
        #a = Arrow3D([x[i], x[i+1]], [y[i], y[i+1]],[z[i], z[i+1]], mutation_scale=20,lw=3,arrowstyle="-|>", color="g")
        a = Arrow3D([x_V_Start[i], x_V_End[i]], [y_V_Start[i], y_V_End[i]], [z_V_Start[i], z_V_End[i]], mutation_scale=20,lw=1,arrowstyle="-|>", color="g")   
        ax.add_artist(a)






    ax.set_xlabel('x_values')
    ax.set_ylabel('y_values')
    ax.set_zlabel('z_values')
    axisEqual3D(ax)
    
    plt.draw()
    plt.show()
    plt.title('Visualization Piping')