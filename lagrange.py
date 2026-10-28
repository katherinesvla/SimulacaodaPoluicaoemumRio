class Lagrange:

    def __init__(self, x, p):

        self.x = x
        self.p = p

    def resolver(self):

        print("posicoes e poluicao")

        pontos = []

        for i in range(len(self.x)):

            posicao = float(self.x[i])
            poluicao = self.p[i]

            pontos.append((posicao, poluicao))

            print(
                "Ponto", i + 1,
                "Posicao:", posicao,
                "Poluicao:", round(poluicao, 6)
            )

        print("ordenacao dos pontos")

        pontos.sort()

        for i in range(len(pontos)):

            posicao = pontos[i][0]
            poluicao = pontos[i][1]

            print(
                "Ponto", i + 1,
                "Posicao:", posicao,
                "Poluicao:", round(poluicao, 6)
            )

        print("posicao central do rio")

        menor_posicao = pontos[0][0]
        maior_posicao = pontos[-1][0]

        centro = (menor_posicao + maior_posicao) / 2

        print("Menor posicao:", menor_posicao)
        print("Maior posicao:", maior_posicao)
        print("Posicao central:", centro)

        print("pontos para interpolacao")

        for i in range(len(pontos) - 1):

            if pontos[i][0] <= centro <= pontos[i + 1][0]:

                ponto1 = pontos[i]
                ponto2 = pontos[i + 1]

                break

        print("Ponto anterior:", ponto1)
        print("Ponto posterior:", ponto2)

        print("interpolacao de lagrange")

        x0 = ponto1[0]
        y0 = ponto1[1]

        x1 = ponto2[0]
        y1 = ponto2[1]

        print("x0 =", x0)
        print("y0 =", round(y0, 6))
        print("x1 =", x1)
        print("y1 =", round(y1, 6))

        termo1 = y0 * (centro - x1) / (x0 - x1)
        termo2 = y1 * (centro - x0) / (x1 - x0)

        poluicao_centro = termo1 + termo2

        print("Primeiro termo:", round(termo1, 6))
        print("Segundo termo:", round(termo2, 6))

        print("Posicao da cidade:", centro)
        print("Poluicao estimada:", round(poluicao_centro, 4))

        return centro, poluicao_centro