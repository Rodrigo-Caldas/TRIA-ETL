"""Módulo para lidar com banco de dados."""

from typing import List

from src.config import config
from src.esquemas import ColecaoDadosChuva
from src.logit import log


def persistir(documentos: List[ColecaoDadosChuva]) -> None:
    """
    Persistir um item no banco de dados.

    Parameters
    ----------
    documentos : List[ColecaoDadosBacia]
        Item a ser persistido.
    """
    try:
        banco = config.docdb.conexao.meteorologia
        nome_colecao = "chuva.diária.ana"
        colecao = banco[nome_colecao]

        for documento in documentos:
            dados = {"$set": documento}

            query = {"codigo": documento["codigo"], "data": documento["data"]}

            colecao.update_one(query, dados, upsert=True)

    except Exception as e:
        log.error(f"[bright_red]Falha no envio dos dados para o banco: {e}")
        raise e
