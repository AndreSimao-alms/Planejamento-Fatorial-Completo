{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "aghata_efeito",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPf2cVucYOX/Fxca8gyZQrh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AndreSimao-alms/Planejamento-Fatorial-Completo/blob/main/aghata_efeito.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "637778be"
      },
      "source": [
        "# Planejamento Fatorial em Química\n",
        "\n",
        "    "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nEPNHUO4WHWF"
      },
      "source": [
        "**Autor:** André Simão, aluno de graduação do curso de bacharelado em química tecnológica pela UFSCar.\\\n",
        "\\\n",
        "**Objetivo geral:** Automatizar tratamento de dados para planejamento fatorial completo para experimentos de 2^4. Dessa forma, a aplicabilidade do programa é em foco para facilitar e aumentar a eficiência do trabalho de experimentadores que não possuem proficiência em linguagem de programação.\\\n",
        "\\\n",
        "**Corpo do projeto:** O desenvolvimento das rotinas em plannejamento fatorial será dividida conforme o conteúdo ofericido pelo curso de Introdução a Quimiometria ministrado pelo Prof. Dr. Edenir Rodrigues Pereira Filho. Tendo em vista esta organização, a divisão de funções será constituido em quatro principais tópicos: planejamento fatorial completo, planejamento fatorial fracionário e construção de modelos de regressão.\\\n",
        "\\\n",
        "**Referências bibliográficas:**\\\n",
        "[1]. Pereira Filho, Edenir R. \"Planejamento fatorial em química: maximizando a obtenção de resultados.\" Edufscar: São Carlos (2015).\\\n",
        "\\\n",
        "[2]. Pereira, Fabíola Manhas Verbi, and Edenir Rodrigues Pereira-Filho. \"Aplicação de programa computacional livre em planejamento de experimentos: um tutorial.\" Química Nova 41 (2018): 1061-1071.\\\n",
        "\\\n",
        "[3]. Teófilo, Reinaldo F., and Márcia Ferreira. \"Quimiometria II: planilhas eletrônicas para cálculos de planejamentos experimentais, um tutorial.\" Química nova 29 (2006): 338-350.\\\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "80487a6f"
      },
      "source": [
        "# Bibliotecas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "61656423"
      },
      "source": [
        "import pandas as pd \n",
        "import numpy as np \n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib.pylab as plt\n",
        "import matplotlib.gridspec as gridspec\n",
        "from matplotlib.backends.backend_pdf import PdfPages\n",
        "from scipy.stats import norm\n",
        "import seaborn as sns\n",
        "from scipy import stats"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OBAcwAZywTV0"
      },
      "source": [
        "# Planejamento Fatorial Completo"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KvxSK_kNwoR6"
      },
      "source": [
        "**CAPÍTULO 1: PLANEJAMENTO FATORIAL EM QUÍMICA.**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9d050630"
      },
      "source": [
        "## Leitura e limpeza de dados (Excel)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XyIZgrxAlgeI"
      },
      "source": [
        "O primeiro passo é realizar a leitura de dados, neste rotina de planejamento fatorial completo não será inclusa a etapa de codificação dos resultados experimentais. O programa necessariamente realiza a leitura da tabela com os resultados experimentais dos 16 experimentos, pois trata-se de dois níveis e 4 variaveis, juntamente com a interação das variáveis, indicada pela Figura 1.\\\n",
        "\\\n",
        "Figura 1. Modelo de tabela recebida pelo arquivo 'efeitos.xlsm'.\n",
        " ![Screenshot_74.png](data:image/png;base64,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)\\\n",
        " \\\n",
        "Após a leitura, a tabela sofre uma modificação através do método .iloc da biblioteca Pandas para selecionar somente o efeito das variáveis em seguido é realizado os cálculos de efeitos, quadrado dos efeitos e porcentagem de contribuição dos quadrados de efeitos em relação a soma."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cb6b982c"
      },
      "source": [
        "def leitura():\n",
        "  leitura1 = pd.read_excel('efeitos.xlsm')\n",
        "  dados1 = leitura1.iloc[:,6:21]\n",
        "  return dados1,leitura1"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "362ead3b"
      },
      "source": [
        "## Cálculo de efeitos "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OKia4KBiqQk_"
      },
      "source": [
        "O cáculo de efeitos, neste caso, é dado pela diferença da média das respostas de nível alto e baixo, indicado pela pela equação 1.\\\n",
        "\\\n",
        "Equação 1. Efeito para as variáveis e interações. [3] \\\n",
        "![Screenshot_75.png](data:image/png;base64,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)\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "27b69c2d"
      },
      "source": [
        "def efeitos(dados1):\n",
        "  soma1=[]\n",
        "  for i in range(15):\n",
        "      s = dados1.iloc[:,i]\n",
        "      soma1.append(sum(s))\n",
        "      somas1 = np.array(soma1)\n",
        "  efeitos1 = somas1/8\n",
        "  efeitor1 = []\n",
        "  for i in efeitos1:\n",
        "    efeitor1.append(i)\n",
        "  return efeitor1"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f5435527"
      },
      "source": [
        "def efeitos_sort(efeitor1):\n",
        "  index= [1,2,3,4,12,13,14,23,24,34,123,124,134,234,1234]\n",
        "  efeito1 = pd.Series(efeitor1, index=index, name='Efeitos/Quadrado/Porcentagem')\n",
        "  efeito3 = efeito1.sort_values()\n",
        "  return efeito3"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "df4dc1d9"
      },
      "source": [
        "## Quadrado dos efeitos\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eQyMQaiaIWBt"
      },
      "source": [
        "É dado pelo quadrado dos efeitos de cada variável e interação, indicado pela Equação.\\\n",
        "\\\n",
        "Equação 2: Quadrados dos efeitos.\\\n",
        "\\\n",
        "**quadrado = (efeitos)²**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f86604f7"
      },
      "source": [
        "def quadrado(efeito3):\n",
        "  quadrado1 = efeito3**2\n",
        "  return quadrado1"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f1ab3c1e"
      },
      "source": [
        "## Porcentagem "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "p9L8p62mIrGF"
      },
      "source": [
        "A porcentagem de contribuição de cada efeitos é calculado com a relação do quadrados dos efeitos com o somatório dos quadrados dos efeitos de cada variável e interação, indicado pela Equação 3.\\\n",
        "\\\n",
        "Equação 3. Porcentagem de contribuição de cada efeitos.\\\n",
        "\\\n",
        "![Screenshot_77.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f2a88a89"
      },
      "source": [
        "def porcentagem(quadrado1):\n",
        "  porcentagem1= quadrado1/sum(quadrado1)\n",
        "  return porcentagem1"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6ca8c3ff"
      },
      "source": [
        "## Início, fim, centro e z"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S1ERPutjLqaC"
      },
      "source": [
        "#n_int = int(input('Qual o número de variáveis e interações?: '))\n",
        "n_int = 15\n",
        "fim = []\n",
        "inicio = [0]\n",
        "centro = []\n",
        "gauss = []\n",
        "inc = (1/(n_int))\n",
        "for i in range(n_int):\n",
        "   fim.append(inicio[i] + inc)\n",
        "   inicio.append(fim[i])\n",
        "   centro.append((inicio[i]+fim[i])/2)\n",
        "   gauss.append(norm.ppf(centro))\n",
        "z = []\n",
        "for j in gauss[n_int-1]:\n",
        "  z.append(j)\n",
        "del inicio[n_int]"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WlCUhCiAiNbj"
      },
      "source": [
        "def gaussiana():  \n",
        "  #n_int = int(input('Qual o número de variáveis e interações?: '))\n",
        "  n_int = 15\n",
        "  fim = []\n",
        "  inicio = [0]\n",
        "  centro = []\n",
        "  gauss = []\n",
        "  inc = (1/(n_int))\n",
        "  for i in range(n_int):\n",
        "    fim.append(inicio[i] + inc)\n",
        "    inicio.append(fim[i])\n",
        "    centro.append((inicio[i]+fim[i])/2)\n",
        "    gauss.append(norm.ppf(centro))\n",
        "  z = []\n",
        "  for j in gauss[n_int-1]:\n",
        "    z.append(j)\n",
        "  del inicio[n_int]\n",
        "  return n_int,fim,inicio,centro,z"
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C-t6m4TLiYKX",
        "outputId": "a52fe68c-8109-49f4-8b3f-1c74ff1efe98"
      },
      "source": [
        "z"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[-1.8339146358159146,\n",
              " -1.2815515655446004,\n",
              " -0.967421566101701,\n",
              " -0.7279132908816442,\n",
              " -0.5244005127080409,\n",
              " -0.3406948270877956,\n",
              " -0.1678940047881056,\n",
              " 0.0,\n",
              " 0.16789400478810546,\n",
              " 0.3406948270877954,\n",
              " 0.5244005127080407,\n",
              " 0.7279132908816441,\n",
              " 0.9674215661017008,\n",
              " 1.2815515655446,\n",
              " 1.8339146358159129]"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cd03c3cc"
      },
      "source": [
        "## Construção do dataframe com os resultados\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "c10cd3ff"
      },
      "source": [
        "def dados_g1(efeito3, quadrado1,porcentagem1,inicio,fim,centro,z):\n",
        "  index1 = efeito3.index\n",
        "  colunas1 = {'Efeitos R1' :efeito3 ,'Quadrado':quadrado1,'Porcentagem':porcentagem1,\"Início\":inicio,'Fim':fim,'Centro':centro,'Gaussiana':z}\n",
        "  gauss1 = pd.DataFrame(colunas1, index=index1)\n",
        "  gauss1 = gauss1.rename_axis('N°')\n",
        "  return gauss1"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f049a0a0"
      },
      "source": [
        "## Gráficos "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "003d2f2c"
      },
      "source": [
        "### Gráfico 1: Probabilidade (Efeito x z)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ac212851"
      },
      "source": [
        "### Plot do gráfico 1 "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AMbbpH3xGHZb"
      },
      "source": [
        "#markers=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P']\n",
        "#len(markers)"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3043d68a"
      },
      "source": [
        "sns.set_theme(style=\"darkgrid\")"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pf3CdBjnHWcl"
      },
      "source": [
        "def etiqueta(annotations,gauss1): \n",
        "  for i,label in enumerate(annotations):\n",
        "    plt.annotate(label, (list(gauss1.iloc[:,0])[i],list(gauss1.iloc[:,6])[i]))"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5e90ebe9"
      },
      "source": [
        "def grafico1(gauss1):\n",
        "    annotations = list(gauss1.index)\n",
        "    plt.figure(figsize=(8,9))\n",
        "    fig1 = plt.scatter(list(gauss1.iloc[:,0]),list(gauss1.iloc[:,6]),s=40, color='darkred')\n",
        "    plt.title('Efeito x Gaussiana (z)', fontsize=18, fontweight='black', loc='left')\n",
        "    plt.ylabel('Gaussiana (z)')\n",
        "    plt.xlabel('Efeitos')\n",
        "    etiqueta(annotations,gauss1)\n",
        "    return fig1"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ebc0a173"
      },
      "source": [
        "### Gráfico 2: Porcentagem de efeito x Interações"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dfc7b24e"
      },
      "source": [
        "### Selecionando dados do dataframe"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f65e4fe9"
      },
      "source": [
        "def dados_g2(porcentagem1):\n",
        "  x2= np.array(porcentagem1.index)\n",
        "  y2= porcentagem1.values\n",
        "  data2= pd.DataFrame({'Efeitos R1': x2, 'Porcentagem (%)': y2})\n",
        "  return data2"
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d50c50a9"
      },
      "source": [
        ""
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b76ba56f"
      },
      "source": [
        "### Plot do gráfico 2"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a13239eb"
      },
      "source": [
        "def grafico2(data2):\n",
        "    plt.figure(figsize=(8,9))\n",
        "    tips = sns.load_dataset(\"tips\")\n",
        "    fig2 = sns.barplot(x='Efeitos R1', y='Porcentagem (%)', data=data2)\n",
        "    fig2.set_title('Porcentagem x Efeitos', fontsize=16, fontweight='black')\n",
        "    return fig2"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nnQ-dodRlI3J"
      },
      "source": [
        "# Reorganização do Planejamento "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ab4fQ_tugiQa"
      },
      "source": [
        "## Variância e Erro de um Efeito"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SB2H3WKUaWA9"
      },
      "source": [
        "### Variância e Erro Experimental"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EzOjvTHOp1K2"
      },
      "source": [
        "#### Excluindo variáveis insignificantes   "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7XYyruJXKJRf"
      },
      "source": [
        "def df_erro1(leitura1):  \n",
        "  V1 = leitura1['V1'][:16].values\n",
        "  V2 = leitura1['V2'][:16].values\n",
        "  V3 = leitura1['V3'][:16].values\n",
        "  V4 = leitura1['V4'][:16].values\n",
        "  R = leitura1['R'][:16].values\n",
        "  col = {'V1': V1, 'V2':V2, 'V3':V3, 'V4':V4, 'R': R}\n",
        "  exp = pd.Series(list(range(1,17)))\n",
        "  dados2 = pd.DataFrame(col, index=exp)\n",
        "  return dados2"
      ],
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sLiZdr8jY19H"
      },
      "source": [
        "def coleta():\n",
        "  x=0\n",
        "  var_exp = []\n",
        "  N=''\n",
        "  while True:\n",
        "    x+=1\n",
        "    if x <= 4:\n",
        "      var_insg = input(f'Digite a variável {x} insignificante?(V1, V2, V3 ou V4): ')\n",
        "      N = str(input('Pressione qualquer tecla para continuar para inserir mais uma variável, caso contrário digite \"N\" para sair. ')).strip().upper()[0]\n",
        "      var_exp.append(var_insg.upper())\n",
        "    if N == \"N\":\n",
        "      break\n",
        "      exit()\n",
        "    if x == 4:\n",
        "      print('Todas variáveis são insignificantes.')\n",
        "      break\n",
        "      exit()\n",
        "  return var_exp"
      ],
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SsiuIfPk8s-H"
      },
      "source": [
        "def tabela_nova1(dados2,cond):\n",
        "  dados2 = dados2.drop(cond[0], axis='columns')\n",
        "  a1 = dados2[dados2.T.index[0]].values\n",
        "  a2 = dados2[dados2.T.index[1]].values\n",
        "  a3 = dados2[dados2.T.index[2]].values\n",
        "  a1a2 = a1*a2\n",
        "  a1a3 = a1*a3\n",
        "  a2a3 = a2*a3\n",
        "  dados2.insert(3, f\"{dados2.T.index[0]}{dados2.T.index[1]}\", a1a2, allow_duplicates=False)\n",
        "  dados2.insert(4, f\"{dados2.T.index[0]}{dados2.T.index[2]}\", a1a3, allow_duplicates=False)\n",
        "  dados2.insert(5, f\"{dados2.T.index[1]}{dados2.T.index[2]}\", a2a3, allow_duplicates=False)\n",
        "  dados3 = dados2.sort_values([f'{dados2.T.index[0]}', f'{dados2.T.index[1]}', f'{dados2.T.index[2]}'], ascending=True)\n",
        "  return dados3\n",
        "def tabela_nova2(dados2,cond):\n",
        "  dados2 = dados2.drop(cond[0], axis='columns')\n",
        "  dados2 = dados2.drop(cond[1], axis='columns')\n",
        "  a1 = dados2[dados2.T.index[0]].values\n",
        "  a2 = dados2[dados2.T.index[1]].values\n",
        "  a1a2 = a1*a2\n",
        "  dados3 = dados2.insert(2, f\"{dados2.T.index[0]}{dados2.T.index[1]}\", a1a2, allow_duplicates=False)\n",
        "  dados3 = dados2.sort_values([f'{dados2.T.index[0]}',f'{dados2.T.index[1]}'], ascending=True)\n",
        "  return dados3\n",
        "def tabela_nova3(dados2,cond):\n",
        "  dados2 = dados2.drop(cond[0], axis='columns')\n",
        "  dados2 = dados2.drop(cond[1], axis='columns')\n",
        "  dados2 = dados2.drop(cond[2], axis='columns')\n",
        "  a1 = dados2[dados2.T.index[0]].values\n",
        "  dados3 = dados2.sort_values([f'{dados2.T.index[0]}'], ascending=True)\n",
        "  return dados3"
      ],
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YRa2dKyhhurD"
      },
      "source": [
        "#cond = coleta()\n",
        "def replicas_inc(cond,dados3):\n",
        "  if len(cond) == 1:\n",
        "    #dados3 = tabela_nova1(dados2)\n",
        "    R2 = []\n",
        "    for i in range(1,17,2):\n",
        "      R2.append(dados3['R'].iloc[i])\n",
        "    replicas = dados3.iloc[:,0:-1]\n",
        "    replicas = replicas.drop_duplicates()\n",
        "    replicas['R1'] = dados3['R']\n",
        "    replicas['R2'] = R2\n",
        "  if len(cond) == 2:\n",
        "    #dados3 = tabela_nova2(dados2)\n",
        "    R=[]\n",
        "    R2=[]\n",
        "    R3=[]\n",
        "    R4=[]\n",
        "    for i in range(0,16,4):\n",
        "      R.append(dados3.iloc[i,-1])\n",
        "    for i in range(1,16,4):\n",
        "      R2.append(dados3.iloc[i,-1])\n",
        "    for i in range(2,16,4):\n",
        "      R3.append(dados3.iloc[i,-1])\n",
        "    for i in range(3,16,4):\n",
        "      R4.append(dados3.iloc[i,-1])\n",
        "    replicas = dados3.iloc[:,0:-1]\n",
        "    replicas = replicas.drop_duplicates()\n",
        "    replicas['R1'] = R\n",
        "    replicas['R2'] = R2\n",
        "    replicas['R3'] = R3\n",
        "    replicas['R4'] = R4\n",
        "  if len(cond) == 3:\n",
        "    #dados3 = tabela_nova3(dados2)\n",
        "    R=[]\n",
        "    R2=[]\n",
        "    R3=[]\n",
        "    R4=[]\n",
        "    R5=[]\n",
        "    R6=[]\n",
        "    R7=[]\n",
        "    R8=[]\n",
        "    for i in range(0,16,8):\n",
        "      R.append(dados3.iloc[i,-1])\n",
        "    for i in range(1,16,8):\n",
        "      R2.append(dados3.iloc[i,-1])\n",
        "    for i in range(2,16,8):\n",
        "      R3.append(dados3.iloc[i,-1])\n",
        "    for i in range(3,16,8):\n",
        "      R4.append(dados3.iloc[i,-1])\n",
        "    for i in range(4,16,8):\n",
        "      R5.append(dados3.iloc[i,-1])\n",
        "    for i in range(5,16,8):\n",
        "      R6.append(dados3.iloc[i,-1])\n",
        "    for i in range(6,16,8):\n",
        "      R7.append(dados3.iloc[i,-1])\n",
        "    for i in range(7,16,8):\n",
        "      R8.append(dados3.iloc[i,-1])\n",
        "    replicas = dados3.iloc[:,0:-1]\n",
        "    replicas = replicas.drop_duplicates()\n",
        "    replicas['R1'] = R\n",
        "    replicas['R2'] = R2\n",
        "    replicas['R3'] = R3\n",
        "    replicas['R4'] = R4\n",
        "    replicas['R5'] = R5\n",
        "    replicas['R6'] = R6\n",
        "    replicas['R7'] = R7\n",
        "    replicas['R8'] = R8\n",
        "  if len(cond) == 4:\n",
        "    print('Todas variáveis são insignificantes.')\n",
        "  return replicas"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Zt2s6fA0kKfP"
      },
      "source": [
        "#### Selecionando replicatas "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cSrraHNFAzmz"
      },
      "source": [
        "#### Construindo tabela de réplicas"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b3mG325gGzGa"
      },
      "source": [
        "### Adicione Tabela de Réplicas Combinada Aqui\n",
        "Caso contenha mais de uma replicata realize as seguintes instruções:\n",
        "- Rode o programa o para cada réplica, utilzando os macros do excel para cada réplica. \n",
        "- Retire o comentário da célula abaixo \"#\"\n",
        "- Depois, pelo Excel, calcule a média das réplicas e monte uma tabela no formato exatamente igual ao apresentado pelo DataFrame aqui acima com o nome *'replicas'*."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VYtAsj6nGx76"
      },
      "source": [
        "#replicas = pd.read_excel('replicas.xlsx')\n",
        "#cond=4"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mRMG5bESqIer"
      },
      "source": [
        "#### Média das Réplicas \n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bakSrCB6qgzb"
      },
      "source": [
        "def media_replicas(cond,replicas):\n",
        "  if len(cond) == 1:\n",
        "    dados_media = replicas.iloc[:,6:8].T.mean()\n",
        "    replicas['Média'] = dados_media \n",
        "  if len(cond) == 2:\n",
        "    mr1 = list(replicas.iloc[:1,3:].T.mean().values)\n",
        "    mr2 = replicas.iloc[1:2,3:].T.mean().values\n",
        "    mr3 = replicas.iloc[2:3,3:].T.mean().values\n",
        "    mr4 = replicas.iloc[3:4,3:].T.mean().values\n",
        "    mean = [mr1,mr2,mr3,mr4]\n",
        "    mean_r =[]\n",
        "    for i in mean:\n",
        "      for j in i:\n",
        "        mean_r.append(j)\n",
        "    mean_r\n",
        "    replicas['Média'] = mean_r\n",
        "    replicas\n",
        "  if len(cond) == 3:\n",
        "    dados_media = replicas.iloc[:,1:9].T.mean()\n",
        "    replicas['Média'] = dados_media \n",
        "  return replicas "
      ],
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IxSNFkRh-yAF"
      },
      "source": [
        "#### Variância das réplicas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sM2CClHT-68v"
      },
      "source": [
        "def var_replicas(cond, replicas):\n",
        "  if len(cond) == 1:\n",
        "    for i in range(replicas.shape[0]):\n",
        "      dados_var = replicas.iloc[:,6:8].T.var()\n",
        "    replicas['Variância'] = dados_var\n",
        "  if len(cond) == 2:\n",
        "    var_r = []\n",
        "    for i  in range(1,5):\n",
        "      var = replicas.iloc[i-1:i,3:7]\n",
        "      var = var.T.var(axis=0).values\n",
        "      var_r.append(var[0])\n",
        "    replicas['Variância'] = var_r\n",
        "  if len(cond) == 3:\n",
        "    for i in range(replicas.shape[0]):\n",
        "      dados_var = replicas.iloc[:,1:9].T.var()\n",
        "      replicas['Variância'] = dados_var\n",
        "  return replicas"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jLlM8JSyCh1p"
      },
      "source": [
        "#### Número de experimentos, graus de liberdade, variancia e erro do experimento e de um efeito."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZowbRH_HC1jY"
      },
      "source": [
        "def exp_eft_dados(cond,replicas):\n",
        "  # numero e graus de liberdade\n",
        "  if len(cond) == 1:\n",
        "    n0 = 2\n",
        "    gl0 = n0 - 1\n",
        "    n = []\n",
        "    gl = []\n",
        "    for i in range(replicas.shape[0]):\n",
        "      n.append(n0)\n",
        "      gl.append(gl0)\n",
        "    replicas['Nº exp'] = n\n",
        "    replicas['g.l'] = gl\n",
        "  if len(cond) == 2:\n",
        "    n0 = 4\n",
        "    gl0 = n0 - 1\n",
        "    n = []\n",
        "    gl = []\n",
        "    for i in range(4):\n",
        "      n.append(n0)\n",
        "      gl.append(gl0)\n",
        "    replicas['Nº exp'] = n\n",
        "    replicas['g.l'] = gl\n",
        "  if len(cond) == 3:\n",
        "    n0 = 8\n",
        "    gl0 = n0 - 1\n",
        "    n = []\n",
        "    gl = []\n",
        "    for i in range(replicas.shape[0]):\n",
        "      n.append(n0)\n",
        "      gl.append(gl0)\n",
        "    replicas['Nº exp'] = n\n",
        "    replicas['g.l'] = gl\n",
        " # variancia e erro do experimento \n",
        "  var_exp = replicas['Variância'].mean()\n",
        "  erro_exp = (var_exp)**(0.5)\n",
        "  print(f\"Variância experimental igual a {var_exp} e Erro experimental igual {erro_exp}\")\n",
        "  replicas['Var_exp'] = var_exp\n",
        "  replicas['Erro_exp'] = erro_exp\n",
        "  # erro e variancia de um efeito \n",
        "  k = 4-len(cond)\n",
        "  erro_eft = (2*erro_exp)/((n0*(2**k))**(0.5))\n",
        "  replicas['Erro_eft'] = erro_eft\n",
        "  print(f'Erro de um Efeito: {erro_eft}')\n",
        "  a = replicas[replicas.T.index[2]].values\n",
        "  a2 = a**2\n",
        "  sum_a = np.sum(a2)/replicas.shape[0]\n",
        "  var_eft = sum_a*(var_exp/replicas.shape[0])\n",
        "  replicas['Var_eft'] = var_eft\n",
        "  return gl,n    "
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nUlM9Y9UACEF"
      },
      "source": [
        "### Valor de \"t\n",
        "Em planejamento fatorial é aplicado 95% de confiança geralmente."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-U0P-bSJpjse"
      },
      "source": [
        "# sig = int(input('Digite o nível de significância?(%): '))\n",
        "def t_value(replicas):\n",
        "  sig = 95\n",
        "  valor_t = (stats.t.ppf((1-(sig/100))/2, sum(replicas['g.l'])))*(-1)\n",
        "  #print(f'Valor de \"t\": {valor_t}')\n",
        "  replicas['t-value'] = valor_t\n",
        "  return valor_t"
      ],
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TuR5Us2d1qrx"
      },
      "source": [
        "### Selecionados dados médios\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CoDObyCe1714"
      },
      "source": [
        "def int_eft_replicas(cond,replicas):\n",
        "  if len(cond) == 1:\n",
        "    media =  replicas[f'{replicas.T.index[8]}'].values\n",
        "    col_vmedio = {f'{replicas.T.index[0]}': replicas[f'{replicas.T.index[0]}'],\n",
        "                  f'{replicas.T.index[1]}': replicas[f'{replicas.T.index[1]}'],\n",
        "                  f'{replicas.T.index[2]}': replicas[f'{replicas.T.index[2]}'],\n",
        "                  f'{replicas.T.index[3]}': replicas[f'{replicas.T.index[3]}'],\n",
        "                  f'{replicas.T.index[4]}': replicas[f'{replicas.T.index[4]}'],\n",
        "                  f'{replicas.T.index[5]}': replicas[f'{replicas.T.index[5]}'],}\n",
        "    v_medio = pd.DataFrame(col_vmedio, index = replicas.index)\n",
        "    eft_medios = []\n",
        "    for i in range(v_medio.shape[0]):\n",
        "      efeito = list(v_medio.loc[list(v_medio.index)[i]].values*media[i])\n",
        "      eft_medios.append(efeito)\n",
        "    col_vmedio = {f'{v_medio.index.values[0]}':eft_medios[0],\n",
        "    f'{v_medio.index.values[1]}':eft_medios[1],\n",
        "    f'{v_medio.index.values[2]}':eft_medios[2],\n",
        "    f'{v_medio.index.values[3]}':eft_medios[3],\n",
        "    f'{v_medio.index.values[4]}':eft_medios[4],\n",
        "    f'{v_medio.index.values[5]}':eft_medios[5],\n",
        "    f'{v_medio.index.values[6]}':eft_medios[6],\n",
        "    f'{v_medio.index.values[7]}':eft_medios[7]}\n",
        "    eft_replicas = pd.DataFrame(col_vmedio, index=v_medio.T.index)\n",
        "    eft_replicas = eft_replicas.T\n",
        "  if len(cond) == 2:\n",
        "    #n_replicas = int(input('Qual o número de réplicas na nova tabela? '))\n",
        "    v_medias = replicas.iloc[:,:3] #ALTERAR\n",
        "    v_medias['Médias'] = replicas['Média']\n",
        "    v1 = [] \n",
        "    v2 = []\n",
        "    v1v2 = [] \n",
        "    for i in range(4):\n",
        "      x = v_medias['Médias'].values[i]\n",
        "      v1.append(v_medias[v_medias.T.index[0]].values[i]*(x))\n",
        "      v2.append(v_medias[v_medias.T.index[1]].values[i]*(x))\n",
        "      v1v2.append(v_medias[v_medias.T.index[0]].values[i]*(x))\n",
        "    col_vmedio = {f'{v_medias.T.index[0]}':v1, f'{v_medias.T.index[1]}':v2,f'{v_medias.T.index[0]}{v_medias.T.index[1]}':v1v2}\n",
        "    eft_replicas = pd.DataFrame(col_vmedio, index=v_medias.index)\n",
        "    eft_replicas\n",
        "  if len(cond) == 3:\n",
        "    media =  replicas[f'{replicas.T.index[9]}'].values\n",
        "    col_vmedio = {f'{replicas.T.index[0]}': replicas[f'{replicas.T.index[0]}'],'Média':media}\n",
        "    v_medio = pd.DataFrame(col_vmedio, index = replicas.index)\n",
        "    eft_medios = []\n",
        "    for i in range(v_medio.shape[0]):\n",
        "      efeito = v_medio[v_medio.T.index[0]].values[i]*v_medio[v_medio.T.index[1]].values[i]\n",
        "      eft_medios.append(efeito)\n",
        "    col_vmedio = {f'{v_medio.T.index[0]}': eft_medios}\n",
        "    eft_replicas = pd.DataFrame(col_vmedio, index=v_medio.index)\n",
        "  return eft_replicas"
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uXQ7AzS1kjUx"
      },
      "source": [
        "### Cálculo de efeitos, quadrado, porcentagem e gaussiana médios"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "01hqUTLJneL_"
      },
      "source": [
        "#### Efeitos"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KQXYy0qnmT65"
      },
      "source": [
        "def efeitos_replicas1(cond,eft_replicas):  \n",
        "  if len(cond) == 1:\n",
        "    efeitor2 = eft_replicas.sum().values/8\n",
        "  if len(cond) == 2:\n",
        "    efeitor2=[]\n",
        "    for i in range(3):\n",
        "      efeitor2.append(eft_replicas.T.values[i].sum()/8)\n",
        "  if len(cond) == 3:\n",
        "    efeitor2=[]\n",
        "    for i in range(1):\n",
        "      efeitor2.append(val_medio.T.values[i].sum()/8)\n",
        "  index_eft = eft_replicas.T.index\n",
        "  efeitos_replicas = pd.DataFrame({'Efeitos':efeitor2}, index=index_eft)  # Utilizar esta variável no dataframe de efeitos e gaussiana \n",
        "  efeitos_replicas = efeitos_replicas.sort_values(by=['Efeitos'])\n",
        "  return efeitos_replicas,efeitor2"
      ],
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q_RMm6Lxns2S"
      },
      "source": [
        "#### Quadrado e porcentagem"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qgM1RdKhm57f"
      },
      "source": [
        "def qdr_por_medio(efeitos_replicas):\n",
        "  efeitor4 = np.sort(efeitos_replicas)\n",
        "  qdr_medio = efeitor4**2\n",
        "  por_medio = qdr_medio/np.sum(qdr_medio)\n",
        "  return efeitor4, qdr_medio, por_medio"
      ],
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ChqaRhCDrNCw"
      },
      "source": [
        "#### Início, Fim, Centro e z (tabela de replicatas)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f5HVhs9aokwL"
      },
      "source": [
        "def gaussiana_replicas(cond):\n",
        "  if len(cond) == 1:\n",
        "    n_int1 = 6\n",
        "    inicio1 = [0]\n",
        "    fim1 = []\n",
        "    centro1 = []\n",
        "    z0 = []\n",
        "    inc1 = (1/(n_int1))\n",
        "    for i in range(n_int1):  \n",
        "      fim1.append(inicio1[i] + inc1)\n",
        "      inicio1.append(fim1[i])\n",
        "      centro1.append((inicio1[i]+fim1[i])/2)\n",
        "      z0.append(norm.ppf(centro1))\n",
        "    z0 = z0[n_int1-1] \n",
        "    z1 = []\n",
        "    for j in z0:\n",
        "      z1.append(j)\n",
        "    del inicio1[n_int1]\n",
        "  if len(cond) == 2:  \n",
        "    #n_int1 = int(input('Qual o número de variáveis e interações?: '))\n",
        "    n_int1 = 3\n",
        "    inicio1 = [0]\n",
        "    fim1 = []\n",
        "    centro1 = []\n",
        "    z0 = []\n",
        "    inc1 = (1/(n_int1))\n",
        "    for i in range(n_int1):  \n",
        "      fim1.append(inicio1[i] + inc1)\n",
        "      inicio1.append(fim1[i])\n",
        "      centro1.append((inicio1[i]+fim1[i])/2)\n",
        "      z0.append(norm.ppf(centro1))\n",
        "    z0 = z0[n_int1-1] \n",
        "    z1 = []\n",
        "    for j in z0:\n",
        "      z1.append(j)\n",
        "    del inicio1[n_int1]\n",
        "    if len(cond) == 3:\n",
        "      n_int1 = 1\n",
        "      inicio1 = [0]\n",
        "      fim1 = []\n",
        "      centro1 = []\n",
        "      z0 = []\n",
        "      inc1 = (1/(n_int1))\n",
        "      for i in range(n_int1):  \n",
        "        fim1.append(inicio1[i] + inc1)\n",
        "        inicio1.append(fim1[i])\n",
        "        centro1.append((inicio1[i]+fim1[i])/2)\n",
        "        z0.append(norm.ppf(centro1))\n",
        "      z0 = z0[n_int1-1] \n",
        "      z1 = []\n",
        "    if cond == 4:\n",
        "      n_int1 = int(input('Qual o número de experimentos?(%): '))\n",
        "      inicio1 = [0]\n",
        "      fim1 = []\n",
        "      centro1 = []\n",
        "      z0 = []\n",
        "      inc1 = (1/(n_int1))\n",
        "      for i in range(n_int1):  \n",
        "        fim1.append(inicio1[i] + inc1)\n",
        "        inicio1.append(fim1[i])\n",
        "        centro1.append((inicio1[i]+fim1[i])/2)\n",
        "        z0.append(norm.ppf(centro1))\n",
        "      z0 = z0[n_int1-1] \n",
        "      z1 = []\n",
        "  dados_efeito_r = (n_int1,inicio1,fim1,centro1,z0)\n",
        "  return dados_efeito_r"
      ],
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CGJw066pdkow"
      },
      "source": [
        "def dados_gr(cond, dados_efeito_r,efeitos_replicas,efeitor4,qdr_medio,por_medio,efeitor2):\n",
        "  if len(cond) == 1:\n",
        "    index_r = list(efeitos_replicas.index)\n",
        "    colunas2 = {'Efeitos':efeitor4, 'Quadrado': qdr_medio, 'Porcentagem': por_medio, 'Início': dados_efeito_r[1],'Fim':dados_efeito_r[2], 'Centro':dados_efeito_r[3], 'Gaussiana':dados_efeito_r[4]}\n",
        "    gauss2 = pd.DataFrame(colunas2, index=index_r)\n",
        "  if len(cond) == 2:  \n",
        "    index_r = list(efeitos_replicas.index)\n",
        "    colunas2 = {'Efeitos':efeitor2, 'Quadrado': qdr_medio, 'Porcentagem': por_medio, 'Início': dados_efeito_r[1],'Fim':dados_efeito_r[2], 'Centro':dados_efeito_r[3], 'Gaussiana':dados_efeito_r[4]}\n",
        "    gauss2 = pd.DataFrame(colunas2, index=index_r)\n",
        "  if len(cond) == 3:  \n",
        "    index_r = []\n",
        "    index_r.append(efeitor2.index)\n",
        "    colunas2 = {'Efeitos':efeitor2, 'Quadrado': qdr_medio, 'Porcentagem': por_medio, 'Início': dados_efeito_r[1],'Fim':dados_efeito_r[2], 'Centro':dados_efeito_r[3], 'Gaussiana':dados_efeito_r[4]}\n",
        "    gauss2 = pd.DataFrame(colunas2, index=index_r)\n",
        "  gauss2\n",
        "  if cond == 4:\n",
        "    index_r = []\n",
        "    index_r.append(efeitor2.index)\n",
        "    colunas2 = {'Efeitos':efeitor2, 'Quadrado': qdr_medio, 'Porcentagem': por_medio, 'Início': dados_efeito_r[1],'Fim':dados_efeito_r[2], 'Centro':dados_efeito_r[3], 'Gaussiana':dados_efeito_r[4]}\n",
        "    gauss2 = pd.DataFrame(colunas2, index=index_r)\n",
        "  return gauss2"
      ],
      "execution_count": 73,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iwW7Q-0kSDJN"
      },
      "source": [
        "## Intervalo de Confiança"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9VOLcG8aSTWm"
      },
      "source": [
        "def inter_confianca(valor_t, gauss2, gl):\n",
        "  confianca = (gl[0])**(0.5)*valor_t\n",
        "  inter_c = [-confianca,0,confianca]\n",
        "  gauss2['|Inter Confiança|'] = inter_c[2]\n",
        "  return inter_c"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Rwx_WDfG_TZ2"
      },
      "source": [
        "## Gráficos - Envolvendo intervalo de confiança e contribuição de efeito"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ywg15-4HNqmX"
      },
      "source": [
        "def etiquetar1(annotationsr1,gauss2): \n",
        "  for i,label in enumerate(annotationsr1):\n",
        "    plt.annotate(label, (list(gauss2['Efeitos'])[i],list(gauss2['Gaussiana'])[i]))"
      ],
      "execution_count": 49,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r3_-zJAFX8f1"
      },
      "source": [
        "def dados_inter_c(gauss2, inter_c):\n",
        "  #Eixo X intervalor de confiança \n",
        "  c1 = []\n",
        "  c2 = []\n",
        "  c3 = []\n",
        "  for _ in range(gauss2.shape[0]):\n",
        "    c1.append(inter_c[0])\n",
        "    c2.append(inter_c[1])\n",
        "    c3.append(inter_c[2])\n",
        "  return c1,c2,c3"
      ],
      "execution_count": 50,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DaHZgDMFM4ug"
      },
      "source": [
        "def graficos_replicas(gauss2,inter_c):\n",
        "    annotationsr1 = list(gauss2.index)\n",
        "    plt.figure(figsize=(8,9))\n",
        "    ax3 = plt.scatter(list(gauss2['Efeitos']),list(gauss2['Gaussiana']),s=40, color='darkred')\n",
        "    plt.title('Efeito x Gaussiana (z) - Replicatas', fontsize=18, fontweight='black', loc='left')\n",
        "    plt.ylabel('Gaussiana (z)')\n",
        "    plt.xlabel('Efeitos')\n",
        "    plt.savefig('ProbabilidadeReplicatas.pdf', format='pdf')\n",
        "    c1,c2,c3 = dados_inter_c(gauss2, inter_c)\n",
        "    etiquetar1(annotationsr1, gauss2)\n",
        "    plt.plot(c1,list(gauss2['Gaussiana']))\n",
        "    plt.plot(c2,list(gauss2['Gaussiana']), color='darkred')\n",
        "    plt.plot(c3,list(gauss2['Gaussiana']), color= 'black')\n",
        "    plt.savefig('ProbabilidadeReplicatas.pdf', format='pdf')\n",
        "    eft_replicas = pd.DataFrame({'Efeitos':gauss2.index, 'Porcentagem (%)':gauss2['Porcentagem']}, index=gauss2.index)\n",
        "    plt.figure(figsize=(8,9))\n",
        "    tips = sns.load_dataset(\"tips\")\n",
        "    ax4 = sns.barplot(x='Efeitos', y='Porcentagem (%)', data=eft_replicas)\n",
        "    ax4.set_title('Porcentagem x Efeitos', fontsize=16, fontweight='black')\n",
        "    plt.savefig('EfeitoReplicatas.pdf', format='pdf')\n",
        "    return ax3,ax4"
      ],
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4f559061"
      },
      "source": [
        "# Resultados finais - Planejamento Fatorial Completo"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0UPBfpQi0Kc3"
      },
      "source": [
        "### Gráfico de probabilidade com intervalo de confiança."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cnrY1ti-fI_t"
      },
      "source": [
        "def salvar_planilhas(gauss1,gauss2,replicas):\n",
        "    writer = pd.ExcelWriter('resultadosfinaisreplicas.xlsx')\n",
        "    gauss1.to_excel(writer, 'Efeitos-Porcemtagem-Gauss.xlsx')\n",
        "    gauss2.to_excel(writer, sheet_name='Resultados Replicas')\n",
        "    replicas.to_excel(writer, sheet_name='replicas.xlsx')\n",
        "    return writer.save()"
      ],
      "execution_count": 66,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d-gfOs_Dw0xA"
      },
      "source": [
        "# Definição da rotina aghata_efeito"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cRPL1PTI9YMh"
      },
      "source": [
        "def dados_efeito():\n",
        "  dados1,leitura1 = leitura()\n",
        "  efeito1 = efeitos(dados1)\n",
        "  efeito3 = efeitos_sort(efeito1)\n",
        "  quadrado1 = quadrado(efeito3)\n",
        "  porcentagem1 = porcentagem(quadrado1)\n",
        "  n_int,fim,inicio,centro,z = gaussiana()\n",
        "  gauss1 = dados_g1(efeito3, quadrado1,porcentagem1,inicio,fim,centro,z)\n",
        "  data2 = dados_g2(porcentagem1)\n",
        "  dados_efeito1 = (dados1,leitura1,efeito1,efeito3,quadrado1,porcentagem1,gauss1,data2) \n",
        "  return dados_efeito1"
      ],
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J-4QEEZtkQcn"
      },
      "source": [
        "def graficos(): \n",
        "   dados_efeito1 = dados_efeito()\n",
        "   sns.set_theme(style=\"darkgrid\")\n",
        "   fig1 = grafico1(dados_efeito1[-2])\n",
        "   plt.savefig('Probabilidade.pdf', format='pdf')\n",
        "   fig2 = grafico2(dados_efeito1[-1])\n",
        "   plt.savefig('Efeito.pdf', format='pdf')\n",
        "   return plt.show()\n",
        "   #return fig1,fig2"
      ],
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oZVhVCYe-Iaf"
      },
      "source": [
        "def reorg_pf():\n",
        "  dados_efeito1 = dados_efeito()\n",
        "  gfc = graficos()\n",
        "  dados2 = df_erro1(dados_efeito1[1])\n",
        "  cond = coleta()\n",
        "  if len(cond) == 1:\n",
        "    dados3 = tabela_nova1(dados2,cond)\n",
        "  if len(cond) == 2:\n",
        "    dados3 = tabela_nova2(dados2,cond)\n",
        "  if len(cond) == 3:\n",
        "    dados3 = tabela_nova3(dados2,cond)\n",
        "  replicas = replicas_inc(cond,dados3)\n",
        "  media_replicas(cond,replicas)\n",
        "  var_replicas(cond, replicas)\n",
        "  gl,n  =exp_eft_dados(cond,replicas)\n",
        "  int_eft_replicas(cond,replicas)\n",
        "  replicas.to_excel('replicas.xlsx')\n",
        "  valor_t = t_value(replicas)\n",
        "  eft_replicas = int_eft_replicas(cond,replicas)\n",
        "  efeitos_replicas,efeitor2 = efeitos_replicas1(cond,eft_replicas)\n",
        "  efeitor4, qdr_medio, por_medio = qdr_por_medio(efeitor2)\n",
        "  dados_efeito_r = gaussiana_replicas(cond)\n",
        "  gauss2 = dados_gr(cond, dados_efeito_r,efeitos_replicas,efeitor4,qdr_medio,por_medio,efeitor2)\n",
        "  gauss2 = gauss2.sort_values(by=['Efeitos'])\n",
        "  inter_c = inter_confianca(valor_t, gauss2, gl)\n",
        "  dados_efeito2 = (dados_efeito1, replicas, valor_t, eft_replicas, efeitor2, efeitor4, gauss2, inter_c)\n",
        "  return dados_efeito2"
      ],
      "execution_count": 62,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xiBio8fLZSDs"
      },
      "source": [
        "def aghata_efeito():\n",
        "  dados_efeito2 = reorg_pf()\n",
        "  graficos_replicas(dados_efeito2[-2], dados_efeito2[-1])\n",
        "  salvar_planilhas(dados_efeito2[0][-2],dados_efeito2[-2],dados_efeito2[1])\n"
      ],
      "execution_count": 70,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "koS1LWmcqi0a",
        "outputId": "b3a165c4-b6e4-4423-a7f1-8699e4408714"
      },
      "source": [
        "aghata_efeito()"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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GEDI+Ne/NqlTp2vqbVu5slIzZz6vEye+U0xMjMaMGeun6gAgcBEGEBK2b69SaelrmjZtVr3tAwaka8CAdO3Z87UqK5erdevWfqoQAAIXrxlAQDpTU6NjO6p0pqbmgmO/+WaPnnjiMf3pT4/rhht6nHNMhw7/oU6drtGsWdObu1QACHqsDCCgeOrqtGFigarK5sliC5PhrlOXocPVq3DaOcfv2+fS2LGjdf/9I5We/ptGz+12u7V3L68ZAICzEQYQUDZMLFDVm/Plrq31btv65nyd8bjluT5ZHo9bp06dks1m05Ejh/XYYw/rt7+9R9nZdzc413vvLdUtt6QoNra1du78SvPnv67evfv4sh0ACAqEAQSMMzU1qiqbVy8ISNLGqCjN+WSt9MlaSdL776/QiBEPymKxyOncq9LSOSotneMd/8EH34/bsuVfmjPnZZ08eUIxMbHq3z9No0Y97LuGACBIEAYQME7sd8lia/gjeeOhQ+pde0rDN/1T7lhHvX0PPPCHBuN/MH78pGavEQBCES8gRMCISnDIcNedc5/hdsuemOjjigDAHAgDCBjhdru6DB0uW2Rkve22yEh1GZqnFna7nyoDgNDGZQIElB/eNVBVNl8Wm02G260u9+Wd990EAIBLRxhAQLGGhan38zP16wmTdWK/S1EJDoWzIgAAlxVhAAEp3G5XK3sXf5cBAKbAawYAADA5wgAAACZHGAAAwOQIAwAAmBxhAAAAkyMMAABgcoQBAABMjjAAAIDJEQYAADA5wgAAACZHGAAAwOQIAwAAmBxhAAAAkyMMAABgcoQBAABMjjAAAIDJEQYAADC5gAgDy5YtU0ZGhq677jq98cYb5x23fv163XDDDcrKylJWVpZyc3N9WCUAAKEpzN8FSFJycrKKioo0Z86cC47t3Lmz3nnnHR9UBQCAOQREGOjataskyWoNiIUKAABMJeh+++7atUs5OTnKzc3VkiVL/F0OAABBzycrAzk5OXI6nefct27dOtlstp91nuuvv15r1qxRdHS09uzZoxEjRighIUF9+/a96Jri46Mv+phgQW/Bid6CE70Fr1Du72J780kYaK5n8Ha73ft1hw4dlJaWpk2bNjUpDBw8eLxZago08fHR9BaE6C040VvwCuX+zu7NarUoLs7eyBFBdpngwIEDMgxDknT06FF98skn+sUvfuHnqgAA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JiZGy5cvD4k5PFdvs2fPDvr5q6qq0qBBg3T11VerZcuWkqT27durpKREmzZt0qRJk3Tq1Cm1a9dOL7zwgtq0aePnii/O+fobNWqUnn32WVksFtXV1alHjx4aP368rrjiivOey1RhAAAANMRlAgAATI4wAACAyREGAAAwOcIAAAAmRxgAAMDkCAMAmqSoqEi9e/dWv379Ljh21KhRl/TBWQAuL95aCOC8UlNT9e2339b7uOecnByNGjXKezvsuLi4izrnO++8o0WLFmnBggXNXS6AJgqpjyMG0Pxmz56tvn371tu2ceNGxcTEXHQQABCYuEwA4KKsW7dODzzwgA4cOKAePXqooKBAkrR582bde++96tmzpzIzM7V+/XrvMXl5eVq0aJF27NihSZMmafPmzerRo4f3FrLHjx/Xk08+qT59+qh///56+eWX5fF4JEm7d+/WsGHDdOONN6p3794aO3as75sGQhwrAwAuSt++ffXqq68qPz9fH3/8saTv7xnx0EMPacaMGbr11lv16aef6rHHHtOKFSvqfU5/586dNWXKlAaXCQoLC3X8+HGtWrVKR48e1ciRIxUfH6/c3FwVFxerX79+mjdvns6cOaMtW7b4vGcg1LEyAKBRjzzyiHr27On98/bbbzcYs2zZMqWkpOi2226T1WpVv3791K1bN61Zs+aC53e73aqoqNDjjz8uu92u9u3ba8SIEXr33XclSWFhYXI6nTpw4IAiIiK8qwkAmg8rAwAaVVJS0uA1Az+9BCBJTqdTlZWVWr16tXdbXV3dz7pV9pEjR3TmzBklJiZ6tyUmJnrvUJmfn6/i4mLdfffdatWqlUaMGKG77777UloCcBbCAIBL5nA4lJWVpalTp15wrMViqfc4NjZW4eHhcjqdSkpKkiS5XC7vranj4+O95924caNGjBihXr16qWPHjs3cBWBeXCYAcMkyMzO1evVqrV27Vm63W6dOndL69eu1b9++BmPj4uK0f/9+nT59WpJks9mUnp6uoqIi1dTUaO/evSotLVVmZqYkacWKFd7ztGrVShaLRVYr/3UBzYmVAQCNevjhh+t9zkDfvn01fPjwemMcDodefvllvfDCC3r88cdltVr1q1/9SpMnT25wvj59+igpKUm33HKLLBaL1q9fr4kTJ6qwsFBpaWmKiIhQbm6uBg8eLEnasmWLnnvuOdXU1CguLk4TJkxQhw4dLmvPgNnwoUMAAJgca20AAJgcYQAAAJMjDAAAYHKEAQAATI4wAACAyREGAAAwOcIAAAAmRxgAAMDkCAMAAJjc/wG3thDwShXDmgAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 576x648 with 1 Axes>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfgAAAIuCAYAAABTpxrQAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deVyU5f7/8TcMoBmISiKgntwK+blFLmiLe+kpXFMxKo+7mUt5Tm4trrllZriv2VctK8ulyI7b0VwqtywtU8ujmYGgLApu4DC/P3w4RwJxQO7RLl/Px8PHY+aee67rc19zj2/u675nxsPhcDgEAACM4nmrCwAAAIWPgAcAwEAEPAAABiLgAQAwEAEPAICBCHgAAAzkdasLAPJr+vTpmjFjRrZlnp6e8vf31wMPPKCePXuqTp06t6g6a61YsUJ//PGHJGnAgAG3uJq/lueee047d+687uMTJkxQ+/btJUl2u10xMTGKjY1VYmKiMjMzVbVqVa1evTpffYaGhkqS6tWrpyVLlkiSTpw4oZUrVzqXR0REFGRzgBsi4GGErKwspaSkaNOmTfrqq680bdo0PfbYY7e6rEK3cuVKZ0gR8Nb5+OOPNXfuXEva/uOPP5x/oPbv35+Ah2UIePyl9e/fXwMGDFB6eromT56sDz/8UFlZWZo4cWKhBvylS5dUpEiRQmsPt9bixYvzDNaffvrJ5XXzcujQoQI9DygMnIOHEXx9fTVo0CDn/RMnTig5Odl5f8WKFercubPCw8NVvXp1NW/eXOPGjcu2jiQ1bdpUoaGhatq0qXbv3q3OnTurZs2aGjlypHOddevWqVu3boqIiFD16tX16KOPqn///jpz5oxznZMnT2rkyJFq2rSpqlevrrp166pnz57atWtXtv6mT5+u0NBQhYaGasOGDRo9erQeeugh1a5dW927d9exY8ec2xMaGpptivnq865OA8fFxWnQoEFq2bKl6tatq2rVqikiIkI9evTQ9u3bc4zZV199pdatW6tGjRpq0aKFVq1apWHDhjnb3LFjh3PdrKwsvf/++3rqqacUHh6umjVrqlWrVlq4cKEuX76cbdyvPv+5557T2rVr1bJlS9WsWVPPPvusjhw5osTERA0YMEDh4eFq0qSJZsyYoaysrDxf31mzZjnbXbRokXP58OHDs41fYQgNDdXy5cud97t06aLQ0FANGzbMuezzzz/XM888o9q1a6t69epq0aKFpk6dqgsXLuRo6+pYSNKwYcPUpUsX5+MzZsxwrjN9+nTn8o0bN6pr166qW7euqlevrsaNG+uVV17RiRMnsrV/8OBB9e/fX48++qiqV6+uiIgItWvXTiNGjFBmZmahjAf+ujiChzGuFxIjRozQRx99lG3Z77//rsWLF2vjxo366KOPVLp06WyPJycnq3v37rp06VK25ZMmTdK7776bbVliYqLWr1+vYcOGyd/fX//9738VHR2tlJQU5zqZmZnaunWrtm/frilTpuiJJ57IUefw4cN19uxZ5/3t27fr+eef1xdffOHS9icmJmrNmjXZlqWmpmrbtm36+uuvtWjRItWvX1+StGPHDvXt21d2u12SdOzYMQ0dOlSBgYE52s3KylL//v21cePGbMsPHz6sN998U7t27dLs2bPl4eGR7fFDhw7ppZdecr4uu3bt0vPPP68iRYrol19+kSSdP39e06dPV1BQkDp06HDdbevTp4+2b9+u3bt365133lHjxo119OhRrVixQpL09NNPq3nz5i6N080aO3asli5dmm3ZsWPHNGfOHG3btk3vv/++ihYtWuD2586dq7fffjvbsvj4eH366afasGGDPvjgA1WpUkUXLlxQ165ds+1nqampSk1N1YEDBzR06FB5e3sXuA789XEEDyOkp6crJibGeb98+fIqVaqU9uzZ4wz3smXLavXq1dq5c6fzYqo//vhD06ZNy9HehQsXVLduXW3YsEF79+7V888/r3379jnD3dfXVzExMdqzZ482b96s4cOH66677pIkjRs3TikpKfLz89PixYu1f/9+rVu3TpUqVVJWVpbGjBmjjIyMHH36+flp9erV2rp1qypXrixJOnr0qPbt26dy5crp0KFDqlevnnP9Q4cOOf9JUkhIiGbNmqUtW7Zo//79+v777zVnzhxJV0J68eLFzudOnTrVGe4DBgzQnj17NGXKFCUmJuao68svv3SGe58+fbRz507t2bNH//jHPyRJmzZt0vr163M878yZM3rttde0e/duhYeHS5KOHz+us2fPas2aNVq+fLnzj4Ib/RFjs9k0efJkFS9eXBcvXtTgwYM1YsQISdJ9992X7ejaFVePyq/9d/WPq0OHDqldu3bOdTdu3KhDhw5p4sSJ+v77753h3r59e23fvl0//PCDhgwZIkn68ccftWzZsuv2O3HixGyvQ//+/Z2v4YABA7Ltj8WLF9fSpUu1Z88e9e3bV9KVMR0/frwk6ciRI85wHzx4sPbv369vvvlGH3zwgfr06SMvL47f7nTsAfhLmzFjRo4r6j08PDR48GBJV6ahr+rSpYuqVq0q6crR8sqVK+VwOLKtc63x48erTJkykqQKFSpo6tSpzse6deumli1bSroS9l27dpUkXbx4Ud98840kKS0tLdt07FUpKSk6cOCAHnjggWzLu3fv7qyvUaNGOnLkiKQrU+9XAzIvJUqU0OHDhzVt2jQdP35c58+fz/b40aNHJV05av7hhx+cz+nbt69sNpsiIyO1dOlS7d27N9vz/vOf/zhvz507N9eLz7Zt26bHH38827KgoCA988wzkqTatWs7223fvr3zD5h77rlHp06dUlxc3A23LyQkRKNHj9agQYO0f/9+SVKRIkU0ZcqUmzpizo9NmzY5b69YscI5g3Ctbdu2qVu3bgVqf9u2bc5THm3atFHdunUlXfkj7MMPP1RKSop27NihS5cuKTg4WF5eXrp8+bLWrFmjixcvqlKlSqpWrZr++c9/Fqh/mIWAhxE8PDzk7++vWrVqqXv37s6p6GvPsQcHBztvFy9eXL6+vkpLS8txHl6SAgICnOF+VVJSkvP21YD6szNnzjiPjPOSmpqaY1nFihWdt6/OBkjKcZrget54440cpyKudbWds2fPOqfNAwMDZbPZnOuEhITkCPjcxufPctuekJAQ5+1rA7hs2bLO2z4+PpLk8vnili1b6u2339bvv/8uSWrQoIHzGoT8KOiFc9fuA9eT21i46tqxvnb8bDabypQpo5SUFF2+fFmpqakqU6aMRo0apSlTpuinn37KdmFg7dq1NW/ePPn6+ha4Fvz1EfD4S7t6Ff31BAQEOG/Hx8c7b589e1bp6emSpFKlSuV4Xm5HhNe2dfXo+s/8/f1ls9lkt9tVoUIFrV27Nsc6Docjx/lqSdmmVHN7/Eaunn/38fHR4sWLVaNGDV28eFG1a9fOUaOnp6eysrJ06tQpZWVlydPzytm6a8foqmvH54MPPsjR3tVtymt7rnXtHxT5NW/ePGe4S9LmzZu1fv16t30k8tp9YPLkyWrdunWOdW70C9x5vbbXtn/trIbdbldCQoKkK+NaokQJSVLHjh3Vvn17HTlyRMeOHdPOnTu1ZMkS7dmzR++//7769Onj2obBSJyDh9EaNWrkvL148WIdOnRIZ8+e1aRJk5z/ETdu3Niltpo1a+a8/d5772ndunU6d+6cEhIStGTJEiUlJalo0aJq0KCBpCsXXr355ptKSkpSRkaGjhw5okWLFjnPXRdEyZIlnbd//vnnbI9dDU5PT08VL15cFy5c0Jtvvpmjjbvuuku1atWSdOV0wcKFC5Wenq4vvvhC3333XY71mzRp4rw9btw4HTx4UBkZGTp9+rTWr1+vPn365Ph0gBV++OEH55Xmjz32mO6//35J0muvveYMP6tdu69cvQYjIyNDqamp2rJli/71r3/ps88+y7ONq+EsXflD8drrMR555BHnH0afffaZdu/erfT0dM2cOdN5vr1+/foqUqSIkpOTNWnSJO3du1cBAQFq0qRJtn3UldMeMBtH8DDagw8+qKioKH300Uf6448/chxxlS1b1uUvjKlZs6a6d++ud999V2lpaTmedzUIX3nlFUVHRys1NVULFy7UwoULc/RZULVq1XLOCrRt21bS/74l7bHHHtPy5ct18eJF51X6FSpUyLWdQYMGqVu3brLb7Xrrrbf01ltvSZJKly6tU6dOSfrfkeYTTzyhzz//XJs3b9ZPP/2kNm3a5Give/fuBd4mV6Snp+tf//qXLl++rNKlS2vs2LE6efKkOnbsqNTUVA0ePFjvvfeecybiRnK7NqJLly569dVX83xeeHi4nn76aS1btkwnTpxQdHR0jnUefvjhPNu49957VbJkSaWkpOjLL7/Ul19+Kel/pw0GDhyot99+W2fOnHFew3CVv7+/hg8fLknKyMjQu+++m+NTHVc9+uijedYB83EED+ONGTNGEyZMUHh4uIoVKyZvb2+VL19eXbp00SeffJLjI3J5GTp0qKZNm6aHHnpI/v7+8vb2VmBgoJo3by4/Pz9JV87Pr1q1Sk8//bTKly8vb29v+fn5qUqVKurQoYNGjRpV4G155pln1LlzZ5UuXTrHVO/w4cPVuXNnBQQEqFixYmrSpEm2z4xfKyIiQrNmzdL9998vb29vVahQQZMmTVK1atWc61w90vT09NSsWbM0YsQI1apVS8WKFZOPj4/Kli2rRx99VCNGjMj2PCuMGjXKOTU/duxYlSxZUmFhYc4/snbs2KEFCxZY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\n",
            "text/plain": [
              "<Figure size 576x648 with 1 Axes>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a variável 1 insignificante?(V1, V2, V3 ou V4): v1\n",
            "Pressione qualquer tecla para continuar para inserir mais uma variável, caso contrário digite \"N\" para sair. a\n",
            "Digite a variável 2 insignificante?(V1, V2, V3 ou V4): v4\n",
            "Pressione qualquer tecla para continuar para inserir mais uma variável, caso contrário digite \"N\" para sair. n\n",
            "Variância experimental igual a 27.125 e Erro experimental igual 5.208166663999915\n",
            "Erro de um Efeito: 2.6040833319999575\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhQAAAIwCAYAAADeR/LFAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeVyU5f7/8TcMICK4QMABl1CPqZma5vK1XNLEMFFQM3fNtVKz7FQulVt1PFp50o7L0SzTY+rBXURFzaW0UtPUJEtLUgFRWdzAQJjfH/68DxPb4A0I+Xo+Hj4eM/d93dd85pqRec91L+NgtVqtAgAAMMHxbhcAAABKPwIFAAAwjUABAABMI1AAAADTCBQAAMA0AgUAADCNQFFIwsLC1KVLFzVq1Ei1a9dW7dq19e233xa4n3Pnzhnb165duwgqRVH6s71+r776qmrXrq1HHnlEV65cKfD2V65cUePGjVW7dm299tprRVBh6ZHXeyPr8nPnzt2lCgFznO52ASXNmjVrNH78+DzbNGvWTEuXLjXuR0ZG6s033yzq0rR9+3b9+OOPRg3Nmzcv8scsLAkJCQoLC9PevXt16tQpXb16VW5ubvL09FRAQIBat26t9u3by8fH526Xiv/v2LFjCg8PlyT16dNH5cuXL3Af5cuXV58+fbRw4UJt3LhRAwcO1EMPPVTYpdpo166dYmJibJZZLBZ5eHioZs2aeuqpp9SrVy85Od3bf/4WL16sq1evSpK6du2qKlWq3OWKUNrd2/+jCsm2bduM2+3atdOzzz4ri8VyR99QfXx8tGzZshzXbd++XWvXrpUkjRo1qtQEig0bNmjy5Mm6fv26zfLLly/r8uXLOn36tHbu3KnY2Fi9+uqrd6nKwpHX61fazJkzR1arVQ4ODurTp88d99O3b199/PHHslqtmjt3rubOnVuIVdonIyNDycnJ+u677/Tdd9/pyJEjeu+994q9jtxkfc8UV6hesmSJEbyaNWtGoIBpBIp85PTh4OHhYXM/Pj7euN2+fXtTH/QuLi5q0qTJHW9f0kREROj111/X7Quy+vr6qnfv3qpXr56cnZ0VHx+vQ4cOKTIy8i5XWjj+LK9fTEyMdu/eLUl65JFH5Ofnd8d9+fn5qXHjxvruu++0a9cuxcfHy9fXt7BKzVO3bt3UvXt3JScn6+OPP9bhw4cl3Qq5r776arHVkZ8/w3sGIFDkI6//6DntHpkwYYImTJggSfrpp58k3fp2FBYWpg0bNujkyZNKTU2Vt7e3HnvsMT333HOqWrWqsf25c+f0xBNPGPd/+uknffvttxowYIDN4/zrX//Sv/71L0m2u2DS0tK0fPlyRURE6NSpU/r999/l5eWlJk2aaNCgQXZNN//973/XZ599Jkn6v//7Py1evFgODg5KTU1VaGiooqOjJUkTJ05U3759c+3n+vXrevvtt40wUbt2bS1dulQVKlSwaRcaGqo33nhDZ8+eNZZlZGRo2rRpioqK0tmzZ3XlyhVlZGTI29tbjRs31tChQ1W3bl2jfdYxqly5sr744gtj3UcffWSMVdeuXfWPf/zDGKsFCxYoMjJSZ86c0c2bN1WhQgVVqVJF9evX13PPPSdvb29J0i+//KK5c+fq4MGDSkhIkJOTkzw9PVWrVi099thjxmPn9PplrePgwYP67bffdPnyZaWnp6tixYpq2LChBgwYkC2IZp3h2rRpkzZu3KgNGzbo4sWLqlKlil544QWFhIQYbZKSkvTPf/5TP/74o+Li4nT58mU5ODjI19dXzZs3z/Zey8uWLVuUmZkpSWrTpo3Nupzej380bdo0devWzbj/+OOP67vvvlNGRoY2b96sZ5991q46zPL39zf+D/v6+urpp5821sXFxWULFBEREVq1apWOHz+u69evq2LFimrWrJmGDx+uOnXq2LT94+uzfv16bdy4UZcuXdL999+vZ599Vj169LCrzqx97dixw2a24MyZM/r000/19ddfKy4uTg4ODvrLX/6ipk2b6q233pKLi0uBXvus/x9uy/p6jho1Si+++KK++uorhYWF6aefflJSUpKuXbsmV1dX1ahRQ0899ZT69esnZ2dnY7v4+HjNmTNHe/fuVXx8vBwdHVWpUiXVqFFDjRo10ujRo+0aC5ReBIoiduPGDQ0fPjzbAZqxsbEKCwvT1q1btWjRIjVo0MD0Y6WkpGjQoEH6/vvvbZafP39e4eHh2rJli959912Fhobm2c+rr76qAwcOKCoqSt98842WLVumfv366f333zfCRPv27fMME5K0e/duJSYmGvffeOONbGHitjJlyuivf/2rcf/mzZs2x6ncFhsbq9jYWG3dulXLli1Tw4YN86whL2+99ZbWrVtns+zSpUu6dOmSvv/+ewUHB8vb21tJSUnq06ePkpOTjXbp6emKiYlRTEyMfvvtt3w/YCVpxYoVunTpks2yixcvavv27dqxY4dmz56tDh065LjtyJEjjbGXpNOnT+v1119XtWrV1KhRI0lSYmKiVq5cmW3bM2fO6MyZM4qMjNTq1avtChUHDhwwbpsZ49uyvr+//fbbYgsUefnLX/5i3M7MzNRrr71mHDNy28WLF7Vp0yZt27ZNs2bNUrt27XLs66WXXtKpU6eM+6dOndKbb76pxMREPffcc3dc465du/Tyyy8rNTXVZvnp06d1+vRpvfbaa3JxcSnU1/62b775Rlu2bLFZdu3aNR09elRHjx7VgQMHjN1X6enp6tevn86cOWPT/vz58zp//rwOHjxIoLgHECjykdNxEOPHj9ezzz6rNm3aaNmyZXrnnXeMgyWff/55tWrVymj70UcfGWGiSpUqGjlypHx9fRUZGakVK1boypUreuWVV7Rly5ZcDxJ78MEHtWzZMv373//Wnj17JP1vKlf63y6YWbNmGWHCzc1NY8aMUbVq1RQWFqbt27fr5s2beuutt9S8efM8p7BdXFw0c+ZMdevWTSkpKXr//fdlsViM3T9+fn5699138x27H374wbhdtmxZNW3a1LiflJSkX375Jds2jzzyiBwcHGSxWDRixAjVqFFDFSpUkKurq1JTU7Vv3z4tXrxY6enpmjNnjhYsWJBvHbm5vZvFw8NDEyZMkL+/vxITE/Xrr79q165dcnS8dRLUt99+a4SJ5s2ba/DgwXJyclJ8fLwOHz5sM7OSl4EDB8rHx0eVKlVS2bJllZaWpuPHj2vmzJmyWq2aNWtWroEiPj5e48ePV9WqVfXhhx/q559/liQtXbrUCBQVKlTQ6NGjVb16dXl4eKhMmTK6fv26IiIitGHDBl2+fFmffPKJJk2alG+tt/uXpICAAJt1t9+PWWV9b1aqVEmNGze2WV+9enXjdtZZm6IWGxurgwcP6vLly1q0aJGxvEOHDjaBYsWKFUaYqFSpkl588UVVr15d+/fv1/z585WWlqbXX39dO3bsyDEUx8fHa+LEifL399eKFSu0a9cuSdLs2bMVHBysypUrF7j2xMRE/e1vfzPCRNWqVTVs2DBVrlxZZ8+eNY6nkgr22nfv3l0tWrTQyy+/rIsXL0qS3nzzTWPGz9/fX5LUtGlT+fr6ys/PT+XKlZODg4MuXryojz76SL/99pt27Niho0ePqkGDBjpx4oQRJmrXrq3Ro0fLzc1NFy5c0PHjx/X1118X+Pmj9CFQmODl5SUvLy+bYyruv/9+Y4rVarVqzZo1xrr+/furWrVqkqTOnTtrx44dunjxos6ePauvv/7aJohk5eHhoSZNmmjVqlXGsqxTubcfK+u37dGjRxvfmh999FE98cQTunDhgtLS0rRp0yYNHTo0z+dWvXp1vfXWWxo/frxSU1M1efJkSbeOln///fdVsWLFfMcn62mG5cuXNz6gpVsf0i+99FK2bY4ePaoyZcrIyclJrVq10uLFi3X06FFdunRJ6enpNm2PHDmSbw15cXd3V0pKisqWLauAgADVqVNHbm5ukm5N+96W9fX19vZW9erVVaVKFVksFiPU2aNdu3ZauHChDh48aLwWWZ06dUrXrl2Tu7t7tm1HjRplfKv//fffNWbMGEmymbW47777VK9ePS1fvlzHjx9XUlKSbt68adOPvWOWdWbpj6/17ffjbYsWLTLCRLly5fTxxx9nCyFZP4Sz9p2bq1ev5hg8ateune0YprysWbPG5v+gi4uLBg0aZPP6SrL5v9WtWzfji0TLli21e/duRUVF6erVq9q8ebN69eqV7XHGjBljzNi1aNFCbdu2VWJiom7evKlt27bd0YzM5s2bde3aNUm3viAsW7bMZhdN7969jdsFee39/f3l7+8vFxcXY90DDzyQbfdus2bNFBUVpblz5+q3337T9evX9ccfpz5y5IgaNGhg85rcPnPr/vvvl7Ozc74zovjzIFDkI6eDMu2dNkxMTLT54zlt2rRc2548eTLXQGHvY2Wdkn/kkUeM2y4uLmrQoIG2b98uSfr111/t6rNbt27as2ePNm/ebCx77rnn7D6ALOsfmStXrigzM9MmVORl7969GjZsmDIyMnJtc/nyZbv6yk2vXr00e/ZsXbhwwfjj7Ovrq3r16qlz58566qmnJN06jqZWrVo6efKkwsPDFR4eLmdnZwUEBKhJkybq16+fze6anPz000/q1auXUlJS8mx35cqVHANFixYtjNtZP+CzvuarVq3SG2+8kWf/dzJmf/wQyeq///2vZsyYIenWbqt58+bleJxOXn3kJCoqKsfdSEuWLDF10HNaWpoOHz6stLQ0mw/UrLNlixYtspnN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\n",
            "text/plain": [
              "<Figure size 576x648 with 1 Axes>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAf8AAAIuCAYAAACxewGpAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3dfVhUdf7/8RczolaICnEzqJs3FbGKrXdomZqJyW4g3mQqtW6St1lubqlYLYKtGVq5aFGtmV50t8Z6l4hmuJo3tZqulV9JK7+6liAYSIJ5O8zvD3/OOl8UR2MG5fN8XJfXdeaczznzPuOHec35nDNzfBwOh0MAAMAYlpouAAAAeBfhDwCAYQh/AAAMQ/gDAGAYwh8AAMMQ/gAAGKZOTRcAVKe5c+fqlVdecZlnsVjUsGFD/eY3v9GIESPUsWPHGqrOs5YsWaKDBw9Kkh5//PEaruba8vvf/15bt2696PIZM2ZowIABkiS73a709HRlZ2erqKhIp0+f1m233ably5df1nOGh4dLkqKiovT2229Lkn744QctXbrUOb9z585XsjvAJRH+qPUqKip05MgRrVu3Tp988onmzJmj3r1713RZ1W7p0qXOACP8PeeDDz7QG2+84ZFtHzx40Pnh9bHHHiP84TGEP2qtxx57TI8//rjKy8s1a9Ys/f3vf1dFRYVeeOGFag3/kydPql69etW2PdSszMzMKkN3165dbretyp49e65oPaA6cM4ftZ6fn58mTJjgfPzDDz+opKTE+XjJkiUaMmSI2rVrpzZt2ig6OlrTp093aSNJ99xzj8LDw3XPPfdo27ZtGjJkiNq2baupU6c626xZs0bDhw9X586d1aZNG3Xr1k2PPfaYfvrpJ2ebQ4cOaerUqbrnnnvUpk0bderUSSNGjNDnn3/u8nxz585VeHi4wsPDlZubq9TUVN15553q0KGDEhMTtX//fuf+hIeHuwxbn1vv3NByfn6+JkyYoJiYGHXq1EmtW7dW586d9cgjj2jz5s2VXrNPPvlEffv2VWRkpPr06aNly5YpKSnJuc0tW7Y421ZUVOjdd9/VwIED1a5dO7Vt21ZxcXGaP3++zpw54/K6n1v/97//vT766CPFxMSobdu2euihh7R3714VFRXp8ccfV7t27dSzZ0+98sorqqioqPL/NyMjw7ndBQsWOOdPmTLF5fWrDuHh4crKynI+HjZsmMLDw5WUlOSct2LFCj344IPq0KGD2rRpoz59+mj27Nk6fvx4pW2dey0kKSkpScOGDXMuf+WVV5xt5s6d65y/du1aPfzww+rUqZPatGmju+++W08//bR++OEHl+3v3r1bjz32mLp166Y2bdqoc+fO6t+/v5KTk3X69OlqeT1w7eLIH0a4WIAkJydr0aJFLvO+//57ZWZmau3atVq0aJGCgoJclpeUlCgxMVEnT550mZ+Wlqa33nrLZV5RUZE+/vhjJSUlqWHDhvrf//1fJSQk6MiRI842p0+f1saNG7V582a99NJL+t3vflepzilTpujo0aPOx5s3b9aYMWO0cuVKt/a/qKhIOTk5LvNKS0u1adMmffrpp1qwYIG6dOkiSdqyZYvGjh0ru90uSdq/f78mT56s4ODgStutqKjQY489prVr17rM/+abbzRz5kx9/vnneu211+Tj4+OyfM+ePXriiSec/y+ff/65xowZo3r16unbb7+VJP3888+aO3euQkNDdf/9919030aPHq3Nmzdr27Zt+utf/6q7775b+/bt05IlSyRJQ4cOVXR0tFuv0y/13HPP6Z133nGZt3//fr3++uvatGmT3n33XdWvX/+Kt//GG2/o5ZdfdplXUFCgxYsXKzc3V++9955uvvlmHT9+XA8//LBLPystLVVpaany8vI0efJk+fr6XnEduPZx5I9ar7y8XOnp6c7HzZo1U0BAgLZv3+4M/iZNmmj58uXaunWr88KugwcPas6cOZW2d/z4cXXq1Em5ubnasWOHxowZo6+++soZ/H5+fkpPT9f27du1fv16TZkyRdddd50kafr06Tpy5IgaNGigzMxM7dy5U2vWrFHLli1VUVGhadOm6dSpU5Wes0GDBlq+fLk2btyoVq1aSZL27dunr776Sk2bNtWePXsUFRXlbL9nzx7nP0kKCwtTRkaGNmzYoJ07d+qLL77Q66+/LulsgGdmZjrXnT17tjP4H3/8cW3fvl0vvfSSioqKKtW1atUqZ/CPHj1aW7du1fbt2/WHP/xBkrRu3Tp9/PHHldb76aef9Oyzz2rbtm1q166dJOnAgQM6evSocnJylJWV5fzAcKkPOFarVbNmzZK/v79OnDihiRMnKjk5WZJ0yy23uByVu+Pc0fz5/8598NqzZ4/69+/vbLt27Vrt2bNHL7zwgr744gtn8A8YMECbN2/Wl19+qUmTJkmS/ud//kfvv//+RZ/3hRdecPl/eOyxx5z/h48//rhLf/T399c777yj7du3a+zYsZLOvqbPP/+8JGnv3r3O4J84caJ27typzz77TO+9955Gjx6tOnU47jMdPQC11iuvvFLpyn8fHx9NnDhR0tmh7XOGDRum2267TdLZo+ylS5fK4XC4tDnf888/r5CQEElS8+bNNXv2bOey4cOHKyYmRtLZDwIPP/ywJOnEiRP67LPPJEllZWUuQ7znHDlyRHl5efrNb37jMj8xMdFZX48ePbR3715JZ4fzz4VnVRo1aqRvvvlGc+bM0YEDB/Tzzz+7LN+3b5+ks0fbX375pXOdsWPHymq1KjY2Vu+884527Njhst4///lP5/Qbb7xxwQvhNm3apHvvvddlXmhoqB588EFJUocOHZzbHTBggPPDzY033qjDhw8rPz//kvsXFham1NRUTZgwQTt37pQk1atXTy+99NIvOtK+HOvWrXNOL1myxDnycL5NmzZp+PDhV7T9TZs2OU+jxMfHq1OnTpLOfkD7+9//riNHjmjLli06efKkbDab6tSpozNnzignJ0cnTpxQy5Yt1bp1a/3pT3+6oudH7UL4o9bz8fFRw4YNdfvttysxMdE5vH3+OX2bzeac9vf3l5+fn8rKyiqd95ekwMBAZ/CfU1xc7Jw+F17/108//eQ8oq5KaWlppXktWrRwTp8bRZBU6dTDxfzlL3+pdHrjfOe2c/ToUedQfHBwsKxWq7NNWFhYpfC/0Ovzf11of8LCwpzT54dzkyZNnNN169aVJLfPT8fExOjll1/W999/L0m64447nNc8XI4rvYjv/D5wMRd6Ldx1/mt9/utntVoVEhKiI0eO6MyZMyotLVVISIhSUlL00ksvadeuXS4XKXbo0EF/+9vf5Ofnd8W14NpH+KPWOne1/8UEBgY6pwsKCpzTR48eVXl5uSQpICCg0noXOpI8f1vnjsr/r4YNG8pqtcput6t58+b66KOPKrVxOByVzo9LchmmvdDySzl3vr9u3brKzMxUZGSkTpw4oQ4dOlSq0WKxqKKiQocPH1ZFRYUslrNnB89/jc45//V57733Km3v3D5VtT/nO//DxuX629/+5gx+SVq/fr0+/vhjr32t8/w+MGvWLPXt27dSm0vdQb2q/9vzt3/+aIjdbldhYaGks69ro0aNJEmDBg3SgAEDtHfvXu3fv19bt27V22+/re3bt+vdd9/V6NGj3dsx1Eqc84exevTo4ZzOzMzUnj17dPToUaWlpTnfpO+++263ttWrVy/n9MKFC7VmzRodO3ZMhYWFevvtt1VcXKz69evrjjvukHT2IrCZM2equLhYp06d0t69e7VgwQLnufIr0bhxY+f0119/7bLsXKhaLBb5+/vr+PHjmjlzZqVtXHfddbr99tslnT0FMX/+fJWXl2vlypX697//Xal9z549ndPTp0/X7t27derUKf3444/6+OOPNXr06ErfYvCEL7/80nlFfO/evXXrrbdKkp599llnMHra+X3l3DUfp06dUmlpqTZs2KAnn3xSH374YZXbOBfc0tkPkedf/3HXXXc5PzR9+OGH2rZtm8rLy/Xqq686z+936dJF9erVU0lJidLS0rRjxw4FBgaqZ8+eLn3UnVMpqN048oex2rdvr8GDB2vRokU6ePBgpSO1Jk2auP1jOW3btlViYqLeeustlZWVVVrvXEg+/fTTSkhIUGlpqebPn6/58+dXes4rdfvttztHE/r16yfpv78e17t3b2VlZenEiRPObxM0b978gtuZMGGChg8fLrvdrhdffFEvvviiJCkoKEiHDx+W9N8j1N/97ndasWKF1q9fr127dik+Pr7S9hITE694n9xRXl6uJ598UmfOnFFQUJCee+45HTp0SIMGDVJpaakmTpyohQsXOkcwLuVC12IMGzZMzzzzTJXrtWvXTkOHDtX777+vH374QQkJCZXadO3atcpt3HTTTWrcuLGOHDmiVatWadWqVZL+eypi/Pjxevnll/XTTz85r5k4p2HDhpoyZYok6dSpU3rrrbcqffvknG7dulVZB2o/jvxhtGnTpmnGjBlq166drr/+evn6+qpZs2YaNmyY/vGPf1T6ml9VJk+erDlz5ujOO+9Uw4YN5evrq+DgYEVHR6tBgwaSzl4PsGzZMg0dOlTNmjWTr6+vGjRooJtvvln333+/UlJSrnhfHnzwQQ0ZMkRBQUGVho+nTJmiIUOGKDAwUNdff7169uzp8p3483Xu3FkZGRm69dZb5evrq+bNmystLU2tW7d2tjl3hGqxWJSRkaHk5GTdfvvtuv7661W3bl01adJE3bp1U3Jysst6npCSkuIc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9u2rxMREb9UKAACqQZXh/8knn2jz5s3y9fXVyZMn9cADD2jChAnq3r27OnfurDfeeMNbdQIAgGpSZfhHRkZq7ty56ty5sz799FPdfvvtzmX16tXT+PHjPV4gAACoXlWe809PT5e/v78+/vhjhYWF6dlnn/VWXQAAwEOqPPL38/PTiBEjvFULAADwgose+c+YMUOHDx+ucuXDhw9rxowZ1V4UAADwnIse+bdo0UKDBg1Sq1at1KlTJ7Vo0UI33HCDjh07pv3792vr1q3at2+fxo4d6816AQDAL3TR8B8yZIgGDhyotWvXasOGDcrNzVVZWZn8/f0VHh6uIUOGqGfPnqpT57JvDAgAAGpQlcnt6+urmJgYxcTEeKseAADgYZd1S18AAHDtI/wBADAM4Q8AgGEIfwAADOP2pfrHjx/Xf/7zH/38888u89u3b1/tRQEAAM9xK/yXLVumadOmydfXV/Xr13fO9/Hx0fr16z1VGwAA8AC3wn/WrFmaO3euunbt6ul6AACAh7l1zt/X11dRUVGergUAAHiBW+H/xz/+US+88IJKSko8XQ8AAPAwt4b9mzdvrjlz5ui9995zznM4HPLx8dHXX3/tseIAAED1cyv8J02apPj4eP3ud79zueAPAABce9wK/9LSUv3xj3+Uj4+Pp+sBAAAe5tY5/wEDBmj58uWergUAAHiBW0f+X331ld5991299tpruvHGG12Wvfvuux4pDAAAeIZb4f/AAw/ogQce8HQtAADAC9wK//79+3u6DgAA4CVunfN3OBz64IMPNGzYMMXFxUmSPv/8c+Xk5Hi0OAAAUP3cCv/09HT94x//0ODBg1VQUCBJCg0N1ZtvvunR4gAAQPVzK/yXLl2q119/Xffdd5/z635NmzbV999/79HiAABA9XMr/O12u2644QZJcob/sWPHdP3113uuMgAA4BFuhX+PHj00Y8YMnTp1StLZawDS09PVs2dPjxYHAACqn1vhP2XKFB0+fFgdOnRQWVmZ2rVrp/z8fD311FOerg8AAFQzt77q5+fnp1dffVU//vij8vPzZbPZFBQU5OnaAACAB7gV/hUVFZKkgIAABQQEOOdZLG4NHAAAgKuIW+H/61//+oI39bFarQoODta9996rxx9/3HlRIAAAuHq5Ff5//vOflZubq1GjRik0NFQFBQV688031aNHD7Vo0UKvvvqqnn/+eU2fPv2i29i3b5+SkpJUWlqqRo0aKS0tTc2bN3dp8+qrryonJ0cWi0W+vr6aMGGCunXrJkk6fvy4pkyZol27dslqtWry5MlccAgAwBVwK/wXLFigpUuXqkGDBpKkFi1aqE2bNhowYIByc3MVHh6uAQMGVLmNqVOnKiEhQfHx8Vq+fLmSk5OVmZnp0qZt27ZKTEzUddddp927d+uhhx7Spk2bVL9+fc2fP19+fn76+OOPtX//fj344INas2YNow0AAFwmt07al5eX6/jx4y7zjh8/rrKyMknSjTfeqBMnTlx0/eLiYuXl5d7MpTIAABpPSURBVCk2NlaSFBsbq7y8PJWUlLi069atm6677jpJUnh4uBwOh0pLSyVJq1at0uDBgyVJzZs3V5s2bbRhwwZ3ygcAAOdx68i/X79+SkxM1LBhwxQaGqrCwkJlZmY6b/izadMmtWjR4qLrFxQUKCQkRFarVdJ/rxUoKChwXkD4fy1btky/+tWvFBoaKknKz89XkyZNnMttNpsOHTrk3l4CAAAnt8J/0qRJuummm7Ry5UoVFRUpKChICQkJztv8dunSRZ07d662orZu3ar09HS99dZb1bZNSQoM9KvW7aF2CApqUNMloJahT6G6VXefciv8LRaLhg4dqqFDh15web169apc32azqbCwUHa7XVarVXa7XUVFRbLZbJXa7tixQxMnTlRGRoZatmzpnB8WFqaDBw86RwoKCgou+wNHcXG5Kiocl7WOxB9ybXf4cJnXn5M+VbvRp1DdLrdPWSw+VR7wuhX+kvTjjz/qq6++0pEjR+Rw/DdA77///kuuGxgYqIiICGVnZys+Pl7Z2dmKiIioNOT/1VdfacKECZozZ45at27tsiwmJkaLFi1SZGSk9u/fr507d+qll15yt3wAAPD/uRX+ubm5mjhxom666SZ99913uvnmm/Xtt9+qffv2boW/JKWkpCgpKUkZGRny9/dXWlqaJGnkyJEaP368IiMjlZqaqhMnTig5Odm53syZMxUeHq5HHnlESUlJ6t27tywWi6ZNmyY/P4bxAQC4XG6F/1//+lc9//zz+u1vf6tOnTpp2bJlWrx4sb777ju3n6hVq1bKysqqNH/evHnO6cWLF190/euvv15z5sxx+/kAAMCFufVVv/z8fP32t791mde/f38tW7bMI0UBAADPcSv8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p6KiwtGzZ0/H559/7nA4HI6jR486ly1cuNAxbtw4L+zNtYVhfwP16tVL//nPf7R3717nvCVLlmjAgAHq0qWLGjVqJEkKDQ1VcHDwZd9ACeapqk/5+fk5b+p18uRJnT59WhYLbz24sveiunXrKjY2VkuWLHGu869//Uu+vr7q2LGjJKlBgwbOZeXl5fS3C+AVMVDdunUVFxenxYsXSzr7x5Gbm6v+/fu7tNuyZYuOHj2qNm3a1ESZuIZcqk/t3LlTcXFxuvPOO9WlSxfdfffdNVgtrhZX+l40cOBALV++3Hm/mHMfGM43cuRIde3aVatWrdIzzzzjhb25thD+hrr//vv14Ycfym63a9WqVWrfvr3LjZK+++47TZ48WS+99JLq169fg5XiWlFVn4qMjNSKFSu0fv167dq1S9u2bavhanG1uJL3ol//+te68cYbtXHjRpWXl2vt2rXq18/1zqvz5s3Txo0bdd999+m1117z6j5dCwh/Q912220KDg7Whg0btHjxYg0cONC5bP/+/Ro1apRSU1Odw2jApVTVp84JCAhQ9+7dtXr16hqoEFejK30vGjhwoJYsWaKcnBx17NhRISEhlbZtsVh0//33a/ny5R7fj2sN4W+wgQMHau7cudq/f7969eolSfr+++/1yCOP6JlnnlGPHj1quEJcay7Up/bt26eKigpJ0s8//6wNGzbo1ltvrckycZW5kveiuLg4bdq0SW+//bbLB4aSkhKVlJQ4H69evVrh4eGe34lrDDf2MdhPP/2kbt266YEHHtCzzz4rSRo/frw2b97s8rWYp556St26daupMnENuVCfevPNN7V06VJZrVZVVFQoOjpa48eP5yIsOF3pe9ETTzyhf/3rX9q4caN8fX0lSXv27NGUKVN0+vRpSVKTJk30zDPPqFmzZl7co6sf4Q8AgGH46A0AgGEIfwAADEP4AwBgGMIfAADDEP4AABiG8AdwWWbPnq3OnTura9eul2w7YsQILV261AtVAbgcfNUPQCX33HOPfvzxR+cNeSSpf//+GjFihGJiYrRu3ToFBgZe1jaXLFmirKwsvf/++9VdLoDLVKemCwBwdXr99dd15513uszbtm2bGjVqdNnBD+DqwrA/ALd8+umnSkxMVFFRkdq1a6ekpCRJ0hdffKEhQ4aoY8eO6tu3r7Zs2eJc5/e//72ysrK0d+9eTZ06VV988YXatWvn/J32srIyTZo0SV26dFHPnj2VkZHh/Cng//znP3rooYfUoUMHde7cWU888YT3dxqopTjyB+CWO++8U/PmzdPEiRO1YcMGSVJhYaFGjx6tmTNnqlu3bvrss880fvx4rVq1SgEBAc51W7VqpdTU1ErD/s8995zKysqUm5ur0tJSPfLIIwoKCtKgQYOUnp6url27KjMzU6dPn9bOnTu9vs9AbcWRP4ALGjdunDp27Oj898EHH1Rqs3z5cnXv3l09evSQxWJR165d1aZNG33yySeX3L7dbldOTo6efPJJ+fn5qWnTpho+fLg+/PBDSVKdOnWUn5+voqIi1atXjztMAtWII38AF/Tqq69WOud//pC+JOXn52v16tVat26dc96ZM2fUuXPnS27/yJEjOn36tMLCwpzzwsLCVFhYKEmaOHGi0tPTdf/996thw4YaPny47r///l+ySwD+P8IfwBWz2WyKj4/XX/7yl0u29fHxcXncuHFj+fr6Kj8/XzfffLMkqaCgwHlf9qCgIOd2t23bpuHDh6tTp0666aabqnkvAPMw7A/givXt21fr1q3Txo0bZbfbdfLkSW3ZskWHDh2q1DYwMFCFhYU6deqUJMlqtSomJkazZ89WeXm5Dh48qAULFqhv376SpFWrVjm307BhQ/n4+HAbYKCacOQP4ILGjBnj8j3/O++8U8OGDXNpY7PZlJGRoVmzZunJJ5+UxWJR27ZtlZKSUml7Xbp00c0336y77rpLPj4+2rJli/785z/rueeeU3R0tOrVq6dBgwZp4MCBkqSdO3fq+eefV3l5uQIDA7knO1CN+JEfAAAMwxgaAACGIfwBADAM4Q8AgGEIfwAADEP4AwBgGMIfAADDEP4AABiG8AcAwDCEPwAAhvl/KCuTjTQqUm4AAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 576x648 with 1 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a86r0uJyjc6d"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}