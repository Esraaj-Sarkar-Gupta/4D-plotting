# THIS IS A TEST FILE 

print("Slicing 3D plots into multiple 2D plots")
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

space_var = 6

x_space = np.linspace(-space_var , space_var , 1000)
y_space = np.linspace(-space_var, space_var , 1000)

def function(x_space , y_space):
    
    matrix = [[] for _ in range(len(x_space))]
    
    for n in range(len(x_space)):
        x = x_space[n]
        matrix[n].append(x)
        for _ in range(2):
            matrix[n].append([])
        for y in y_space:
            z = np.sqrt(25 - x**2 - y**2)
            z_neg = (-1) * np.sqrt(25 - x**2 - y**2)
            matrix[n][1].append(y)
            matrix[n][1].append(y)
            matrix[n][2].append(z)
            matrix[n][2].append(z_neg)
    
    return matrix

matrix = function(x_space, y_space)
#print(matrix)

for i in range(len(x_space)):
    plt.figure()
    plt.plot(matrix[i][1] , matrix[i][2])
    
    plt.xlim(-10 , 10)
    plt.ylim(-10 , 10)
    
    plt.xlabel("X")
    plt.ylabel("Y")
    
    plt.title(f"Section at x = {x_space[i]}")
    plt.gca().set_aspect('equal')

    
    plt.show()


    
    