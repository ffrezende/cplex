# Como executar?

Passo-a-passo para a execução desse trem:

1. Criar arquivo `.txt` de dados aleatórios
    * `python program1.py`
1. Ler os dados txt e produzir o `.lp`
    * `python program2.py`
1. Abrir o prompt de comando e abrir a shell do CPLEX
    * `cplex`
1. Ler o arquivo de dados do formato `.lp`
    * `read dados.lp lp`
1. Gerar solução
    * `optimize`