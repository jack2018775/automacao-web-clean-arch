from src.contas_contabeis_updater.domain.repositories.conta_contabil_repository import ContaContabilRepository
from src.shared.domain.repositories.web_autimation import WebAutomation
from src.contas_contabeis_updater.domain.entities.conta_contabil import ContaContabil


class AtualizarStatusContabilUseCase:
    def __init__(self, repo: ContaContabilRepository, web_automation: WebAutomation):
        self.repo = repo
        self.web_automation = web_automation
        
    def __call__(self, *args, **kwds):
        contas = self.repo.get_all()
        
        for conta in contas:
            conta: ContaContabil
            print(f"[INFO] Verificando conta {conta.descricao} ({conta.id})")
            ...
            