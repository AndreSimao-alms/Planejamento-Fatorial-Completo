# Planejamento-Fatorial-Completo
Objetivo geral: Automatizar tratamento de dados para planejamento fatorial completo para experimentos de 2^4.

## O que é Planejamento fatorial completo?
O planejamento fatorial completo é a etapa inicial que é realizada pelo experimentador que procura identificar efeitos e maiores importâncias dentre um grupo de variáveis para um determinado estudo.

## Qual o contexto do projeto? 
Atualmente, estou realizando o curso de Introdução à Quimiometria no curso de Química UFSCar, o objetivo é aplicar os conceitos oferecidos pelo curso e atingir maior proficiência nas ferramentas para data science até o final do processo. 

## O que a rotina gera como resultado?
A rotina gera de maneir, quase instatânea um grupo de resultados oferecida pela tabela de resultados obtidos para 16 experimentos, por exemplo, efeitos das interações das variáveis, porcentagem dos quadrados e distribuição acumulatica de probabilidade inversa (PPF) também é gerados dois gráficos, o primeiro tipo Scatter, Efeitos x gaussiana (PPF) e o segundo tipo bar, Porcentagemn x Efeitos.

## Que tipo de dados é fornecido à rotina?
Os dados serão colados no arquivo excel 'efeitos.xlsx' na planilha 'Dados' e em seguida o usuário clicará no botão ao lado, assim, através do Macro 'efeitos' o excel irá calcular as interações das variáveis. Após isso, o arquivo já estará salvo, basta somente realizar upload no diretório da rotina e acionar a opção 'run all' para obter os resultados.

## Instruções de uso:
- Baixe o arquivo "aghata_efeito.py" e "efeitos.xlsm".
- Abra o arquivo "efeitos.xlsm", ative os macros, cole os resultados na planilha "Dados" e depois clique para no botão ao lado.
- Feche o "efeitos.xlsm"
- Abra um notebook no Colaboratory Google e faça upload dos dois arquivos e depois escreva o seguinte código na célula
'''
import aghata_efeito as agt
aghata_efeito()
'''
- Siga as instruções orientadas
- Pronto! Basta baixar os seus resultados. 
