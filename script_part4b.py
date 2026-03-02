#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc

h = 0.1
t1, d1, s1 = route_nyc.nyc_route_traveler_euler(4, h)
t2, d2, s2 = route_nyc.nyc_route_traveler_euler(9.5, h)

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine,xx_fine,zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)
plt.plot(t1, d1, color='blue', label='Route 1 (start 04:00)')
plt.plot(t2, d2, color='green', label='Route 2 (start 09:30)')
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')
plt.legend()
plt.show()
