from dataclasses import dataclass

@dataclass
class Assunto:
    id: int
    descricao: str
    ativo: bool