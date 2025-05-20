"""Registro TypedDict."""

from typing import List
from typing import TypedDict

from pandas import Timestamp


class ValoresChuva(TypedDict):
    """Estrutura da chuva horária."""

    data: Timestamp
    chuva: float


class ColecaoDadosChuva(TypedDict):
    """Estruturação dos dados de chuva horária da ANA."""

    codigo: int
    valores: List[ValoresChuva]
