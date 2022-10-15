# see: https://ionq.com/docs/getting-started-with-native-gates

import numpy as np
from .gate_class import QuantumGate

class GeneralPi(QuantumGate):
    def __init__(self, phi):
        self.phi = phi
        mtx = np.array([[0, np.exp(-1j * phi)],
                        [np.exp( 1j * phi), 0]])
        super().__init__(mtx, name=f"GPI({phi:.4f})")

class GeneralPi2(QuantumGate):
    def __init__(self, phi):
        self.phi = phi
        mtx = np.array([[1, -1j * np.exp(-1j * phi)],
                        [-1j * np.exp( 1j * phi), 1]])
        mtx /= np.sqrt(2)
        super().__init__(mtx, name=f"GPI2({phi:.4f})")

class VirtualZ(QuantumGate):
    def __init__(self, angle):
        self.theta = theta
        mtx = np.array([[np.exp(-1j * theta / 2), 0],
                        [0, np.exp( 1j * theta / 2)]])
        super().__init__(mtx, name=f"RZ({theta:.4f})")

class MolmerSorensen(QuantumGate):
    def __init__(self, phi_0, phi_1):
        self.phi_0 = phi_0; self.phi_1 = phi_1
        mtx = np.array([[1, 0, 0, -1j * np.exp(-1j * (phi_0 + phi_1))],
                        [0, 1, -1j * np.exp(-1j * (phi_0 - phi_1)), 0],
                        [0, -1j * np.exp( 1j * (phi_0 - phi_1)), 1, 0],
                        [-1j * np.exp( 1j * (phi_0 + phi_1)), 0, 0, 1]])
        mtx /= np.sqrt(2)
        super().__init__(mtx, name=f"MS({phi_0:.4f}, {phi_1:.4f})")
