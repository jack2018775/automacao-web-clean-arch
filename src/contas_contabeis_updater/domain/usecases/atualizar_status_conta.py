from src.contas_contabeis_updater.domain.repositories.conta_contabil_repository import ContaContabilRepository
from src.contas_contabeis_updater.domain.usecases.filtrar_conta_contabil import FiltrarContaContabilUseCase
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
            print(f"[INFO] Verificando conta {conta.desc} ({conta.id})")
            
            filtrar_conta_contabil_analitica = FiltrarContaContabilUseCase(self.web_automation)
            filtrar_conta_contabil_analitica(conta.id)
                        
            if conta.deve_star.lower() == 'ativo':
                selector = 'form[name="planejamento_analitico"] input[id="ativoS"]'
            elif conta.deve_star.lower() == 'inativo':
                selector = 'form[name="planejamento_analitico"] input[id="ativoN"]'
            else:
                raise ValueError("Status inválido. Use 'Ativo' ou 'Inativo'.")
            
            # 1️⃣ Selecionar o status
            self.web_automation.click(selector)

            # 2️⃣ Confirmar a alteração no formulário
            self.web_automation.click('form[name="planejamento_analitico"] button[title="Alt+S"]')