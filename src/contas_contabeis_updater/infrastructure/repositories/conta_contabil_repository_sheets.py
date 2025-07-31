from typing import List
from src.contas_contabeis_updater.domain.repositories.conta_contabil_repository import ContaContabilRepository
from src.contas_contabeis_updater.domain.entities.conta_contabil import ContaContabil
from src.shared.infrastructure.repositories.google_sheets_repository import GoogleSheetsRepository


class ContaContabilRepositorySheets(GoogleSheetsRepository, ContaContabilRepository):
    def __init__(self, spreadsheet_url):
        super().__init__(spreadsheet_url=spreadsheet_url)
        
    def get_all(self):
        contas_contabeis: List[ContaContabil] = []
        rows = self.ws.get_all_values()[1:]
        
        for row in rows:
            conta_contabil = ContaContabil(
                id=int(row[self.col_indices['id'] -1]),
                desc=str(row[self.col_indices['desc'] -1]),
                deve_star=str(row[self.col_indices['deve_estar'] -1])
            )
            contas_contabeis.append(conta_contabil)
        return contas_contabeis
        ...
        
    def atualiza_status(self, conta_id: int, status: str) -> None:
        pass