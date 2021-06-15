import numpy as np
import matplotlib.pyplot as plt
from bases import *

xs = np.arange(-10, 10, .1)
#print(xs)
neuron1 = Neuron(2, 1)
ys = neuron1.plotpoints(xs)
#print(ys)
ys_with_relu = ReLU.calculate(neuron1.plotpoints(xs))
#print(ys_with_relu)

plt.plot(xs, ys, 'r--', xs, ys_with_relu, 'b--')
plt.show()
