# Trabalho 02 - Cálculo Numérico

## Tema 2 - Simulação da Poluição em um Rio

**Professora:** Suzana Matos França de Oliveira

**Alunas::**
- Katherine Maria Carvalho da Silva
- Geovanna Duarte Nascimento da Silva

**Linguagem utilizada:** Python

## Objetivo do Trabalho

O objetivo deste trabalho é desenvolver um programa em Python para simular os níveis de poluição em um rio, utilizando métodos de Cálculo Numérico.

O programa utiliza três métodos matemáticos:

1. Fatoração LU para determinar as posições dos pontos de coleta.
2. Método de Gauss-Seidel para calcular os níveis de poluição, verificando a convergência.
3. Interpolação linear de Lagrange para estimar o nível de poluição na posição central do rio.

Os dados das matrizes e dos vetores são lidos de arquivos TXT.

A precisão utilizada nos cálculos iterativos é de 0.0001.

## Organização dos Arquivos

O projeto foi desenvolvido em Python, utilizando programação orientada a objetos e separando os métodos matemáticos em arquivos diferentes.

### principal.py
Arquivo principal do programa. Realiza a leitura dos dados, executa os métodos e apresenta os resultados da simulação.

### leitordedados.py
Contém a classe LeitorDados, responsável pela leitura das matrizes e dos vetores armazenados nos arquivos TXT.

### fatoracaolu.py
Contém a classe FatoracaoLU, responsável pela resolução do primeiro sistema linear por meio da fatoração LU, utilizando substituição progressiva e regressiva.

### gaussseidel.py
Contém a classe GaussSeidel, responsável pela resolução aproximada do segundo sistema linear e pela verificação da convergência.

### lagrange.py
Contém a classe Lagrange, responsável pela ordenação dos pontos e pela estimativa da poluição na posição central do rio.

### Arquivos de entrada
- A1.txt: matriz do primeiro sistema linear.
- b1.txt: vetor do primeiro sistema linear.
- A2.txt: matriz do segundo sistema linear.
- b2.txt: vetor do segundo sistema linear.

## Como Executar o Programa

Para executar o trabalho, é necessário ter o Python instalado no computador.

1. Abra a pasta Trabalho2 no Visual Studio Code (VS Code).

2. Confira se os seguintes arquivos estão na mesma pasta:
   - principal.py
   - leitordedados.py
   - fatoracaolu.py
   - gaussseidel.py
   - lagrange.py
   - A1.txt
   - b1.txt
   - A2.txt
   - b2.txt

3. Abra o terminal do VS Code.

4. No terminal, estando na pasta Trabalho2, digite:

   python principal.py

5. Pressione Enter.

O programa apresentará as matrizes, os cálculos da fatoração LU, as iterações do método de Gauss-Seidel, a interpolação de Lagrange e o resultado final da simulação.

A precisão utilizada é de 0.0001.

## Resultados Obtidos

### Fatoração LU

O primeiro sistema linear foi resolvido pelo método da Fatoração LU, utilizando substituição progressiva e regressiva.

O vetor solução encontrado foi:

x = [23, 7, 30, -50, -12]

A verificação do sistema A1 * x = b1 confirmou que a solução está correta.

### Método de Gauss-Seidel

O segundo sistema linear foi resolvido pelo método iterativo de Gauss-Seidel.

O vetor solução aproximado encontrado foi:

p = [1.999996, 24.000001, 72.000002, 8.999999, 57.0]

Número de iterações: 9

Precisão exigida: 0.0001

A matriz A2 apresentou dominância diagonal estrita, garantindo a convergência do método.

### Interpolação de Lagrange

Os pontos de coleta foram organizados em ordem crescente de posição:

(-50, 9)
(-12, 57)
(7, 24)
(23, 2)
(30, 72)

A posição central foi considerada como o ponto médio entre a menor e a maior posição de coleta.

Posição central = (-50 + 30) / 2 = -10

Para estimar a poluição nessa posição, foi utilizada a interpolação linear de Lagrange entre os pontos (-12, 57) e (7, 24).

Poluição estimada na posição central: 53.5263

Os resultados demonstram a aplicação dos três métodos numéricos na simulação da poluição do rio.
