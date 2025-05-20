"""Configurações do serviço ana."""

import asyncio
from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from src.logit import log


class DOCDB(BaseSettings):
    """Classe para conexão com o banco de dados."""

    usuario: str = "rodrigocaldas"
    senha: str = "endurance"
    endereco: str = "meteorologia.ielpsol.mongodb.net"

    @property
    def uri(self) -> str:
        """Monta a uri de conexão"""
        return f"mongodb+srv://{self.usuario}:{self.senha}@{self.endereco}/?retryWrites=true&w=majority&appName=meteorologia"

    @property
    def conexao(self) -> MongoClient:
        """Conexão com banco MongoDB."""
        client = MongoClient(self.uri, server_api=ServerApi("1"))

        try:
            client.admin.command("ping")
            log.info(
                "[brigth_green]Pinged your deployment. You successfully connected to MongoDB!"
            )
            return client

        except Exception as e:
            log.error(f"[bright_red]Falha na conexão com o banco: {e}")
            raise e


class Configuracoes(BaseSettings):
    """Configurações e parâmetros do serviço."""

    url_base: str = "http://telemetriaws1.ana.gov.br/ServiceANA.asmx"
    lista_ana: List[str] = [
        "Latitude",
        "Longitude",
        "Altitude",
        "Codigo",
        "Nome",
        "BaciaCodigo",
        "SubBaciaCodigo",
        "nmEstado",
        "TipoEstacao",
        "TipoEstacaoTelemetrica",
        "Operando",
    ]
    limitador_tarefas: asyncio.Semaphore = asyncio.Semaphore(7)
    diretorio_dados: Path = Path("dados")
    docdb: DOCDB = DOCDB()


config = Configuracoes()
config.diretorio_dados.mkdir(parents=True, exist_ok=True)
