from src.shared.domain.repositories.web_autimation import WebAutomation


class AbrirListagemParamOSUseCase:
    def __init__(self, web_automation: WebAutomation):
        self.web_automation = web_automation

    def __call__(self):
        # Clicar no menu "Configurações"
        self.web_automation.click('a[title="Configurações"]')
        
        # Clicar no sub menu "Processos"
        self.web_automation.click('div[id="menua648352b6f304a5155942c5a60d1dc15"]')

        # Duplo clique no sub-menu "Processo"
        self.web_automation.duble_click("a[rel=\"cria_grid('#1_grid','wfl_parametro_oss','S');\"]")
