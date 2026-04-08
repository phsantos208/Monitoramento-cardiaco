Sistema de Monitoramento Cardíaco
Um script simples em Python para coleta e análise de dados de frequência cardíaca durante um período de 60 segundos. O objetivo é fornecer estatísticas básicas sobre os batimentos registrados e identificar possíveis variações fora da faixa de repouso padrão.

 Funcionalidades
O sistema processa as seguintes informações:

Coleta de Dados: Entrada manual de 60 medições (uma por segundo).

Média de BPM: Cálculo da média aritmética do período.

Picos Cardíacos: Identificação automática do maior e menor batimento registrado.

Análise de Faixa Segura: Identifica quantos registros ficaram fora do intervalo de 60 a 100 BPM.

 Tecnologias Utilizadas
Linguagem: Python 3

 Como usar
Certifique-se de ter o Python instalado.
Aviso: Este projeto possui caráter estritamente educativo e não deve ser utilizado como diagnóstico médico real.
Clone este repositório ou baixe o arquivo .py.

Execute o script no terminal:

Bash

python nome_do_arquivo.pyAviso: Este projeto possui caráter estritamente educativo e não deve ser utilizado como diagnóstico médico real.
Digite os valores solicitados conforme cada segundo de monitoramento.

 Exemplo de Saída
Plaintext

=== Resultados ===
Media de batimentos: 72.5
Pico maximo: 105 bpm
Pico minimo: 58 bpm
Valores fora da faixa segura: 4
