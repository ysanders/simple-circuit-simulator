class QuantumRegister:

    def __init__(self, length : int, initial_state=None):
        self.state = np.zeros(length)

        if initial_state is None: # assume initial state is 0
            self.state[0] = 1

        elif type(initial_state) is int:
            assert initial_state >= 0 and initial_state < length
            self.state[initial_state] = 1

        else: # assume initial_state is binary string
            assert type(initial_state) is str
            assert len(initial_state) is length

            # The following asserts that initial_state is
            # of the form, e.g., '10' rather than '0b10',
            # which is the output of bin(2).
            chars = set(initial_state); bits = {'0', '1'}
            assert chars.union(bits) is bits

    def __len__(self):
        return len(self.state)

    def __repr__(self):
        return "QuantumRegister({})".format(len(self))
