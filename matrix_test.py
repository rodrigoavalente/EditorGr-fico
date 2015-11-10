#!/usr/bin/env python

import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_matrix_rows(self):
        matrix = Matrix(3, 3)
        self.assertEqual(matrix.rows(), 3)

    def test_row_out_of_range(self):
        matrix = Matrix(5, 5)
        value = matrix.index(5, 0)
        self.assertRaises(IndexError)

    def test_negative_row(self):
        matrix = Matrix(5, 5)
        value = matrix.index(-1, 0)
        self.assertRaises(IndexError)

    def test_wrong_type_row(self):
        matrix = Matrix(2, 3)
        value = matrix.index(1.5, 2)
        value = matrix.index("1", 2)
        self.assertRaises(TypeError)

    def test_column_out_of_range(self):
        matrix = Matrix(5, 5)
        value = matrix.index(0, 5)
        self.assertRaises(IndexError)

    def test_negative_column(self):
        matrix = Matrix(5, 5)
        value = matrix.index(0, -1)
        self.assertRaises(IndexError)

    def test_wrong_type_column(self):
        matrix = Matrix(5, 5)
        value = matrix.index(0, 1.5)
        value = matrix.index(0, "1")
        self.assertRaises(ValueError)


if __name__ == "__main__":
    unittest.main()
