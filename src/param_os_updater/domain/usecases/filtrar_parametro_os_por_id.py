from src.param_os_updater.domain.entities.param_os import ParamOS
from src.shared.domain.repositories.web_autimation import WebAutomation


class FiltrarParametroOSPorIDUseCase:
    def __init__(self, web_automation: WebAutomation):
        self.web_automation = web_automation

    def __call__(self, param_os_id: int):
        # Clicar na seleção de campo do filtro
        self.web_automation.click('span[class="selectedColumn"]')
        
        # Selecionar a coluna ID
        self.web_automation.click('li[data-nome="ID"]')
        
        # Digitar o ID desejado e pressionar Enter:
        self.web_automation.send_keys('input[class="gridActionsSearchInput"]', str(param_os_id), press_enter=True)
        
        # Duplo clique no sub-menu "Processo"
        self.web_automation.duble_click(f'tr[id="row{str(param_os_id)}"]')
        
        
        
        # Troca o setor para 200 - CAC
        self.web_automation.send_keys('input[id="id_setor"]', '200', press_tab=True)
        
        # Clica em salvar
        self.web_automation.click('form[name="wfl_parametro_oss"] button[title="Alt+S"]')
        
        # Fecha a janela
        self.web_automation.click('form[name="wfl_parametro_oss"] a[id="wfl_parametro_oss_btn_close"]')
        self.web_automation.click('div[class="searchTags"] i[class="fa fa-times"]')
