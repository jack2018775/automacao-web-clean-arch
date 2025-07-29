#src\domain\entities\tarefa.py
from dataclasses import dataclass

from src.tarefa_setor_updater.domain.entities.setor import Setor
from .assunto import Assunto


@dataclass(slots=True)
class Tarefa:
    id: int
    descricao: str
    pode_finalizar_processo: bool
    setor: Setor
    assunto: Assunto
    ativo: bool

    def __post_init__(self): # noqa
        self._valida_campos()

    def _valida_campos(self):
        if not isinstance(self.id, int):
            raise ValueError("O campo 'id' deve ser um número inteiro.")
        if not isinstance(self.descricao, str):
            raise ValueError("O campo 'descricao' deve ser uma string.")
        if not isinstance(self.pode_finalizar_processo, bool):
            raise ValueError("O campo 'pode_finalizar_processo' deve ser um booleano.")
        if not isinstance(self.ativo, bool):
            raise ValueError("O campo 'ativo' deve ser um booleano.")

        if not self.descricao.strip():
            raise ValueError("O campo 'descricao' não pode ser vazio.")




