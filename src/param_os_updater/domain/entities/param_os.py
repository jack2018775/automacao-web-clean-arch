from src.tarefa_setor_updater.domain.entities.setor import Setor
from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class ParamOS:
    id: int
    desc: Optional[str] = None
    setor: Optional[Setor] = None
    ativo: Optional[str] = None