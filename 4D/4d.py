print("Slicing 4D plots into multiple 3D plots")

import time 
import os

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm


try:
    os.makedirs('./logs') # Make a directory to save logs into (disused)
    makedirs_log = True
except:
    makedirs_log = False

try:
    os.makedirs('./plots') # Make directory to save plots into 
except:
    pass

filename = './logs/log.txt' # Define logfile (disused)

# Log functions:

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


space_var = 6 # Define variable limits variable

# Define variable limits and resolution:
x_space = np.linspace(-space_var, space_var, 100)
y_space = np.linspace(-space_var, space_var, 100)
z_space = np.linspace(-space_var, space_var, 100)

log_display("Space limits defined")

# Define function to solve for an equation and save values into a solution matrix:
def function(x_space , y_space , z_space):
    
    matrix = [[] for _ in range(len(x_space))] # Define matrix size corresponding to the resolution of solutions
    
    for n in range(len(x_space)):
        x = x_space[n]
        matrix[n].append(x) # Define x for which the rest of the variables will be solved for. Plots will be sliced across the x axis
        for _ in range(3):
            matrix[n].append([]) # Define elements in matrix to hold solutions
        for y in y_space: # y for all y values to be considered
            for z in z_space: # z for all z values to be considered
                w_pos = np.sqrt(25 - x**2 - y**2 - z**2) # Compute solution of w for given x , y and z
                w_neg = (-1) * np.sqrt(25 - x**2 - y**2 - z**2) # Compute negative solution (caused by square root plus-minus)
                
                # Store solutions:
                for _ in range(2):
                    matrix[n][1].append(y) 
                for _ in range(2):
                    matrix[n][2].append(z)
                matrix[n][3].append(w_pos)
                matrix[n][3].append(w_neg)
    
    return matrix # Function returns matrix as the solution of the system

log_display("Begin solving for system...")
start_time = time.time()

matrix = function(x_space, y_space , z_space) # Compute the solution using the defined function

end_time = time.time()
log_display(f"Finish solving for system in time {end_time - start_time} seconds")

log_display("Graphs are being generated...")

for i in range(len(x_space)): # Generate plots for every set of solutions computed
    
    if i % 100 == 0:
        log_display(f"On iteration number {i}/{len(x_space)}")
    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111 , projection = '3d')
    
    ax.plot(matrix[i][1] , matrix[i][2] , matrix[i][3] , alpha = 0.5)
    ax.scatter(0,0,0, color = 'red')
    
    plot_variable = 6
    
    ax.set_xlim(-plot_variable , plot_variable)
    ax.set_ylim(-plot_variable , plot_variable)
    ax.set_zlim(-plot_variable , plot_variable)
    
    ax.set_xlabel('Y')
    ax.set_ylabel('Z')
    ax.set_zlabel('W')
    
    plt.title(f"System 3D slice  at x = {x_space[i]}")
    # plt.show()
    plt.savefig(f"./plots/plot__{i}.png") # Save the plot into desired directory
    
log_display("Graphs finish rendering. END")

