"""Registro Basemodel."""

from datetime import datetime
from typing import List

from pydantic import BaseModel


class ValorChuva(BaseModel):
    """
    Estrutura da chuva diária.

    Parameters
    ----------
    data : datetime
        Data da chuva.
    chuva : float
        Valor da chuva.
    """

    data: datetime
    chuva: float


class ColecaoEstacoesChuva(BaseModel):
    """
    Estruturação do código da estação e valores.

    Parameters
    ----------
    codigo: int
        Código da estação.
    valores: List[ValorChuva]
        Valores da data e chuva.
    """

    codigo: int
    valores: List[ValorChuva]


class Capital(BaseModel):
    """
    Estrutura de dados para capitais,

    Parameters
    ----------
    capital: str
        Capital.
    codigos: List[ColecaoEstacoesChuva]
        Códigos das estações.
    """

    capital: str
    codigos: List[ColecaoEstacoesChuva]
