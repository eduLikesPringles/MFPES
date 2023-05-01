import numpy as np
import matplotlib.pyplot as plt

x = [0, 5, 17, 23]
y = [0, 100, 100, 190]

fig, ax = plt.subplots()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# Major ticks every 20, minor ticks every 5
"""y_major_ticks = np.arange(0, 200, 50)
y_minor_ticks = np.arange(0, 200, 2)
x_major_ticks = np.arange(0, 25, 5)
x_minor_ticks = np.arange(0, 40, 2)

ax.set_xticks(x_major_ticks)
ax.set_xticks(x_minor_ticks, minor=True)
ax.set_yticks(y_major_ticks)
ax.set_yticks(y_minor_ticks, minor=True)

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)"""

plt.plot(x, y)
plt.title("")
plt.xlabel("d (km)")
plt.ylabel("t (h)")
plt.xlim(0, 23)
plt.ylim(0, 190)
plt.grid()
plt.show()

plt.show()
# print(x[10])
"""
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np


offCoord = [[50/2, 30/2]]

fig, ax = plt.subplots(1)
ax.set_aspect('equal')

for c in offCoord:
    # fix radius here
    hexagon = RegularPolygon((c[0], c[1]), numVertices=6, radius=np.sqrt(25), alpha=0.2, edgecolor='k')
    ax.add_patch(hexagon)
plt.autoscale(enable = True)
plt.grid()
plt.title("")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.xlim(0,50)
plt.ylim(0, 30)
plt.show()"""