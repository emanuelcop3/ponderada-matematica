# -*- coding: utf-8 -*-
"""Ponderada11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iJSninJNfQYmZl6Le1WGmFpOuWPczW4F

Para calcular a entropia do sistema de vendas diárias, podemos usar a fórmula da entropia de Shannon:

\[ H(X) = - \sum_{i=1}^{n} p(x_i) \log_2 p(x_i) \]

onde:
- \( H(X) \) é a entropia do sistema.
- \( p(x_i) \) é a probabilidade de ocorrência do evento \( x_i \).
- \( n \) é o número total de eventos.

Primeiro, precisamos calcular a probabilidade de ocorrência de cada produto com base nas vendas diárias e, em seguida, calcular a entropia.

Vamos fazer isso em Python:
"""

import math

# Dados de vendas diárias
vendas_diarias = [10, 5, 3, 2, 0, 0]

# Calculando o total de vendas
total_vendas = sum(vendas_diarias)

# Calculando a probabilidade de cada produto
probabilidades = [venda / total_vendas for venda in vendas_diarias if venda > 0]

# Calculando a entropia
entropia = -sum(p * math.log2(p) for p in probabilidades)

entropia

"""#### A entropia do sistema de vendas diárias para os produtos é aproximadamente 1,74 bits. Isso indica a incerteza ou aleatoriedade associada à distribuição das vendas diárias dos produtos. Quanto maior a entropia, mais distribuída ou uniforme é a importância relativa dos produtos; neste caso, uma entropia de 1,74 sugere uma distribuição moderada, com alguns produtos sendo mais significativos que outros. ​"""