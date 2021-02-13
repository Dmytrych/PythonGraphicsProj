import matplotlib.pyplot as plt
from numpy import arange, sin, log

x_val = arange(0, 100.0, 0.01)

figure = plt.figure(1)
plt.plot(x_val, log(x_val)/x_val, 'g^')

plt.show()
