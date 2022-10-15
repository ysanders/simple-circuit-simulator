import numpy as np

class QuantumRegister:

    def __init__(self, length : int, initial_state=None):
        self._len = length
        self.state = np.zeros(2 ** length)

        if initial_state is None: # assume initial state is 0
            self.state[0] = 1

        elif type(initial_state) is int:
            assert initial_state >= 0 and initial_state < 2 ** length
            self.state[initial_state] = 1

        else: # assume initial_state is binary string
            assert type(initial_state) is str
            assert len(initial_state) is length

            # The following asserts that initial_state is
            # of the form, e.g., '10' rather than '0b10',
            # which is the output of bin(2).
            chars = set(initial_state); bits = {'0', '1'}
            assert chars.union(bits) == bits

           # Now we can safely add the 1 to the state vector.
            addr = int('0b' + initial_state, 2)
            self.state[addr] = 1

    def __len__(self):
        return self._len

    def __repr__(self):
        return "QuantumRegister({})".format(len(self))
