#!/usr/bin/env python
# -*- coding: utf8 -*-

import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_instance(self):
        matrix = Matrix(3, 3)
        self.assertIsInstance(matrix, Matrix)

    def test_matrix_init_typerror(self):
        matrix = Matrix("1", 2)
        matrix = Matrix((1, 2), 2)
        matrix = Matrix(1, "2")
        matrix = Matrix(1, (1, 2))
        self.assertRaises(TypeError)

    def test_matrix_init_valuerror(self):
        matrix = Matrix(-1, 2)
        matrix = Matrix(1, -2)
        self.assertRaises(ValueError)

    def test_matrix_rows(self):
        matrix = Matrix(3, 3)
        self.assertEqual(matrix.rows(), 3)

    def test_row_out_of_range(self):
        matrix = Matrix(5, 5)
        value = matrix.get(5, 0)
        self.assertRaises(IndexError)

    def test_negative_row(self):
        matrix = Matrix(5, 5)
        value = matrix.get(-1, 0)
        self.assertRaises(IndexError)

    def test_wrong_type_row(self):
        matrix = Matrix(2, 3)
        value = matrix.get(1.5, 2)
        value = matrix.get("1", 2)
        self.assertRaises(TypeError)

    def test_column_out_of_range(self):
        matrix = Matrix(5, 5)
        value = matrix.get(0, 5)
        self.assertRaises(IndexError)

    def test_negative_column(self):
        matrix = Matrix(5, 5)
        value = matrix.get(0, -1)
        self.assertRaises(IndexError)

    def test_wrong_type_column(self):
        matrix = Matrix(5, 5)
        value = matrix.get(0, 1.5)
        value = matrix.get(0, "1")
        self.assertRaises(ValueError)

    def test_get_value(self):
        matrix = Matrix(7, 8)
        value = matrix.get(1, 6)
        self.assertEqual(value, 0)

    def test_set_value(self):
        matrix = Matrix(8, 8)
        matrix.set(8, 8, 15)
        self.assertEquals(matrix.get(8, 8), 15)

    def test_matrix_eq(self):
        matrix1 = Matrix(2, 3)
        matrix2 = Matrix(2, 3)
        self.assertEquals(matrix1, matrix2)

    def test_matrix_ne(self):
        matrix1 = Matrix(1, 1)
        matrix2 = Matrix(3, 3)
        self.assertNotEquals(matrix1, matrix2)

    def test_matrix_is_empty(self):
        matrix = Matrix()
        self.assertTrue(matrix.is_empty())

    def test_matrix_is_zeros(self):
        matrix = Matrix(5, 5)
        self.assertTrue(matrix.is_zeros())

    def test_matrix_zeros(self):
        matrix = Matrix(5, 5)
        matrix.zeros(3, 3)
        self.assertEquals(matrix, Matrix(3, 3))

    def test_matrix_empty_zeros(self):
        matrix = Matrix(5, 5)
        self.assertFalse(matrix.is_empty())

if __name__ == "__main__":
    unittest.main()
