# src/tarefa_setor_updater/presentation/cli/main.py
from sys import path

path.append('A:\\dev\\python\\automacao-web-clean-arch')
from src.tarefa_setor_updater.domain.entities.setor import Setor
from src.tarefa_setor_updater.infrastructure.repositories.tarefa_repository_sheets import TarefaRepositorySheets
from src.tarefa_setor_updater.domain.usecases.atualizar_setor_tarefa import AtualizarTarefaSetorUseCase


def main():
    repo = TarefaRepositorySheets(
        creds_json_path='src/shared/infrastructure/creds/service-account.json',
        spreadsheet_name='os_aberta',
        spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1rAXHK7e0nIZkdXNMNMEpF7RKcV_9-qg0nn0W35WgQso/edit?usp=sharing'
    )

    usecase = AtualizarTarefaSetorUseCase(repo)
    usecase.execute(Setor(id=200, nome='CAC'))

if __name__ == '__main__':
    main()
