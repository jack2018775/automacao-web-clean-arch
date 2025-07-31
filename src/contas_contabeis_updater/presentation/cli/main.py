# src/tarefa_setor_updater/presentation/cli/main.py
from sys import path

path.append('A:\\dev\\python\\automacao-web-clean-arch')

from src.tarefa_setor_updater.domain.entities.user import User
from src.shared.domain.usecases.login_use_case import LoginUseCase
from src.shared.infrastructure.repositories.playwright_webdriver import PlaywrightWebAutomation
from src.tarefa_setor_updater.infrastructure.repositories.tarefa_repository_sheets import TarefaRepositorySheets
from src.contas_contabeis_updater.domain.usecases.atualizar_status_conta import AtualizarStatusContabilUseCase


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
            spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1rAXHK7e0nIZkdXNMNMEpF7RKcV_9-qg0nn0W35WgQso/edit?usp=sharing'
        )

        
        # 🔐 Etapa 1: Login
        login = LoginUseCase(web_automation, getenv('LOGIN_URL'), user)
        login()
        
        #
        
        

if __name__ == '__main__':
    main()
