from src.shared.domain.repositories.web_autimation import WebAutomation
import time


class FiltrarProcessoUseCase:
    def __init__(self, web_automation: WebAutomation):
        self.web_automation = web_automation

    def __call__(self, processo_id: int, col_name: str = 'ID'):
        # 1. Clicar na seleção de campo do filtro
        filtro_selecionado = self.web_automation.get_text('span[class="selectedColumn"]')

        if col_name == 'ID' and filtro_selecionado != col_name:
            # 2. Selecionar "id" como coluna
            self.web_automation.click('span[class="selectedColumn"]')
            if self.web_automation.element_exists('li[data-valor="wfl_processo.id"]'):
                self.web_automation.click('li[data-valor="wfl_processo.id"]')
            else:
                time.sleep(1)
                self.web_automation.click('li[data-valor="wfl_processo.id"]')

        # Escrever o ID e pressionar Enter
        self.web_automation.send_keys('input[class="gridActionsSearchInput"]', str(processo_id), press_enter=True)
        
        # Entra na janela de detalhes do processo
        self.web_automation.duble_click(f'table[data-nome="wfl_processo"] tr[id="row{processo_id}"]')
