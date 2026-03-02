import numpy as np
from scipy import interpolate

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    return 546.8/v + 50.31 + 0.2584*v + 0.008210*v**2

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):
    distance_km, speed_kmph = load_route(route)
    
    assert x <= distance_km[-1], 'x cannot be larger than route length'
    

    strides = np.linspace(0, x, n+1)
    h = x/n
    integrands = 1 / velocity(strides, route)
    ends = integrands[[0, -1]]
    middle = 2 * integrands[1:-1]
    integral = (h/2)*(np.sum(ends) + np.sum(middle))
    
    return integral
#print(time_to_destination(15, "speed_elsa.npz", 1000000))
diff = 1
u=1
while diff > 0.016667:
    diff = time_to_destination(15, "speed_elsa.npz", u) -0.2276846457
    u = u+1
print("Här är antal n", u)

### PART 2B ###
def total_consumption(x, route, n):
    
    distance_km, speed_kmph = load_route(route)

    assert x <= distance_km[-1], 'x cannot be larger than route length'
    strides = np.linspace(0, x, n + 1)
    h = x/n
    
    integrands = consumption(velocity(strides, route))
    ends = integrands[[0, -1]]
    middle = 2 * integrands[1:-1]
    integral = (h/2)*(np.sum(ends) + np.sum(middle))
    
    return integral
    

### PART 3A ###
def distance(T, route): 
    n = 10000
    tol = 1e-4
    def F(x):
        return time_to_destination(x, route, n) - T
    def dF(x):
        return 1/velocity(x, route)
    
    x =T * velocity(0, route)
    for i in range(100):
        xn = x - F(x)/dF(x)
        if abs(xn-x) < tol:
            return xn
        x = xn
    return x
    #raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    n = 10000000
    tol = 1e-10
    d_km,h = load_route(route)
    d=d_km[-1]
   
    if total_consumption(d, route, n) <= C:
        return d
    def G(x):
        return total_consumption(x, route, n) - C
    def dG(x):
        h = 1e-5
        return (G(x + h) - G(x - h)) / (2*h)
    
    x = d/2
    for i in range(100):
        xn = x - G(x)/dG(x)
        xn = max(0, min(xn, d))
        if abs(xn-x) < tol:
            return xn
        x = xn
    return x
print(reach(10000, 'speed_anna.npz'))

