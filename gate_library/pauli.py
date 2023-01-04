import numpy as np
from .gate_class import QuantumGate, IdentityGate

I = IdentityGate(1)
X = QuantumGate(np.array([[0, 1], [1, 0]]), name="X")
Y = QuantumGate(np.array([[0, -1j], [1j, 0]]), name="Y")
Z = QuantumGate(np.array([[1, 0], [0, -1]]), name="Z")
