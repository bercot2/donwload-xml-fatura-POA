import os
import shutil
from datetime import datetime

from enviroments import DIRECTORY_XML


def prepare_enviroment():
    # 1. Verifica se há arquivos .pdf na pasta
    arquivos_pdf = [f for f in os.listdir(DIRECTORY_XML) if f.lower().endswith(".pdf")]

    # 2. Cria a pasta com base em ano-mês atual
    data_agora = datetime.now()
    nome_pasta = f"{data_agora.year}-{data_agora.month:02d}"
    caminho_final = os.path.join(DIRECTORY_XML, nome_pasta)

    os.makedirs(caminho_final, exist_ok=True)

    # 3. Move todos os PDFs para essa pasta
    for pdf in arquivos_pdf:
        origem = os.path.join(DIRECTORY_XML, pdf)
        destino = os.path.join(caminho_final, pdf)
        shutil.move(origem, destino)

    # 4. Retorna o caminho da nova pasta criada
    return caminho_final
