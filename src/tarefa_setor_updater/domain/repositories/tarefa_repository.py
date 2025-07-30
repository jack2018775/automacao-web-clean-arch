# src/tarefa_setor_updater/domain/repositories/tarefa_repository.py
from abc import ABC, abstractmethod
from typing import List
from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa

class TarefaRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Tarefa]:
        pass

    # @abstractmethod
    # def atualizar_setor(self, tarefa_id: int, novo_setor_id: int) -> None:
    #     pass
