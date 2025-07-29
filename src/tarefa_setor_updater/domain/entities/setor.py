
from dataclasses import dataclass
from .assunto import Assunto


@dataclass(slots=True)
class Setor:
    id: int
    nome: str
    ativo: str