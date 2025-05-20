"""Módulo principal da aplicação src."""

import asyncio
from pathlib import Path

import geopandas as gpd

from src import ana, utils
from src.config import config
from src.logit import console


async def handler(
    data_inicio: str = "01-01-2025",
    data_fim: str = "",
    caminho_contorno: Path = Path("capitais_2024", "capitais.shp"),
) -> None:
    """
    Execução do serviço de coleta da chuva diária dos postos em operação da ANA.

    Parameters
    ----------
    data_inicio : str, optional
        Data de início da requisição dos dados, by default '01-01-2025'.
    data_fim : str, optional
        Data final da requisição dos dados, by default "".
    caminho_contorno : Path, optional
        Caminho do shapefile ou do diretório contendo shapefiles, by default Path("BR_Municipios_2024").
    """
    console.rule("Iniciando serviço de coleta de chuva diária da ANA.")

    df_inventario = ana.mostrar_inventario()

    gdf_capitais = gpd.read_file(caminho_contorno)

    for linha in range(len(gdf_capitais)):
        linha_df = gdf_capitais.iloc[[linha]]
        capital = linha_df.iloc[0]["NM_MUN"]
        console.rule(f"Obtendo dados de {capital}")

        caminho_csv = Path(config.diretorio_dados, capital)
        caminho_csv.mkdir(parents=True, exist_ok=True)

        gdf_inventario_filtrado = utils.filtrar_postos_da_bacia(df_inventario, linha_df)

        lista_codigo = gdf_inventario_filtrado["codigo"].tolist()

        await ana.obter_chuvas(lista_codigo, caminho_csv, data_inicio, data_fim)

    console.rule("Fim do serviço!")


if __name__ == "__main__":

    asyncio.run(handler())
