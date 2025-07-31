
from abc import ABC
from typing import Optional

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from src.shared.domain.repositories.web_autimation import WebAutomation


class GoogleSheetsRepository(ABC):
    def __init__(
            self,
            spreadsheet_url: str,
            creds_json_path: str = 'src/shared/infrastructure/creds/service-account.json',
            worksheet_name: str = 'Página1',
        ):
            # Autenticação via Service Account
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive',
            ]
            
            # Tem que atualizar as creds
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