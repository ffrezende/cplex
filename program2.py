import re

def from_inline_matrix_to_matrix(inline_matrix):
  result_matrix = []
  regex_results = re.finditer('\[(.*?)\]', inline_matrix)
  for result in regex_results:
    row = result.group(1).split(' ')[1:]
    int_row = [float(x) for x in row]
    result_matrix.append(int_row) 
    
  return result_matrix

# PEGANDO DADOS DO TXT
file = open('dados.txt', 'r')

empregados = range(0, int(file.readline()))
resolucoes = range(0, int(file.readline()))
plataformas = range(0, int(file.readline()))
Wjk = from_inline_matrix_to_matrix(file.readline())
QAjk_min = from_inline_matrix_to_matrix(file.readline())
QAjk_max = from_inline_matrix_to_matrix(file.readline())
Hmax = int(file.readline())
Aik = from_inline_matrix_to_matrix(file.readline())


# ESCREVENDO DADOS NO FORMATO .lp
lp_file = open('dados.lp', 'w')

# Função Objetivo
lp_file.write('Maximize\n')
lp_file.write('  obj:')
aux_string = ''
for j in resolucoes:
  for k in plataformas:
    aux_string += ''
    for i in empregados:
      # precisa colocar o 1/parâmetro multiplicando porque o lp não aceita divisão
      multiplier = (1/Wjk[j][k]) * Aik[i][k]
      aux_string += ' {0} X{1}{2}{3} +'.format(multiplier, i, j, k) 
    aux_string = aux_string[:-1] # removendo ultimo + 
    aux_string += '\n  +'
lp_file.write(aux_string[:-1] + '\n') # removendo ultimo + e escrevendo no arquivo


# Restrições
lp_file.write('Subject to\n')

# Mínimo de resoluções a serem completas
counter = 0
for j in resolucoes:
    for k in plataformas:
        counter += 1
        lp_file.write('  a{0}: '.format(counter))
        aux_string = ''
        for i in empregados:
          aux_string += ' X{0}{1}{2} +'.format(i, j, k) 
        aux_string = aux_string[:-1] # removendo ultimo + 
        lp_file.write('{0} >= {1}\n'.format(aux_string, QAjk_min[j][k]*Wjk[j][k]))

# Máximo de resoluções a serem completas
counter = 0
for j in resolucoes:
    for k in plataformas:
        counter += 1
        lp_file.write('  b{0}: '.format(counter))
        aux_string = ''
        for i in empregados:
          aux_string += ' X{0}{1}{2} +'.format(i, j, k) 
        aux_string = aux_string[:-1] # removendo ultimo + 
        lp_file.write('{0} <= {1}\n'.format(aux_string, QAjk_max[j][k] * Wjk[j][k]))

# Máximo de horas disponíveis
aux_string = ''
for j in resolucoes:
    for k in plataformas:
        for i in empregados:
          aux_string += ' X{0}{1}{2} +'.format(i, j, k) 
aux_string = aux_string[:-1] # removendo ultimo + 
lp_file.write('  c1: {0} <= {1}\n'.format(aux_string, Hmax))

# Fim
lp_file.write('End\n')

