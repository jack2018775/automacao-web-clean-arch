# src/tarefa_setor_updater/domain/repositories/tarefa_repository.py
from abc import ABC, abstractmethod
from typing import List
from src.param_os_updater.domain.entities.param_os import ParamOS
from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa

class TarefaRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Tarefa]:
        pass

    @abstractmethod
    def get_all_param_os(self) -> List[ParamOS]:
        pass