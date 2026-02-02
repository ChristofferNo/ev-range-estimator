import roadster
import matplotlib.pyplot as plt
import numpy as np

distance_km, speed_kmph = roadster.load_route('speed_anna.npz')

x = np.linspace(0, 65, 10000)
v=roadster.velocity(x,'speed_anna')

plt.xlabel('km')
plt.ylabel('km/h')
plt.plot(x, v, label="Aprox with interpolation", color='yellow')
plt.plot(distance_km, speed_kmph, linestyle=':', label='data points', color='black')
plt.xlim(15, 20)

plt.legend()
plt.show()
