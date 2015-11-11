# !/usr/bin/python
# -*- coding: utf8 -*-
"""
Explicação:
Dada uma matriz de tamanho MxN na qual cada elemento represente um pixel, crie
um programa que leia uma sequência de comandos e os interprete manipulando a
matriz de acordo com a descrição abaixo de cada comando.

Comandos:
I M N
Cria uma nova matriz MxN. Todos os pixels são brancos (O).

C
Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam brancos (O).

L X Y C
Colore um pixel de coordenadas (X,Y) na cor C.

V X Y1 Y2 C
Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
inclusivo) na cor C.

H X1 X2 Y C
Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo
inclusivo) na cor C.

K X1 Y1 X2 Y2 C
Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e (X2,Y2) o
canto inferior direito.

F X Y C
Preenche a região com a cor C. A região R é definida da seguinte forma:
O pixel (X,Y) pertence à região. Outro pixel pertence à região,
se e somente se, ele tiver a mesma cor que o pixel (X,Y) e tiver pelo
menos um lado em comum com um pixel pertencente à região.

S Name
Escreve a imagem em um arquivo de nome Name.

X
Encerra o programa.

Considerações:
Comandos diferentes de I, C, L, V, H, K, F, S e X devem ser ignorados

Testes:

Entrada 01
I 5 6
L 2 3 A
S one.bmp
G 2 3 J
V 2 3 4 W
H 3 4 2 Z
F 3 3 J
S two.bmp
X

Saida 01
one.bmp
OOOOO
OOOOO
OAOOO
OOOOO
OOOOO
OOOOO
two.bmp
JJJJJ
JJZZJ
JWJJJ
JWJJJ
JJJJJ
JJJJJ

Entrada 02
I 10 9
L 5 3 A
G 2 3 J
V 2 3 4 W
H 1 10 5 Z
F 3 3 J
K 2 7 8 8 E
F 9 9 R
S one.bmp
X

Saida 02
one.bmp
JJJJJJJJJJ
JJJJJJJJJJ
JWJJAJJJJJ
JWJJJJJJJJ
ZZZZZZZZZZ
RRRRRRRRRR
REEEEEEERR
REEEEEEERR
RRRRRRRRRR
"""

import os
from matrix import Matrix


