#!/usr/bin/env python
# -*- coding: utf8 -*-


class Matrix():

    def __init__(self, rows=0, columns=0):
        self.__rows = rows
        self.__columns = columns
        try:
            if type(rows) is not int:
                raise TypeError("O valor passado não é um número inteiro.")
            elif rows < 0:
                raise ValueError("Não é possível iniciar a matriz \
                    com o número de linhas negativo.")

            if type(columns) is not int:
                raise TypeError("O valor passado não é um número inteiro.")
            elif columns < 0:
                raise ValueError("Não é possível iniciar a matriz \
                    com o número de colunas negativo.")
        except TypeError as error:
            print error.args[0]
        except ValueError as error:
            print error.args[0]
        else:
            self.__matrix = [[0 for x in range(rows)] for x in range(columns)]

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def get(self, row, column):
        try:
            if row < 0:
                raise IndexError("O número de linhas fornecido é negativo.")
            elif row >= self.__rows:
                raise IndexError("O número de linhas fornecido é\
                 maior que as dimensões da matriz.")
            elif type(row) is not int:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de linhas.")
            if column < 0:
                raise IndexError("O número de colunas fornecido é negativo.")
            elif column >= self.__columns:
                raise IndexError("O número de colunas fornecido é\
                 maior que as dimensões da matriz.")
            elif type(column) is not int:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de colunas.")

        except IndexError as error:
            print error.args[0]
        except ValueError as error:
            print error.args[0]
        else:
            return self.__matrix[row][column]

    def set(self, row, column, value):
        try:
            if row < 0:
                raise IndexError("O número de linhas fornecido é negativo.")
            elif row >= self.__rows:
                raise IndexError("O número de linhas fornecido é\
                 maior que as dimensões da matriz.")
            elif type(row) is not int:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de linhas.")
            if column < 0:
                raise IndexError("O número de colunas fornecido é negativo.")
            elif column >= self.__columns:
                raise IndexError("O número de colunas fornecido é\
                 maior que as dimensões da matriz.")
            elif type(column) is not int:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de colunas.")

        except IndexError as error:
            print error.args[0]
        except ValueError as error:
            print error.args[0]
        else:
            self.__matrix[row][column] = value

    def __str__(self):
        string = ""
        for i in range(self.__rows):
            for j in range(self.__columns):
                string = string + str(self.__matrix[i][j]) + " "
            string += "\n"
        return string

    def rows(self):
        return self.__rows

    def columns(self):
        return self.__columns

    def is_empty(self):
        if not self.__matrix:
            return True
        else:
            return False


def main():
    print "Criando matrix (5,5) e imprimindo-a:"
    matrix = Matrix(5, 5)
    matrix2 = Matrix(5, 5)
    print matrix
    print "Preenchendo a matriz com 1:"
    for i in range(matrix.rows()):
        for j in range(matrix.columns()):
            matrix.set(i, j, 1)
    print matrix


if __name__ == "__main__":
    main()
