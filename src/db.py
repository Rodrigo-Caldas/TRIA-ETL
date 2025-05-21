"""Módulo para lidar com banco de dados."""

from datetime import datetime

from dateutil.parser import parse

from src.config import config
from src.esquemas import Capital
from src.logit import log


def persistir(documento: Capital) -> None:
    """
    Persistir um item no banco de dados.

    Parameters
    ----------
    documentos : Capital
        Item a ser persistido.
    """
    try:
        banco = config.docdb.conexao.meteorologia
        nome_colecao = "chuva.diária.ana"
        colecao = banco[nome_colecao]

        capital = documento.capital
        novo_codigo = documento.codigos[0]

        doc_capital = colecao.find_one({"capital": capital})

        if not doc_capital:
            colecao.insert_one(documento.model_dump())
            log.info(
                "[bright_green]Capital não existia. Documento inserido por completo!"
            )
            return

        # Capital existe: verificar se código existe
        resultado = colecao.find_one(
            {"capital": capital, "codigos.codigo": novo_codigo.codigo}, {"codigos.$": 1}
        )

        datas_existentes = set()

        if resultado:
            valores = resultado["codigos"][0].get("valores", [])
            datas_existentes = {
                v["data"] if isinstance(v["data"], datetime) else parse(v["data"])
                for v in valores
            }

        # Filtra apenas os valores com datas novas
        novos_valores = [
            v.model_dump()
            for v in novo_codigo.valores
            if v.data not in datas_existentes
        ]

        if not resultado:
            colecao.update_one(
                {"capital": capital},
                {
                    "$push": {
                        "codigos": {
                            "codigo": novo_codigo.codigo,
                            "valores": [v.model_dump() for v in novo_codigo.valores],
                        }
                    }
                },
            )
            log.info(
                "[bright_green]Capital existia, mas o código era novo. Código adicionado por completo!"
            )

        elif novos_valores:
            colecao.update_one(
                {"capital": capital, "codigos.codigo": novo_codigo.codigo},
                {"$push": {"codigos.$.valores": {"$each": novos_valores}}},
            )
            log.info(
                "[bright_green]Capital e código encontrados. Novas datas adicionadas!"
            )

        else:
            log.info("[bright_green]Todos os dados já existem no banco. Nada inserido.")

    except Exception as e:
        log.error(f"[bright_red]Erro ao persistir dados: {e}")
        raise
