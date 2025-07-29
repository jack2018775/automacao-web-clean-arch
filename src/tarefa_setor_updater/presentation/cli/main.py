# src/tarefa_setor_updater/presentation/cli/main.py
from sys import path

path.append('A:\\dev\\python\\automacao-web-clean-arch')

from src.tarefa_setor_updater.domain.usecases.filtrar_processo import FiltrarProcessoUseCase
from src.tarefa_setor_updater.domain.usecases.abrir_listagem_processo import AbrirListagemProcessoUseCase
from src.tarefa_setor_updater.domain.entities.user import User
from src.shared.domain.usecases.login_use_case import LoginUseCase
from src.shared.infrastructure.repositories.playwright_webdriver import PlaywrightWebAutomation
from src.tarefa_setor_updater.domain.entities.setor import Setor
from src.tarefa_setor_updater.infrastructure.repositories.tarefa_repository_sheets import TarefaRepositorySheets
from src.tarefa_setor_updater.domain.usecases.atualizar_setor_tarefa import AtualizarTarefaSetorUseCase

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
from os import getenv


def main():
    with sync_playwright() as pw:
        web_automation= PlaywrightWebAutomation.create(pw, headless=False)
        user = User(
            getenv('EMAIL_3'),
            getenv('PASSWORD_3'),
        )
        repo = TarefaRepositorySheets(
            creds_json_path='src/shared/infrastructure/creds/service-account.json',
            spreadsheet_name='os_aberta',
            spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1rAXHK7e0nIZkdXNMNMEpF7RKcV_9-qg0nn0W35WgQso/edit?usp=sharing'
        )

        
        # 🔐 Etapa 1: Login
        login = LoginUseCase(web_automation, getenv('LOGIN_URL'), user)
        login()
        
        # 📂 Etapa 2: Acessar Processos
        abrir_listagem_processo = AbrirListagemProcessoUseCase(web_automation)
        abrir_listagem_processo()
        
        # 3. Atualizar o setor das tarefas dos processos
        atualizar_setor_da_tarefa = AtualizarTarefaSetorUseCase(repo, web_automation)
        atualizar_setor_da_tarefa(Setor(id=200, nome='CAC'))

if __name__ == '__main__':
    main()
