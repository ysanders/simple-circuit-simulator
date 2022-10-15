import unittest
import numpy as np
from gates import pauli

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


