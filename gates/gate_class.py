import numpy as np

class QuantumGate:

    def __init__(self, matrix, name=None):
        self.name = name

        assert len(matrix.shape) == 2
        assert matrix.shape[0] == matrix.shape[1]

        no_qubits = np.log2(len(matrix))
        assert int(no_qubits) == no_qubits
        self.no_qubits = int(no_qubits)

        self.matrix = matrix

    def __repr__(self):
        if self.name is None:
            return f"QuantumGate({self.no_qubits})"
        else:
            return self.name

    def __array__(self):
        return self.matrix

def IdentityGate(no_qubits):
    return QuantumGate(np.identity(2 ** no_qubits),
                       name=f"IdentityGate{no_qubits}")