class EditorGrafico():

    def __init__(self):
        self.__command = []
        self.__matrix = Matrix()

    def color_pixel(self, row, column, original_value, color):
        self.__matrix.set(row, column, color)
        colored = True
        colored_neighbors = []
        neighbors = self.__matrix.find_neighbors(row, column)

        for neighbor in neighbors:
            (i, j) = neighbor
            if self.__matrix.get(i, j) == original_value:
                self.__matrix.set(i, j, color)
                colored_neighbors.append((i, j))

        if colored_neighbors is not None:
            for neighbor in colored_neighbors:
                (i, j) = neighbor
                self.color_pixel(i, j, original_value, color)

    def execute_command(self, command):
        option = ""

        try:
            if type(command) is not str:
                raise TypeError("O comando enviado não é aceitavél.")

        except TypeError as error:
            print error.args[0]

        else:
            self.__command = command.split()
            option = self.__command[0]

        if option == "I":
            try:
                (rows, columns) = 0, 0
                if len(self.__command) > 3 or len(self.__command) < 3:
                    raise UserWarning("Quantidade de argumentos inválida.\
                        Uso: I L C [L = linhas][C = colunas]")

                columns = int(self.__command[1])
                rows = int(self.__command[2])

            except UserWarning as error:
                print error.args[0]

            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."

            else:
                self.__matrix = Matrix(rows, columns)
                return "Criando a Matriz."

        elif option == "C":
            try:
                if self.__matrix.is_empty():
                    raise UserWarning("Limpando matriz vazia.")

                elif self.__matrix.is_zeros():
                    raise UserWarning("A matriz já está limpa.")

            except UserWarning as error:
                print error.args[0]

            else:
                self.__matrix.zeros()
                return "Limpando a Matriz."

        elif option == "L":
            try:
                if self.__matrix.is_empty():
                    raise UserWarning("A matrix está vazia,\
                     impossível colorir o pixel.")

                if len(self.__command) > 4 or len(self.__command) < 4:
                    raise UserWarning("Quantidade de argumentos inválida.\
                        Uso: L X Y C[X = coluna][Y = linha][C = cor]")

                column = int(self.__command[1])
                row = int(self.__command[2])

            except UserWarning as error:
                print error.args[0]

            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."

            else:
                self.__matrix.set(row, column, self.__command[3])
                return "Colorindo o pixel."

        elif option == "V":
            try:
                if self.__matrix.is_empty():
                    raise UserWarning("A matrix está vazia,\
                     impossível colorir o intervalo.")

                if len(self.__command) > 5 or len(self.__command) < 5:
                    raise UserWarning("Quantidade de argumentos inválida.\
                        Uso: V X Y1 Y2 C[X = coluna][Y1 = intervalo menor]\
                        [Y2 = intervalor maior][C = cor]")

                interval = (int(self.__command[2]), int(self.__command[3]) + 1)
                rows = range(interval[0], interval[1])
                column = int(self.__command[1])

            except UserWarning as error:
                print error.args[0]

            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."

            else:
                for i in rows:
                    self.__matrix.set(i, column, self.__command[4])
                return "Colorindo o segmento vertical."

        elif option == "H":
            try:
                if self.__matrix.is_empty():
                    raise UserWarning("A matrix está vazia,\
                     impossível colorir o intervalo.")

                if len(self.__command) > 5 or len(self.__command) < 5:
                    raise UserWarning("Quantidade de argumentos inválida.\
                        Uso: H X1 X2 Y C[X1 = intervalo menor]\
                        [X2 = intervalo maior][Y = linha][C = cor]")

                interval = (int(self.__command[1]), int(self.__command[2]) + 1)
                columns = range(interval[0], interval[1])
                row = int(self.__command[3])

            except UserWarning as error:
                print error.args[0]

            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."

            else:
                for j in columns:
                    self.__matrix.set(row, j, self.__command[4])
                return "Colorindo o segmento horizontal."

        elif option == "K":
            try:
                if self.__matrix.is_empty():
                    raise UserWarning("A matrix está vazia,\
                     impossível colorir o intervalo.")

                if len(self.__command) > 6 or len(self.__command) < 6:
                    raise UserWarning("""Quantidade de argumentos inválida.
                                      Uso: K X1 X2 Y1 Y2 C
                                      [X1 = intervalo menor colunas]
                                      [X2 = intervalo maior colunas]
                                      [Y1 = intervalo menor linhas]
                                      [Y2 = intervalo maior linhas]
                                      [C = cor]""")

                rows_interval = range(int(self.__command[3]),
                                      int(self.__command[4]) + 1)
                columns_interval = range(int(self.__command[1]),
                                         int(self.__command[2]) + 1)

            except UserWarning as error:
                print error.args[0]

            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."

            else:
                for i in rows_interval:
                    for j in columns_interval:
                        self.__matrix.set(i, j, self.__command[5])
                print self.__matrix
                return "Colorindo o retângulo."

        elif option == "F":
            try:
                if self.__matrix.is_empty():
                    raise UserWarning("A matrix está vazia,\
                     impossível colorir o pixel.")

                if len(self.__command) > 4 or len(self.__command) < 4:
                    raise UserWarning("Quantidade de argumentos inválida.\
                        Uso: F X Y C[X = coluna][Y = linha][C = cor]")

                column = int(self.__command[1])
                row = int(self.__command[2])
            except UserWarning as error:
                print error.args[0]

            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."

            else:
                value = self.__matrix.get(row, column)
                self.color_pixel(row, column, value, self.__command[3])
                return "Colorindo a região."

        elif option == "S":
            try:
                if len(self.__command) > 2 or len(self.__command) > 2:
                    raise UserWarning("Quantidade de argumentos inválida\
                        Uso: S Name [Name = nome do arquivo]")

            except UserWarning as error:
                print error.args[0]

            else:
                if not os.path.exists("output"):
                    os.makedirs("output")
                file = open("output/" + self.__command[1], "w")
                file.write(self.__matrix.__str__())
                file.close()

                return "Salvo em output/" + self.__command[1]

        else:
            return "Comando inválido."

    def matrix(self):
        return self.__matrix


def main():
    editor = EditorGrafico()
    while True:
        command = raw_input("Digite o comando a ser executado: ")
        if command == "X":
            print "Encerrando a aplicação."
            break
        else:
            answer = editor.execute_command(command)
            if answer is not None:
                print answer

if __name__ == '__main__':
    main()
