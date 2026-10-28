from fractions import Fraction
from leitordedados import LeitorDados
from fatoracaolu import FatoracaoLU
from gaussseidel import GaussSeidel
from lagrange import Lagrange

leitor = LeitorDados()

A1 = leitor.ler_matriz("A1.txt")
b1 = leitor.ler_vetor("b1.txt")

A2 = leitor.ler_matriz("A2.txt")
b2 = leitor.ler_vetor("b2.txt")

epsilon = 0.0001

print("matriz A1:")

for linha in A1:
    print(linha)

print("vetor b1:")
print(b1)

n = len(A1)

lu = FatoracaoLU(A1, b1)

x = lu.resolver()

print("\nVETOR SOLUCAO S1:")
print([str(valor) for valor in x])


print("verificacao do sistema A1*x = b1")

resultado = [Fraction(0) for i in range (n)]

for i in range(n):
    soma = Fraction(0)

    for j in range(n):
        soma = soma + A1[i][j]*x[j]
    resultado[i]= soma

    print("Linha", i + 1, "=", resultado[i])

print("resultado calculado:")
print([str(valor) for valor in resultado])

print("vetor original b1:")
print(b1)

if resultado == b1:
    print("solucao correta")
else:
    print("solucao incorreta")

n2 = len(A2)

gs = GaussSeidel(A2, b2, epsilon)

p, iteracao = gs.resolver()

lagrange = Lagrange(x, p)

centro, poluicao_centro = lagrange.resolver()

print("resultado da simulacao:")

print("fatoracao LU")
print("Posicoes dos pontos de coleta:")

for i in range(n):
    print("x", i + 1, "=", x[i])

print("metodo de gauss-seidel")
print("Niveis de poluicao:")

for i in range(n2):
    print("p", i + 1, "=", round(p[i], 6))

print("Iteracoes:", iteracao)
print("Precisao exigida:", epsilon)

print("interpolacao de lagrange")

print("Posicao central:", centro)

print(
    "Poluicao estimada na cidade:",
    round(poluicao_centro, 4)
)

print("simulacao concluida")
