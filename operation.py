import numpy as np
from .gates.gate_class import QuantumGate
from .register import QuantumRegister

def validate_register_locations(locations : tuple,
                                register_size : int):

    if any((type(loc) is not int) for loc in locations):
        raise AssertionError("Register location(s) must be of type int.")

    if any((loc >= 0) and (loc < register_size) for loc in locations):
        raise AssertionError("A register location is out of bounds.")

    if len(locations) != len(set(locations)):
        raise AssertionError("A register location is repeated.")

class QuantumOperation:

    def __init__(self,
                 register : QuantumRegister,
                 gate : QuantumGate,
                 *target,
                 ctrl=None):

        target_tuple = tuple(target)

        try:
            validate_register_locations(target_tuple, len(register))

        except:
            print("Failed to validate gate target locations.")
            raise

        assert len(target_tuple) == gate.num_qubits,\
                "Incorrect number of gate target(s) given."

        if ctrl is not None:
            try:
                validate_register_locations(ctrl, len(register))
            
            except:
                print("Failed to validate gate control locations.")
                raise

            assert len(set(target).intersection(set(ctrl))) == 0,\
                    "No location should be both a target and a control."

        self.gate = gate
        self.register = register
        self.target = target_tuple
        self.ctrl = ctrl
        self._compiled = False

    def __call__(self):
        if not self._compiled:
            self.compile()
            self._compiled = True

        self.register.state = np.dot(self.matrix, self.register.state)
        return self.register

    def compile(self):
        pass # to do

