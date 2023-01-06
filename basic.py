from ..gate import QuantumGate
import numpy as np

def IdentityGate(num_qubits):
    matrix = np.identity(2 ** num_qubits)
    name = f"IdentityGate({num_qubits})"
    return QuantumGate(matrix, name=name)

def HadamardGate(diagonal_element, antidiagonal_element):
    matrix = np.array([[diagonal_element,      antidiagonal_element],
                       [antidiagonal_element, -1 * diagonal_element]])
    matrix /= (diagonal_element**2 + antidiagonal_element**2)
    assert matrix @ matrix == np.identity(2)
    name = f"Hadamard({diagonal_element}, {antidiagonal_element})"
    return QuantumGate(matrix, name=name)

def RotationGate(theta):
    matrix = np.array([[np.cos(theta), -np.sin(theta)],
                       [np.sin(theta),  np.cos(theta)]])
    name = f"Rotation({theta:.3f})"
    return QuantumGate(matrix, name=name)
