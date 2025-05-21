# TRIA-ETL

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")
![texto](https://img.shields.io/static/v1?label=ambiente&message=docker&color=blue&style=flat-square "linguagem")

Pipeline ETL de dados de chuva horária em acumulado diário.


## :world_map: Conteúdo
1. [O que faz](#sparkles-o-que-faz)  
2. [Quais tecnologias posso usar](#arrow_forward-quais-tecnologias-posso-usar) 
3. [Mamba-Conda](#snake-mamba-conda)
4. [Docker](#whale-docker)

## :sparkles: O que faz?

:heavy_check_mark: Busca os dados dos pluviômetros da ANA a partir do contorno das capitais do Brasil.

:heavy_check_mark: O usuário escolhe o período de busca (ex: 01/01/2019 à 31/12/2019).

:heavy_check_mark: Os dados horários são transformados em diários.

:heavy_check_mark: Os dados serão salvos no formato CSV na pasta ``dados``. Caso o usuário queira trabalhar com os dados em um excel.

:heavy_check_mark: Os dados serão inseridos em um banco de dados MongoDB.

## :warning: Quais tecnologias posso usar?

Há duas maneiras de executar este repositório, utilizando conda/mamba ou docker.

- [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
- [Docker](https://docs.docker.com/engine/install/)

Execute o comando abaixo para clonar o repositório:

```bash  
git clone https://github.com/Rodrigo-Caldas/TRIA-ETL.git
```

## :snake: Mamba/Conda

Para rodar a aplicação utilizando Mamba ou Conda crie o ambiente no terminal:

```bash 
mamba env create -f requirements.yaml
```
 ou 
```bash 
conda env create -f requirements.yaml
```

Ative o ambiente criado:

```bash
mamba activate tria-etl
```

Para testar a aplicação execute no terminal:

```bash
python -m src
```

## :whale: Docker

Para rodar a aplicação em um container, construa a imagem da aplicação a partir do comando:

```bash
docker build . -t tria-etl
```

Com a imagem criada, podemos criar o container onde a aplicação será rodada a partir do comando:

```bash
docker run -v /caminho/da/pasta/dados/local:/home/dados -it tria-etl
```