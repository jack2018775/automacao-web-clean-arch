from dataclasses import dataclass
from typing import Optional

@dataclass
class Assunto:
    id: int
    descricao: str
    ativo: Optional[bool] = None