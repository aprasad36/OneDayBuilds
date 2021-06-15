import numpy as np

class Neuron:
    def __init__(self, w, b, activation = None):
        #so now
        self.w = w
        self.b = b
        self.activation = activation

        #and then
    def plotpoints(self, xs: np.ndarray):
        #actually this is the plots to point at
        return self.w * xs + self.b

class Identity:
    def __init__(self):
        pass

    @staticmethod
    def calculate(v):
        return v

class ReLU:
    def __init__(self):
        pass

    @staticmethod
    def calculate(vs: np.ndarray):
        return np.array([0 if v < 0 else v for v in vs])
