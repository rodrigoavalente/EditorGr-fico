#!/usr/bin/env python
# -*- coding: utf8 -*-

import unittest
from matrix import Matrix
from editor_grafico import EditorGrafico


class EditorGraficoTest(unittest.TestCase):

    def test_instance(self):
        editor = EditorGrafico()
        self.assertIsInstance(editor, EditorGrafico)

    def test_set_command_true(self):
        editor = EditorGrafico()
        self.assertTrue(editor.execute_command("I 5 5"))

    def test_create_matrix(self):
        editor = EditorGrafico()
        editor.execute_command("I 5 5")
        matrix = Matrix(5, 5)
        self.assertEquals(editor.matrix(), matrix)

    def test_create_matrix_user_warning_more_arguments(self):
        editor = EditorGrafico()
        editor.execute_command("I 3 5 5")
        self.assertRaises(UserWarning)

    def test_create_matrix_user_warning_few_arguments(self):
        editor = EditorGrafico()
        editor.execute_command("I 3")
        self.assertRaises(UserWarning)

    def test_clear_empty_matrix(self):
        editor = EditorGrafico()
        editor.execute_command("C")
        self.assertRaises(UserWarning)

    def test_clear_zeros_matrix(self):
        editor = EditorGrafico()
        editor.execute_command("I 5 5")
        self.assertRaises(UserWarning)

    def test_to_color_pixel_empty(self):
        editor = EditorGrafico()
        editor.execute_command("L 1 2 A")
        self.assertRaises(UserWarning)

    def test_to_color_few_argments(self):
        editor = EditorGrafico()
        editor.execute_command("I 5 5")
        editor.execute_command("L 1 1")
        self.assertRaises(UserWarning)

    def test_to_color_wrong_row_value(self):
        editor = EditorGrafico()
        editor.execute_command("I 5 5")
        editor.execute_command("L A 1 C")
        self.assertRaises(ValueError)

    def test_to_color_wrong_column_value(self):
        editor = EditorGrafico()
        editor.execute_command("I 5 5")
        editor.execute_command("L 1 B C")
        self.assertRaises(ValueError)

    def test_to_color_result(self):
        editor = EditorGrafico()
        editor.execute_command("I 5 5")
        editor.execute_command("L 2 2 A")
        color = editor.matrix().get(2, 2)
        self.assertEquals(color, "A")

if __name__ == "__main__":
    unittest.main()
