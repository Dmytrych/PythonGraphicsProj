import matplotlib.pyplot as plt
from numpy import arange, sin

x_val = arange(-20.0, 20.0, 0.01)

figure = plt.figure(1)
plt.plot(x_val, sin(x_val), 'g^')

plt.show()
