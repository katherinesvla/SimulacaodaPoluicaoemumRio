class GaussSeidel:

    def __init__(self, A2, b2, epsilon):

        self.A2 = A2
        self.b2 = b2
        self.epsilon = epsilon

    def resolver(self):

        n2 = len(self.A2)

        print("metodo gauss-seidel")

        print("matriz A2:")
        for linha in self.A2:
            print(linha)

        print("vetor b2:")
        print(self.b2)

        print("precisao:", self.epsilon)

        print("verificacao da convergencia")

        convergencia = True

        for i in range(n2):

            diagonal = abs(self.A2[i][i])

            soma = 0

            for j in range(n2):
                if i != j:
                    soma = soma + abs(self.A2[i][j])

            print("linha", i + 1)
            print("diagonal =", diagonal)
            print("soma =", soma)

            if diagonal > soma:
                print("condicao satisfeita")
            else:
                print("condicao insatisfeita")
                convergencia = False

        if convergencia:
            print("matriz diagonal dominante")
            print("convergencia garantida para gauss-seidel")
        else:
            print("dominancia diagonal estrita nao satisfeita")
            print("convergencia precisa ser analisada")

        print("primeira iteracao de gauss-seidel")

        p = [0.0 for i in range(n2)]

        print("vetor inicial:", p)

        for i in range(n2):

            soma = 0.0

            for j in range(n2):
                if i != j:
                    soma = soma + self.A2[i][j] * p[j]

            p[i] = (self.b2[i] - soma) / self.A2[i][i]

            print("p", i + 1, "=", round(p[i], 6))

        print("vetor apos a primeira iteracao:")
        print([round(valor, 6) for valor in p])

        print("iteracoes de gauss-seidel")

        iteracao = 1
        max_iteracoes = 1000

        while iteracao < max_iteracoes:

            p_anterior = p.copy()

            for i in range(n2):

                soma = 0.0

                for j in range(n2):
                    if i != j:
                        soma = soma + self.A2[i][j] * p[j]

                p[i] = (self.b2[i] - soma) / self.A2[i][i]

            iteracao = iteracao + 1

            erro = 0.0

            for i in range(n2):

                diferenca = abs(p[i] - p_anterior[i])

                if diferenca > erro:
                    erro = diferenca

            print("iteracao", iteracao)
            print("vetor:", [round(valor, 6) for valor in p])
            print("erro:", round(erro, 8))

            if erro < self.epsilon:
                print("precisao atingida")
                break

        else:
            print("limite de iteracoes atingido")

        print("solucao aproximada:")
        print([round(valor, 6) for valor in p])

        print("verificacao do sistema A2 * p = b2")

        resultado = []

        for i in range(n2):

            soma = 0.0

            for j in range(n2):
                soma = soma + self.A2[i][j] * p[j]

            resultado.append(soma)

            print("Linha", i + 1, "=", round(soma, 6))

        print("resultado calculado:")
        print([round(valor, 6) for valor in resultado])

        print("vetor original b2:")
        print(self.b2)

        erro_residual = 0.0

        for i in range(n2):

            diferenca = abs(resultado[i] - self.b2[i])

            if diferenca > erro_residual:
                erro_residual = diferenca

        print("maior erro residual:")
        print(round(erro_residual, 8))

        return p, iteracao