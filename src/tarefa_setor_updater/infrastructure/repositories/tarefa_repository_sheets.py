import gspread
from oauth2client.service_account import ServiceAccountCredentials
from typing import List, Optional
import time

import os
import sys

from src.param_os_updater.domain.entities.param_os import ParamOS
from src.shared.infrastructure.repositories.google_sheets_repository import GoogleSheetsRepository
from src.tarefa_setor_updater.domain.entities.processo import Processo
sys.path.append('d:\\jackson\\dev\\python\\automacao')

from src.tarefa_setor_updater.domain.entities.assunto import Assunto
from src.tarefa_setor_updater.domain.entities.setor import Setor
from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa
from src.shared.domain.repositories.web_autimation import WebAutomation
from src.tarefa_setor_updater.domain.repositories.tarefa_repository import TarefaRepository



class TarefaRepositorySheets(GoogleSheetsRepository, TarefaRepository):
    """
    Implementação de OsRepository usando Google Sheets.
    Atualizações são refletidas em tempo real no navegador.
    Requer um Service Account JSON com acesso ao Google Sheets.
    """
    def __init__(
        self,
        web_automation: Optional[WebAutomation] = None,
        spreadsheet_url: str = 'https://docs.google.com/spreadsheets/d/1rAXHK7e0nIZkdXNMNMEpF7RKcV_9-qg0nn0W35WgQso/edit?gid=0#gid=0'
    ):
        super().__init__(spreadsheet_url=spreadsheet_url)
        self.web_automation = web_automation
        
    
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
    

    def get_all_param_os(self) -> List[ParamOS]:
        param_os_list: List[ParamOS] = []
        
        rows = self.ws.get_all_values()[1:]
        
        for row in rows:
            param_os = ParamOS(
                int(row[self.col_indices['id_wfl_param_os'] - 1]),
                'DESC ALEATORIA',
                Setor(10, 'DESC ALEATORIA')
            )
            param_os_list.append(param_os)
            
        return param_os_list

    def atualizar_coluna_por_tarefa_id(self, tarefa_id: int, nome_coluna: str, valor: str) -> None:
        """Atualiza o valor de uma celular especifica na linha da tabela informada pelo ID

        Args:
            tarefa_id (int): ID da tarefa que foi atualizado no sistema
            nome_coluna (str): Qual a coluna que vc que editar
            valor (str): O valor que irá para a celular
        """
        col_index = self.colunas.get(nome_coluna)
        if col_index is None:
            raise ValueError(f'Coluna {nome_coluna} não está definida em {self.colunas}')
        
        # for row_idx, row in enumerate(self.sheet)

        

    def close(self):
        # Não há instâncias COM para fechar, mas podemos desvincular ws se desejado
        del self.ws

if __name__ == '__main__':

    # Exemplo de uso
    repo = TarefaRepositorySheets(
        creds_json_path='src/infrastructure/creds/service-account.json',
        spreadsheet_name='os_aberta',
    )
    tarefa_list = repo.get_all()
    print(tarefa_list)