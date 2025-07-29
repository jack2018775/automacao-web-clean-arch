#src\domain\entities\tarefa.py
from dataclasses import dataclass

from src.tarefa_setor_updater.domain.entities.tarefa import Tarefa
from .assunto import Assunto


@dataclass(slots=True)
class Processo:
    id: int
    descricao: str
    tarefa: Tarefa