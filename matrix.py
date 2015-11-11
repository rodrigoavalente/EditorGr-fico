#!/usr/bin/env python
# -*- coding: utf8 -*-


class Matrix():

    def __init__(self, rows=0, columns=0):
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
            self.__rows = rows
            self.__columns = columns
            self.__matrix = [[0 for x in range(columns)] for x in range(rows)]

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        string = ""
        for i in range(self.__rows):
            for j in range(self.__columns):
                if type(self.__matrix[i][j]) is str:
                    string = string + self.__matrix[i][j] + " "
                else:
                    string = string + str(self.__matrix[i][j]) + " "
            string += "\n"
        return string

    def get(self, row, column):
        try:
            if type(row) is not int:
                raise IndexError("O número de linhas fornecido é negativo.")

            elif row - 1 > self.__rows:
                raise IndexError("O número de linhas fornecido é\
                 maior que as dimensões da matriz.")

            elif row - 1 < 0:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de linhas.")

            if column - 1 < 0:
                raise IndexError("O número de colunas fornecido é negativo.")

            elif column > self.__columns:
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
            return self.__matrix[row - 1][column - 1]

    def set(self, row, column, value):
        try:
            if type(row) is not int:
                raise IndexError("O número de linhas fornecido é negativo.")
            elif row - 1 > self.__rows:
                raise IndexError("O número de linhas fornecido é\
                 maior que as dimensões da matriz.")
            elif row - 1 < 0:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de linhas.")

            if type(column) is not int:
                raise IndexError("O número de colunas fornecido é negativo.")
            elif column - 1 > self.__columns:
                raise IndexError("O número de colunas fornecido é\
                 maior que as dimensões da matriz.")
            elif column - 1 < 0:
                raise ValueError("Não foi fornecido um número\
                 inteiro para o número de colunas.")

            if type(value) is not str:
                if type(value) is not int:
                    if type(value) is not float:
                        raise ValueError("A matriz só aceita\
                         texto ou números.")
        except IndexError as error:
            print error.args[0]
        except ValueError as error:
            print error.args[0]
        else:
            self.__matrix[row - 1][column - 1] = value

    def rows(self):
        return self.__rows

    def columns(self):
        return self.__columns

    def is_empty(self):
        if not self.__matrix:
            return True
        else:
            return False

    def is_zeros(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.__matrix[i][j] != 0:
                    return False

        return True

    def zeros(self, rows=None, columns=None):
        if rows is None:
            rows = self.__rows
        if columns is None:
            columns = self.__columns
        self.__init__(rows, columns)

    def find_neighbors(self, row, column):
        neighbors = []
        if 1 < row < self.__rows:
            xi = (0, -1, 1)
        elif row > 1:
            xi = (0, -1)
        else:
            xi = (0, 1)

        if 1 < column < self.__columns:
            yi = (0, -1, 1)
        elif column > 1:
            yi = (0, -1)
        else:
            yi = (0, 1)

        for x in xi:
            for y in yi:
                if x == 0 == y:
                    continue
                elif (x + y) == 1 or (x + y) == -1:
                    neighbors.append((x + row, y + column))

        return neighbors


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
