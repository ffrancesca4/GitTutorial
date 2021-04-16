# import plot libraries libraries
	
from mpl_toolkits.mplot3d import Axes3D
	
import matplotlib.pyplot as plt
	
# import numpy linear algebra library
	
import numpy as np
	
 
	
# create figure and set it to 3d projection
	
fig = plt.figure()
	
ax = fig.gca(projection='3d')
	
 
	
# 1D arrays for x and y coordinates
	
n_points = 200
	
x_min,x_max = -5,5
	
y_min,y_max = -5,5
	
X = np.linspace(x_min,x_max, n_points)
	
Y = np.linspace(y_min,y_max, n_points)
	
 
	
# 2D X,Y grids from 1D arrays
	
X, Y = np.meshgrid(X, Y)
	
 
	
# Z 2D grid for the plot
	
R = np.sqrt(X**2 + Y**2)
	
Z = np.sin(R)
	
 
	
# plot the surface.
	
surf = ax.plot_surface(X, Y, Z, cmap='magma',linewidth=0, antialiased=True)
	
 
	
# Customize the z axis.
	
ax.set_zlim(-1.01, 1.01)
	
 
	
# Add a color bar
	
fig.colorbar(surf, shrink=0.5, aspect=5)
	
 
	
# plot
	
plt.show()

Close the file and run the code

$ python Plot3D.py

plot 3d
Stage, Status, Commit and Log

$ git add Plot3D.py # add the file to the staging area

$ git status # check the repository status

$ git commit -m "this is my first commit" # always include a meaningful commit message

$ git log # see the commit history

Let's modify the code
and stage and commit again

	
n_points = 500
	
Z = np.sin(R)
	
surf = ax.plot_surface(X, Y, Z, cmap='viridis',linewidth=0, antialiased=True)

Seeing the modifications
git diff
Creating a new branch

A branch is a new ramification of your code, where you might try out new features, without affecting your original code.

$ git branch develop # create a new branch whose name is develop

$ git checkout develop # move to the new branch

$ gedit Plot2D.py # create a new file inside the new branch

Copy-Paste the code below in Plot3D.py # import plot libraries libraries from mpl_toolkits.mplot3d import Axes3D import matplotlib.pyplot as plt # import numpy linear algebra library import numpy as np # create figure and set it to 3d projection fig = plt.figure() ax = fig.gca( projection='3d') # 1D arrays for x and y coordinates n_points = 200 x_min, x_max = - 5 , 5 y_min, y_max = - 5 , 5 X = np.linspace(x_min,x_max, n_points) Y = np.linspace(y_min,y_max, n_points) # 2D X,Y grids from 1D arrays X, Y = np.meshgrid(X, Y) # Z 2D grid for the plot R = np.sqrt(X** 2 + Y** 2 ) Z = np.sin(R) # plot the surface. surf = ax.plot_surface(X, Y, Z, cmap='magma',linewidth=0, antialiased=True) # Customize the z axis. ax.set_zlim(- 1.01 , 1.01 ) # Add a color bar fig.colorbar(surf, shrink=0.5, aspect=5) # plot plt.show() 
