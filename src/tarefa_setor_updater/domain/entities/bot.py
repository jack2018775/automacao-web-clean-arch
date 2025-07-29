#src\domain\entities\tarefa.py
from dataclasses import dataclass
from .assunto import Assunto


@dataclass(slots=True)
class Bot:
    action: str
    status: str