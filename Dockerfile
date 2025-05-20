FROM mambaorg/micromamba:latest

WORKDIR /home

COPY src src
COPY capitais_2024 capitais_2024
COPY requirements.yaml .

VOLUME ["/home/dados"]

USER root

RUN chmod +x /home/ana/executa_container.sh
RUN micromamba env create -f requirements.yaml && micromamba clean --all --yes
RUN echo "micromamba activate tria-etl" >> ~/.bashrc

CMD ["./ana/executa_container.sh"]