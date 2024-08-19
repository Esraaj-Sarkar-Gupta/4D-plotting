import time 
import os

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm


try:
    os.makedirs('./logs')
    makedirs_log = True
except:
    makedirs_log = False
    
try:
    os.makedirs('./plots')
except:
    pass
    
filename = './logs/log.txt'

def log(text):
    with open(filename , 'a') as file:
        T = time.localtime()
        file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n") # Writes log into the log file in special format

def log_display(text):
    with open(filename  , 'a') as file:
        T = time.localtime()
        file.write(f"\n(Disp) {T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n") # Writes log into the log file in special format
    print(f"{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}") # Prints log into the output console in special format    

log_display("Basic functions defined and imports completed")


space_var = 6

x_space = np.linspace(-space_var, space_var, 100)
y_space = np.linspace(-space_var, space_var, 100)
z_space = np.linspace(-space_var, space_var, 100)

log_display("Space limits defined")

def function(x_space , y_space , z_space):
    
    matrix = [[] for _ in range(len(x_space))]
    
    for n in range(len(x_space)):
        x = x_space[n]
        matrix[n].append(x)
        for _ in range(3):
            matrix[n].append([])
        for y in y_space:
            for z in z_space:
                w = np.sin(x**2 + y**2 + z**2)
                for _ in range(1):
                    matrix[n][1].append(y)
                for _ in range(1):
                    matrix[n][2].append(z)
                matrix[n][3].append(w)
    
    return matrix

log_display("Begin solving for system...")
start_time = time.time()

matrix = function(x_space, y_space , z_space)

end_time = time.time()
log_display(f"Finish solving for system in time {end_time - start_time} seconds")

log_display("Graphs are being generated...")

for i in range(len(x_space)):
    
    if i % 100 == 0:
        log_display(f"On iteration number {i}/{len(x_space)}")
    
    fig = plt.figure()
    ax = fig.add_subplot(111 , projection = '3d')

    ex = np.array(matrix[i][1])
    why = np.array(matrix[i][2])
    jed = np.array(matrix[i][3])
    
    ax.scatter(ex , why , jed , alpha = 0.5 , c = jed , cmap = 'viridis')
    ax.scatter(0,0,0, color = 'red')
    
    plot_variable = 6
    
    ax.set_xlim(-plot_variable , plot_variable)
    ax.set_ylim(-plot_variable , plot_variable)
    ax.set_zlim(-plot_variable , plot_variable)
    
    ax.set_xlabel('Y')
    ax.set_ylabel('Z')
    ax.set_zlabel('W')
    
    plt.title(f"System 3D slice  at X = {x_space[i]}")
    # plt.show()
    plt.savefig(f"./plots/plot_{i}.png")
log_display("Graphs finish rendering. END")

