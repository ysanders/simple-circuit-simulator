# see: https://ionq.com/docs/getting-started-with-native-gates

import numpy as np

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
                     [0, -1j * np.exp(-1j * (phi_0 - phi_1)), 1, 0],
                     [-1j * np.exp( 1j * (phi_0 + phi_1)), 0, 0, 1]]) / np.sqrt(2)
