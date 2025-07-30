from src.shared.domain.repositories.web_autimation import WebAutomation
from src.tarefa_setor_updater.domain.entities.processo import Processo
from src.tarefa_setor_updater.domain.entities.setor import Setor
from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa
from src.tarefa_setor_updater.domain.repositories.tarefa_repository import TarefaRepository
from src.tarefa_setor_updater.domain.usecases.filtrar_processo import FiltrarProcessoUseCase

import re
import time



class AtualizarTarefaSetorUseCase:
    def __init__(self, tarefa_repo: TarefaRepository, web_automation: WebAutomation):
        self.tarefa_repo = tarefa_repo
        self.web_automation = web_automation
    
    def __call__(self, novo_setor: Setor):
        processos = self.tarefa_repo.get_all()
        
        for processo in processos:
            processo: Processo
            if processo.tarefa.setor.id != novo_setor.id:
                print(f"[INFO] Atualizando tarefa {processo.tarefa.id} do processo {processo.descricao}[{processo.id}] do setor {processo.tarefa.setor.nome}[{processo.tarefa.setor.id}] para {novo_setor.nome}[{novo_setor.id}]")
                
                # Limpa o Filtro
                if self.web_automation.element_exists('div[class="searchTags"] i[class="fa fa-times"]'):
                    self.web_automation.click('div[class="searchTags"] i[class="fa fa-times"]')
                
                # 🔎 : Filtrar Processo pelo ID
                filtra_processo = FiltrarProcessoUseCase(self.web_automation)
                filtra_processo(processo.id)
                # self.tarefa_repo.atualizar_setor(tarefa_id=processo.tarefa.id, novo_setor_id=novo_setor.id)
                
                #✅ : Acessar a Aba de Tarefas
                self.web_automation.click('a[rel="2"]')
                
                #📝 : Alterar o Setor da Tarefa
                # Clicar na aba de tarefas
                # self.web_automation.duble_click(f'tr[id="row{processo.tarefa.id}"]')
                self._procura_tarefa_pagination(processo.tarefa)
                
                try:
                    # Digitar o ID do novo setor
                    self.web_automation.send_keys('input[id="id_setor"]', str(novo_setor.id), press_tab=True, timeout=3)
                    # self.web_automation.click(f'div[id="id_setor_label-autocomplete-list"] div[data-id="{novo_setor.id}"]')
                except Exception as e:
                    input("Deu erro deseja continuar ?")
                
                # Salvar a alteração
                self.web_automation.click('form[name="wfl_tarefa"] button[title="Alt+S"]', sleep=2)
                
                # Fechar a janela de tarefa e do processo
                self.web_automation.click('a[id="wfl_tarefa_btn_close"]')
                time.sleep(1)
                self.web_automation.click(f'a[id="wfl_processo_btn_close"]')
                
            else:
                continue
            
    def _procura_tarefa_pagination(self, tarefa: Tarefa):
        tarefa_row_selector = f'tr[id="row{tarefa.id}"]'
        
        while True:
            time.sleep(1)
            if self.web_automation.element_exists(tarefa_row_selector):
                self.web_automation.duble_click(tarefa_row_selector)
                return True
            
            # Verifica se há próxima página
            paginator_text = self.web_automation.get_text('form[name="wfl_processo"] span[class="pPageStat"]')
            match_re = re.search(r'(\d+) \- (\d+) \/ (\d+)', paginator_text)
            
            if not match_re:
                print("[WARN] Não foi possível interpretar o texto da paginação.")
                return False
            
            _, ultimo_item, total = map(int, match_re.groups())
            
            if ultimo_item < total:
                self.web_automation.click('form[name="wfl_processo"] i.fa-forward', sleep=1)
                