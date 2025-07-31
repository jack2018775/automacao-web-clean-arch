from src.shared.domain.repositories.web_autimation import WebAutomation


class AbrirListagemContasAnaliticasUseCase:
    def __init__(self, web_automation: WebAutomation):
        self.web_automation = web_automation
        
    def __call__(self, *args, **kwds):
        # Clicar no menu "Contabilidade"
        self.web_automation.click('div[id="menu5f45d90b6928018b9dbea1365233ee96"]')
        
        # Clicar no menu "plano de contas"
        self.web_automation.click("a:has-text('Plano de contas')")

        # Clicar no submenu "Contas Contábeis Analíticas"
        self.web_automation.click("a[rel=\"cria_grid('#1_grid','planejamento_analitico','N');\"]")