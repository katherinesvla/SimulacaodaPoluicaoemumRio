class LeitorDados:

    def ler_matriz(self, nome):

        matriz = []

        arquivo = open(nome, "r")

        for linha in arquivo:

            valores = []

            for numero in linha.split():
                valores.append(int(numero))

            if valores:
                matriz.append(valores)

        arquivo.close()

        return matriz

    def ler_vetor(self, nome):

        vetor = []

        arquivo = open(nome, "r")

        for linha in arquivo:

            if linha.strip():
                vetor.append(int(linha.strip()))

        arquivo.close()

        return vetor