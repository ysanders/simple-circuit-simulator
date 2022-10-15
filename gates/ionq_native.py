# see: https://ionq.com/docs/getting-started-with-native-gates

import numpy as np
from .gate_class import QuantumGate


def GPI(phi : float):
    return np.array([[0, np.exp(-1j * phi)],
                     [np.exp( 1j * phi), 0]])

def GPI2(phi : float):
    return np.array([[1, -1j * np.exp(-1j * phi)],
                     [-1j * np.exp( 1j * phi), 1]]) / np.sqrt(2)

def RZ(theta : float):
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp( 1j * theta / 2)]])

def MS(phi_0 : float, phi_1 : float):
    return np.array([[1, 0, 0, -1j * np.exp(-1j * (phi_0 + phi_1))],
                     [0, 1, -1j * np.exp(-1j * (phi_0 - phi_1)), 0],
                     [0, -1j * np.exp( 1j * (phi_0 - phi_1)), 1, 0],
                     [-1j * np.exp( 1j * (phi_0 + phi_1)), 0, 0, 1]]) / np.sqrt(2)


class GeneralPi(QuantumGate):

    def __init__(self, angle):
        self.angle = angle
        self.matrix = GPI(angle)
        self.no_qubits = 1

    def __repr__(self):
        return f"GPI({self.angle:.4f})"

class GeneralPi2(QuantumGate):

    def __init__(self, angle):
        self.angle = angle
        self.matrix = GPI2(angle)
        self.no_qubits = 1

    def __repr__(self):
        return f"GPI2({self.angle:.4f})"

class VirtualZ(QuantumGate):

    def __init__(self, angle):
        self.angle = angle
        self.matrix = RZ(angle)
        self.no_qubits = 1

    def __repr__(self):
        return f"RZ({self.angle:.4f})"

class MolmerSorensen(QuantumGate):

    def __init__(self, angle_0, angle_1):
        self.angle_0 = angle_0
        self.angle_1 = angle_1
        self.matrix = MS(angle_0, angle_1)
        self.no_qubits = 2

    def __repr__(self):
        return f"MS({self.angle_0:.4f}, {self.angle_1:.4f})"
