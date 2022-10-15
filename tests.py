import unittest
import numpy as np
from gates import pauli, ionq_native

class TestPauliMatrices(unittest.TestCase):

    def test_shapes(self):
        self.assertEqual(np.shape(pauli.I), (2, 2))
        self.assertEqual(np.shape(pauli.X), (2, 2))
        self.assertEqual(np.shape(pauli.Y), (2, 2))
        self.assertEqual(np.shape(pauli.Z), (2, 2))

    def test_involutory(self):
        self.assertTrue(np.allclose(pauli.X @ pauli.X, pauli.I))
        self.assertTrue(np.allclose(pauli.Y @ pauli.Y, pauli.I))
        self.assertTrue(np.allclose(pauli.Z @ pauli.Z, pauli.I))
        self.assertTrue(np.allclose(-1j * pauli.X @ pauli.Y @ pauli.Z, pauli.I))

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

