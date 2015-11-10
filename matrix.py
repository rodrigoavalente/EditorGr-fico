#!/usr/bin/env python
# -*- coding: utf8 -*-


class Matrix():

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__matrix = [[0 for x in range(rows)] for x in range(columns)]

    def index(self, row, column):
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


def main():
    print "Criando matrix (5,5) e imprimindo-a:"
    matrix = Matrix(5, 5)
    print matrix
    print "Preenchendo a matriz com 1:"
    for i in range(matrix.rows()):
        for j in range(matrix.columns()):
            matrix[i][j] = 1
    print matrix


if __name__ == "__main__":
    main()
