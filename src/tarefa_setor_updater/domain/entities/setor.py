
from dataclasses import dataclass
from typing import Optional
from .assunto import Assunto


@dataclass(slots=True)
class Setor:
    id: int
    nome: str
    ativo: Optional[str] = None