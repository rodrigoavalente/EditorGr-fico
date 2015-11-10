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
O pixel (X,Y) pertence à região. Outro pixel pertence à região, se e somente se,
ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um lado em comum com
um pixel pertencente à região.

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
from matrix import Matrix


class EditorGrafico():

    def __init__(self):
        self.__command = []
        self.__matrix = Matrix()

    def set_command(self, command):
        try:
            if type(command) is not str:
                raise TypeError("O comando enviado não é aceitavél.")
                return False
            else:
                self.__command = command.split()
        except TypeError as error:
            print error[0]
        else:
            return True

    def execute_command(self):
        command = None

        try:
            command = self.__command[0]
        except IndexError:
            print "Não foi definido nenhum comando."

        if command == "I":
            try:
                (rows, columns) = 0, 0
                if len(self.__command) > 3 or len(self.__command) < 3:
                    raise UserWarning("Quantidade de argumentos inválido.\
                        Uso: I L C [L = linhas][C = colunas]")
                else:
                    row = int(self.__command[1])
                    column = int(self.__command[2])
            except UserWarning as error:
                print error.args[0]
            except ValueError:
                print "O valor passado para linhas ou colunas não é um número."
            else:
                self.__matrix = Matrix(rows, columns)
                return "Criando a Matriz."
        elif command == "C":
            return "Limpando a Matriz."
        elif command == "L":
            return "Colorindo o pixel."
        elif command == "V":
            return "Colorindo o segmento vertical."
        elif command == "H":
            return "Colorindo o segmento horizontal."
        elif command == "K":
            return "Colorindo o retângulo."
        elif command == "F":
            return "Colorindo a região."
        else:
            return "Comando inválido."

    def matrix(self):
        return self.__matrix


def main():
    pass

if __name__ == '__main__':
    main()
