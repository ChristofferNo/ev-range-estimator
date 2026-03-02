### 2C
import numpy as np
import roadster
import matplotlib.pyplot as plt

def konvergensstudie(route, antal_n, x=65):
    felvärden = []
    n=1
    list_n = []
    förväntat = []
    while n < 500000000:
        
        list_n.append(n)
        felvärden.append(abs((roadster.time_to_destination(x, route, n))- 0.9609402397659929))
        förväntat.append(1/((n)**2))
        n=2*n
    plt.loglog(list_n, felvärden, label = "konvergens")
    plt.plot(list_n, förväntat, label="förväntad konvergens")
    plt.xlabel("n, antal delintervall")
    plt.ylabel("integrationsfel")
    plt.title("Konvergensstudie av integral")
    plt.legend()
    plt.show()
    return felvärden[-1]





