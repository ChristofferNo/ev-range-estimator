### 2C
import numpy as np
import roadster
import matplotlib.pyplot as plt

def konvergensstudie(route, antal_n, x=65):
    värden = []
    n=50000
    list_n = []
    förväntat = []
    for i in range(antal_n):
        b = 2**i
        list_n.append(b)
        värden.append(abs((roadster.time_to_destination(x, route, b*n))- 0.9609402397659929))
        förväntat.append(1/(n))
    plt.loglog(list_n, värden)
    plt.plot(list_n, förväntat)
    plt.show()
    return värden[-1]
print(konvergensstudie('speed_elsa.npz', 8))





