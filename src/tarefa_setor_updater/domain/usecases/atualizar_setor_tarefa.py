from src.tarefa_setor_updater.domain.entities.setor import Setor
from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa
from src.tarefa_setor_updater.domain.repositories.tarefa_repository import TarefaRepository


class AtualizarTarefaSetorUseCase:
    def __init__(self, tarefa_repo: TarefaRepository):
        self.tarefa_repo = tarefa_repo
    
    def __call__(self, novo_setor: Setor):
        processos = self.tarefa_repo.get_all()
        
        for processo in processos:
            if processo.tarefa.setor.id != novo_setor:
                print(f"[INFO] Atualizando tarefa {processo.tarefa.id} do processo {processo.descricao}[{processo.id}] do setor {processo.tarefa.setor.nome}[{processo.tarefa.setor.id}] para {novo_setor.nome}[{novo_setor.id}]")
                self.tarefa_repo.atualizar_setor(tarefa_id=processo.tarefa.id, novo_setor_id=novo_setor.id)