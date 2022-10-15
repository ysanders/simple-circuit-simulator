import unittest
import numpy as np
from gates import pauli, ionq_native
from register import QuantumRegister

class TestPauliMatrices(unittest.TestCase):

    def test_shapes(self):
        self.assertEqual(np.shape(pauli.I), (2, 2))
        self.assertEqual(np.shape(pauli.X), (2, 2))
        self.assertEqual(np.shape(pauli.Y), (2, 2))
        self.assertEqual(np.shape(pauli.Z), (2, 2))

#    def test_involutory(self):
#        self.assertTrue(np.allclose(pauli.X @ pauli.X, pauli.I))
#        self.assertTrue(np.allclose(pauli.Y @ pauli.Y, pauli.I))
#        self.assertTrue(np.allclose(pauli.Z @ pauli.Z, pauli.I))
#        self.assertTrue(np.allclose(-1j * pauli.X @ pauli.Y @ pauli.Z, pauli.I))

    def test_determinants(self):
        self.assertEqual(np.linalg.det(pauli.X), -1)
        self.assertEqual(np.linalg.det(pauli.Y), -1)
        self.assertEqual(np.linalg.det(pauli.Z), -1)

    def test_traces(self):
        self.assertEqual(np.trace(pauli.X), 0)
        self.assertEqual(np.trace(pauli.Y), 0)
        self.assertEqual(np.trace(pauli.Z), 0)

class TestIonQGates(unittest.TestCase):

    def test_shapes(self):
        self.assertEqual(np.shape(ionq_native.GPI(0)), (2, 2))
        self.assertEqual(np.shape(ionq_native.GPI2(0)), (2, 2))
        self.assertEqual(np.shape(ionq_native.RZ(0)), (2, 2))
        self.assertEqual(np.shape(ionq_native.MS(0, 0)), (4, 4))

    def test_periodicity(self):
        period = 4 * np.pi # NOT 2 * np.pi

        # single-qubit gates
        self.assertTrue(np.allclose(ionq_native.GPI(0),
                                    ionq_native.GPI(period)))
        self.assertTrue(np.allclose(ionq_native.GPI2(0),
                                    ionq_native.GPI2(period)))
        self.assertTrue(np.allclose(ionq_native.RZ(0),
                                    ionq_native.RZ(period)))

        # two-qubit gates
        self.assertTrue(np.allclose(ionq_native.MS(0, 0),
                                    ionq_native.MS(period, 0)))
        self.assertTrue(np.allclose(ionq_native.MS(0, 0),
                                    ionq_native.MS(period, 0)))
        self.assertTrue(np.allclose(ionq_native.MS(0, 0),
                                    ionq_native.MS(0, period)))
        self.assertTrue(np.allclose(ionq_native.MS(0, 0),
                                    ionq_native.MS(period, period)))



class TestQuantumCircuit(unittest.TestCase):

    def test_length(self):
        one_qubit_register = QuantumRegister(1)
        self.assertEqual(len(one_qubit_register), 1)
        self.assertEqual(len(one_qubit_register.state), 2)

        two_qubit_register = QuantumRegister(2)
        self.assertEqual(len(two_qubit_register), 2)
        self.assertEqual(len(two_qubit_register.state), 4)

    def test_initial_state(self):
        state_00 = np.array([1, 0, 0, 0])
        state_01 = np.array([0, 1, 0, 0])
        state_10 = np.array([0, 0, 1, 0])
        state_11 = np.array([0, 0, 0, 1])

        basic_init = QuantumRegister(2)
        init_0 = QuantumRegister(2, initial_state=0)
        init_1 = QuantumRegister(2, initial_state=1)
        init_2 = QuantumRegister(2, initial_state=2)
        init_3 = QuantumRegister(2, initial_state=3)
        init_00 = QuantumRegister(2, initial_state='00')
        init_01 = QuantumRegister(2, initial_state='01')
        init_10 = QuantumRegister(2, initial_state='10')
        init_11 = QuantumRegister(2, initial_state='11')

        self.assertTrue(np.allclose(basic_init.state, state_00))

        self.assertTrue(np.allclose(init_0.state, state_00))
        self.assertTrue(np.allclose(init_1.state, state_01))
        self.assertTrue(np.allclose(init_2.state, state_10))
        self.assertTrue(np.allclose(init_3.state, state_11))
 
        self.assertTrue(np.allclose(init_00.state, state_00))
        self.assertTrue(np.allclose(init_01.state, state_01))
        self.assertTrue(np.allclose(init_10.state, state_10))
        self.assertTrue(np.allclose(init_11.state, state_11))
