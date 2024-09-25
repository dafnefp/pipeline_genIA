<h3 align="center"> 
	🚧  Projeto em construção... 🚀 🚧
</h3><br>

<p align="center">
 <a href="#introdução">Introdução</a> •
  <a href="#objetivo">Objetivo</a> • 
  <a href="#dados">Dados</a> • 
 <a href="#autor">Autor</a>
</p>

<h1 align="center">Webscraping e Inteligencia Artificial</h1>

## Introdução

Quem nunca ouviu falar em inteligência artificial generativa, ou então Gen AI? É a tecnologia hype do momento, mas calma, se você não conhece esses termos, tenho certeza que você conhece o ChatGPT.

As inteligências artificiais generativas têm a capacidade de criar novas informações, como audio, código, texto, imagem e videos, em resposta a uma pergunta feita pelo usuário. Com base em foundation models ou modelo de base (grandes redes neurais de aprendizado profundo), elas identificam e codificam os padrões e identificam os relacionamentos em uma grande quantidade de dados e, em seguida, usam essas informações para entender as solicitações ou perguntas de linguagem natural dos usuários, respondendo com novo conteúdo relevante.

Focando na geração de texto, temos as famosas LLM's (large language model), que é um tipo de modelo de linguagem que utiliza algoritmos avançados de processamento de linguagem natural (NLP), para entender e gerar texto. Sua arquitetura é baseada em um componente específico, chamado Transformer AI.

Esses transformadores processam enormes volumes de textos, identificando as maneiras como as palavras se relacionam e construindo um modelo que permita a reprodução de textos semelhantes, sendo possivel prever palavras ou frases seguintes de acordo com a anterior.

A imagem abaixo mostra que GenAi e LLM são subconjuntos da inteligencia artificial.

![Imagem](https://www.researchgate.net/publication/378394229/figure/fig1/AS:11431281225168931@1708621228583/LLMs-within-the-AI-taxonomy-LLMs-exist-as-a-subset-of-deep-learning-models-which-are-a.tif)

Alguns exemplos de aplicação de LLM:
- Geração de texto
- Tradução automática
- Assistentes virtuais
- Análise de sentimentos
- Recomendação de conteúdo

## Objetivo

Ao participar da série **Pipeline Gen AI - ETL com API e CRM de vendas: Python, SQL, OpenAI, Langchain e Git** de 3 aulas ao vivo do canal [Jormada de dados](https://www.youtube.com/@JornadaDeDados) do [Luciano Vasconcelos](https://www.linkedin.com/in/lucianovasconcelosf/), tive algumas ideias de projeto para construção.

Dessa maneira, meu objetivo é utilizar o streamlit como um frontend, onde o usuário ao abrir a página teria uma lista de ações com as maiores altas e baixas do dia, extraída a partir de um webscraping do site da [InfoMoney](https://www.infomoney.com.br/ferramentas/altas-e-baixas/). 

Ao selecionar a ação desejada e informar um período para obtenção dos dados, outro webscraping seria realizado para obtenção desses dados referentes as informações selecionadas.

Após essa extração, o usuário teria a possibilidade de perguntar qualquer informação em relação aos dados, que uma inteligencia artificial iria responde-lo.

## Dados

Os dados extraídos no segundo webscraping realizado pela aplicação e que são insumos para a inteligencia artificial responder a pergunta são:

- DATA: dia 
- ABERTURA: valores de abertura
- FECHAMENTO: valores de fechamento
- VARIAÇÃO: variação em percentual do fechamento de um dia em comparação com o anterior 
- MÍNIMO: valor minimo 
- MÁXIMO: maximo atingido
- VOLUME: volume de ações negociadas no dia

## Autor

Feito por Dafne Piovesan.

[![Linkedin Badge](https://img.shields.io/badge/-Dafne-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/dafnefp/)](https://www.linkedin.com/in/dafnefp/) 
[![Email Badge](https://img.shields.io/badge/-dafnefp@uol.com.br-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dafnefp@uol.com.br)](mailto:dafnefp@uol.com.br)
