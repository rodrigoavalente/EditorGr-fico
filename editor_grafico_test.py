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
        self.assertTrue(editor.set_command("I 5 5"))

    def test_set_command_false(self):
        editor = EditorGrafico()
        self.assertFalse(editor.set_command(2))

    def test_set_command_exception(self):
        editor = EditorGrafico()
        editor.set_command(25)
        self.assertRaises(TypeError)

    def test_has_command(self):
        editor = EditorGrafico()
        editor.execute_command()
        self.assertRaises(IndexError)

    def test_execute_command(self):
        editor = EditorGrafico()
        editor.set_command("I 5 5")
        self.assertIsInstance(editor.execute_command(), str)
        editor.set_command("C")
        self.assertIsInstance(editor.execute_command(), str)

    def test_create_matrix(self):
        editor = EditorGrafico()
        editor.set_command("I 5 5")
        editor.execute_command()
        matrix = Matrix(5, 5)
        self.assertEquals(editor.matrix(), matrix)

    def test_create_matrix_user_warning_more_arguments(self):
        editor = EditorGrafico()
        editor.set_command("I 3 5 5")
        editor.execute_command()
        self.assertRaises(UserWarning)

    def test_create_matrix_user_warning_few_arguments(self):
        editor = EditorGrafico()
        editor.set_command("I 3")
        editor.execute_command()
        self.assertRaises(UserWarning)

if __name__ == "__main__":
    unittest.main()
