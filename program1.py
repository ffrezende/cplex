#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def plot_matrix_inline(matrix):
  result_string = ""
  for i in range(0, matrix.shape[0]):
    result_string += "["
    for j in range(0, matrix.shape[1]):
      result_string += " " + str(matrix[i][j])
    result_string += "]"
  return result_string

# Tamanhos dos Conjuntos
# Contratados
n = 4
# Estagiários
m = 2
# Empregados
empregados = 6
# Resoluções
resolucoes = 8
# Plataformas
plataformas = 3

# Parâmetros

# peso em horas da atividade do tipo  j da plataforma k
Wjk = np.random.randint(1, 10, size=(resolucoes, plataformas))
# quantidade mínima de atividades do tipo j da plataforma k  que devem ser resolvidas por mês
QAjk_min = np.random.randint(1, 25, size=(resolucoes, plataformas))
# quantidade máxima de atividades do tipo j da plataforma k  que podem ser resolvidas por mês
QAjk_max = np.random.randint(26, 50, size=(resolucoes, plataformas))
# Horas disponíveis por dia para contratados
Hc = 8
# Horas disponíveis por dia para estagiários
He = 6
# Dias em um mês
D = 22
# Horas disponíveis em um mês
Hmax = 24*D*(n*Hc + m*He)
# Afinidade dos programadores
Aik = np.random.rand(empregados, plataformas)

# Escrevendo no arquivo
file = open('dados.txt', 'w')
# Parâmetros
file.write(str(empregados) + '\n')
file.write(str(resolucoes) + '\n')
file.write(str(plataformas) + '\n')
file.write(plot_matrix_inline(Wjk) + '\n')
file.write(plot_matrix_inline(QAjk_min) + '\n')
file.write(plot_matrix_inline(QAjk_max) + '\n')
file.write(str(Hmax) + '\n')
file.write(plot_matrix_inline(Aik) + '\n')