from fractions import Fraction

class FatoracaoLU:

    def __init__(self, A1, b1):

        self.A1 = A1
        self.b1 = b1

    def resolver(self):

        n = len(self.A1)

        U = [[Fraction(valor) for valor in linha] for linha in self.A1]

        L = [[Fraction(0) for j in range(n)]
             for i in range(n)]

        for i in range(n):
            L[i][i] = Fraction(1)

        print("matriz L:")

        for linha in L:
            print([str(valor) for valor in linha])

        pivo = U[0][0]

        print("primeiro pivo:", pivo)

        if pivo == 0:
            raise ValueError("Pivo zero.")

        for i in range(1, n):

            multiplicador = U[i][0] / pivo

            L[i][0] = multiplicador

            print("multiplicador m:", i + 1, "1=", multiplicador)

            for j in range(n):
                U[i][j] = U[i][j] - multiplicador * U[0][j]

            print("Linha", i + 1, "atualizada:")
            print([str(valor) for valor in U[i]])

        print("matriz U primeiro pivo:")

        for linha in U:
            print([str(valor) for valor in linha])

        print("matriz L primeiro pivo:")

        for linha in L:
            print([str(valor) for valor in linha])

        print("segundo pivo")

        pivo = U[1][1]

        print("segundo pivo:", pivo)

        if pivo == 0:
            raise ValueError("Pivo zero.")

        for i in range(2, n):

            multiplicador = U[i][1] / pivo

            L[i][1] = multiplicador

            print("multiplicador:", i + 1, "2=", multiplicador)

            for j in range(1, n):
                U[i][j] = U[i][j] - multiplicador * U[1][j]

            print("Linha", i + 1, "atualizada:")
            print([str(valor) for valor in U[i]])

        print("matriz U segundo pivo:")

        for linha in U:
            print([str(valor) for valor in linha])

        print("matriz L segundo pivo:")

        for linha in L:
            print([str(valor) for valor in linha])

        print("terceiro pivo")

        pivo = U[2][2]

        print("Terceiro pivo:", pivo)

        if pivo == 0:
            raise ValueError("Pivo zero.")

        for i in range(3, n):

            multiplicador = U[i][2] / pivo

            L[i][2] = multiplicador

            print("Multiplicador:", i + 1, "3=", multiplicador)

            for j in range(2, n):
                U[i][j] = U[i][j] - multiplicador * U[2][j]

            print("Linha", i + 1, "atualizada:")
            print([str(valor) for valor in U[i]])

        print("matriz U terceiro pivo:")

        for linha in U:
            print([str(valor) for valor in linha])

        print("matriz L terceiro pivo:")

        for linha in L:
            print([str(valor) for valor in linha])

        print("quarto pivo")

        pivo = U[3][3]

        print("Quarto pivo:", pivo)

        if pivo == 0:
            raise ValueError("Pivo zero.")

        for i in range(4, n):

            multiplicador = U[i][3] / pivo

            L[i][3] = multiplicador

            print("Multiplicador m", i + 1, "4 =", multiplicador)

            for j in range(3, n):
                U[i][j] = U[i][j] - multiplicador * U[3][j]

            print("Linha", i + 1, "atualizada:")
            print([str(valor) for valor in U[i]])

        print("\nMATRIZ U FINAL:")

        for linha in U:
            print([str(valor) for valor in linha])

        print("\nMATRIZ L FINAL:")

        for linha in L:
            print([str(valor) for valor in linha])

        print("substituicao progressiva")

        y = [Fraction(0) for i in range(n)]

        for i in range(n):

            soma = Fraction(0)

            for j in range(i):
                soma = soma + L[i][j] * y[j]

            y[i] = (Fraction(self.b1[i]) - soma) / L[i][i]

            print("y", i + 1, "=", y[i])

        print("vetor y:")

        print([str(valor) for valor in y])

        print("substituicao regressiva")

        x = [Fraction(0) for i in range(n)]

        for i in range(n - 1, -1, -1):

            soma = Fraction(0)

            for j in range(i + 1, n):
                soma = soma + U[i][j] * x[j]

            if U[i][i] == 0:
                raise ValueError("zero na diagonal de U")

            x[i] = (y[i] - soma) / U[i][i]

            print("x", i + 1, "=", x[i])

        print("vetor solucao:")
        print([str(valor) for valor in x])

        return x