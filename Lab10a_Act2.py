# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab10a_Act2
# Date:         12 November 2021

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
import matplotlib.pyplot as plt

# Plot 1
# equation: y = 1/(4f) * x^2
x_plot1 = np.linspace(-2, 2, 100)
y1_plot1 = 1/8 * x_plot1**2 # f = 2
y2_plot1 = 1/24 * x_plot1**2 # f = 6
plt.plot(x_plot1, y1_plot1, 'r', linewidth = 2.0, label = 'f=2')
plt.plot(x_plot1, y2_plot1, 'b', linewidth = 6.0, label = 'f=6')
plt.title('Parabola plots with varying focal length')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2.25, 2.25, -0.025, 0.525])
plt.legend(loc = 'lower left')
plt.show()


# Plot 2
# equation: 2x^3 + 3x^2 - 11x - 6
x_plot2 = np.linspace(-4, 4, 25) # creates 25 points
y_plot2 = (2 * x_plot2**3) + (3 * x_plot2**2) - (11 * x_plot2) - 6
plt.plot(x_plot2, y_plot2, 'y*', markeredgecolor = "k", markersize = '10') # yellow stars, black border
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot of cubic polynomial')
plt.axis([-4.5, 4.5, -51, 135])
plt.show()


# Plot 3
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
# allows for top subplot to not have x axis labels

# Plot 3a
# equation: y = cos(x)
plt.subplot(2, 1, 1)
x_plot3a = np.linspace(-2*np.pi, 2*np.pi, 100)
y_plot3a = np.cos(x_plot3a)
plt.plot(x_plot3a, y_plot3a, color = 'maroon', label = 'cos(x)')
plt.ylabel('y=cos(x)')
plt.legend(loc = 'lower right')
plt.grid(True)
plt.xlabel('')
plt.title('Plot of cos(x) and sin(x)')

# Plot 3b
# equation: y = sin(x)
plt.subplot(2, 1, 2)
x_plot3b = np.linspace(-2*np.pi, 2*np.pi, 100)
y_plot3b = np.sin(x_plot3a)
plt.plot(x_plot3b, y_plot3b, color = 'dimgray', label = 'sin(x)')
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.axis([-7, 7, -1.1, 1.1])
plt.legend(loc = 'upper right')
plt.grid(True)
plt.show()