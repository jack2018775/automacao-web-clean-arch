from src.contas_contabeis_updater.domain.repositories.conta_contabil_repository import ContaContabilRepository
from src.shared.infrastructure.repositories.google_sheets_repository import GoogleSheetsRepository


class ContaContabilRepositorySheets(GoogleSheetsRepository, ContaContabilRepository):
    def __init__(self, spreadsheet_url):
        super().__init__(spreadsheet_url=spreadsheet_url)
        
    def get_all(self):
        rows = self.ws.get_all_values()[1:]
        ...