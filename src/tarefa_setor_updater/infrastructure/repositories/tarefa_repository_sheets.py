import gspread
from oauth2client.service_account import ServiceAccountCredentials
from typing import List, Optional
import time

import os
import sys

from src.tarefa_setor_updater.domain.entities.processo import Processo
sys.path.append('d:\\jackson\\dev\\python\\automacao')

from src.tarefa_setor_updater.domain.entities.assunto import Assunto
from src.tarefa_setor_updater.domain.entities.setor import Setor
from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa
from src.shared.domain.repositories.web_autimation import WebAutomation
from src.tarefa_setor_updater.domain.repositories.tarefa_repository import TarefaRepository



class TarefaRepositorySheets(TarefaRepository):
    """
    Implementação de OsRepository usando Google Sheets.
    Atualizações são refletidas em tempo real no navegador.
    Requer um Service Account JSON com acesso ao Google Sheets.
    """
    def __init__(
        self,
        creds_json_path: str = 'src/infrastructure/creds/service-account.json',
        spreadsheet_name: str = 'setor_processo',
        worksheet_name: str = 'Página1',
        web_automation: Optional[WebAutomation] = None,
        spreadsheet_url: str = 'https://docs.google.com/spreadsheets/d/1rAXHK7e0nIZkdXNMNMEpF7RKcV_9-qg0nn0W35WgQso/edit?gid=0#gid=0'
    ):
        self.web_automation = web_automation
        # Autenticação via Service Account
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            creds_json_path,
            scope
        )
        client = gspread.authorize(creds)

        # Abre a planilha e seleciona a worksheet
        # sh = client.open(spreadsheet_name)
        sh = client.open_by_url(spreadsheet_url)
        self.ws = sh.worksheet(worksheet_name)

        # Lê os headers da primeira linha e cria mapeamento coluna -> índice (1-based)
        headers = self.ws.row_values(1)
        self.col_indices = {header: idx + 1 for idx, header in enumerate(headers)}
        
    
    def get_all(self) -> List[Tarefa]:
        processos: List[Processo] = []
        rows = self.ws.get_all_values()[1:]
        
        for row in rows:
            try:
                tarefa = Tarefa(
                    id=int(row[self.col_indices['tarefa_id'] - 1]),
                    descricao=str(row[self.col_indices['tarefa_descricao'] - 1]),
                    setor=Setor(
                        id=int(row[self.col_indices['setor_id'] - 1]),
                        nome=str(row[self.col_indices['setor'] - 1]),
                    ),
                    assunto=Assunto(
                        id=int(row[self.col_indices['assunto_id'] - 1]),
                        descricao=str(row[self.col_indices['assunto'] - 1]),
                    ),
                )
                processo = Processo(
                    id=int(row[self.col_indices['processo_id'] - 1]),
                    descricao=str(row[self.col_indices['processo_descricao'] - 1]),
                    tarefa=tarefa
                )
                processos.append(processo)
            except (KeyError, IndexError, ValueError) as e:
                print(f"[ERRO] Linha ignorada por dados inválidos: {row} -> {e}")
                continue
            
        return processos

    def atualizar_setor(self, tarefa_id: int, novo_setor_id: int) -> None:
        pass

        

    def close(self):
        # Não há instâncias COM para fechar, mas podemos desvincular ws se desejado
        del self.ws

if __name__ == '__main__':

    # Exemplo de uso
    repo = TarefaRepositorySheets(
        creds_json_path='src/infrastructure/creds/service-account.json',
        spreadsheet_name='os_aberta',
    )
    os_list = repo.get_all_os()
    print(os_list)