from abc import ABC, abstractmethod
from typing import List

from src.contas_contabeis_updater.domain.entities.conta_contabil import ContaContabil

class ContaContabilRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ContaContabil]:
        pass
    @abstractmethod
    def atualiza_status(self, conta_id: int, status: str) -> None:
        pass