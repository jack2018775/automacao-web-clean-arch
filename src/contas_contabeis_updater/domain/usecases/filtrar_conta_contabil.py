from src.shared.domain.repositories.web_autimation import WebAutomation


class FiltrarContaContabilUseCase:
    def __init__(self, web_automation: WebAutomation):
        self.web_automation = web_automation
        
    def __call__(self, conta_id):
         # Clicar na seleção de campo do filtro
        self.web_automation.click('span[class="selectedColumn"]')

        # Selecionar o campo "ID"
        self.web_automation.click('li[data-valor="planejamento_analitico.id"]')

        # Digitar o ID desejado e pressionar Enter
        self.web_automation.send_keys(
            'input[class="gridActionsSearchInput"]',
            str(conta_id),
            press_enter=True
        )
        
        # Entrar em detalhes da conta contábil
        self.web_automation.duble_click(f'tr[id="row{str(conta_id)}"]')