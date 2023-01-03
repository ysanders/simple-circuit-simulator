import numpy as np

class QuantumGate:

    def __init__(self, matrix : np.ndarray, name=None):
        self.name = name

        assert len(matrix.shape) == 2
        assert matrix.shape[0] == matrix.shape[1]

        num_qubits = np.log2(len(matrix))
        assert int(num_qubits) == num_qubits
        self.num_qubits = int(num_qubits)

        # assume multiqubit gates do NOT commute with swaps
        self.ordered = (self.num_qubits > 1) 

        self.matrix = matrix

    def __repr__(self):
        if self.name is None:
            return f"QuantumGate({self.num_qubits})"
        else:
            return self.name

    def __array__(self):
        return self.matrix

def IdentityGate(num_qubits):
    return QuantumGate(np.identity(2 ** num_qubits),
                       name=f"IdentityGate({num_qubits})")
