# src/tarefa_setor_updater/presentation/cli/main.py
from sys import path

path.append('A:\\dev\\python\\automacao-web-clean-arch')

from src.contas_contabeis_updater.domain.usecases.abrir_listagem_contas_analiticas import AbrirListagemContasAnaliticasUseCase
from src.tarefa_setor_updater.domain.entities.user import User
from src.shared.domain.usecases.login_use_case import LoginUseCase
from src.shared.infrastructure.repositories.playwright_webdriver import PlaywrightWebAutomation
from src.contas_contabeis_updater.infrastructure.repositories.conta_contabil_repository_sheets import ContaContabilRepositorySheets
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
        repo = ContaContabilRepositorySheets(
            spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1eX3iOACNQ5a31YrNp0njuhw7wMcrckXp1uBDIM8sGAk/edit?usp=sharing'
        )

        
        # 🔐 Etapa 1: Login
        login = LoginUseCase(web_automation, getenv('LOGIN_URL'), user)
        login()
        
        # Acessar listagem de contas contábeis analíticas
        abrir_listagem = AbrirListagemContasAnaliticasUseCase(web_automation)
        abrir_listagem()
        
        atualizar_status_contabil = AtualizarStatusContabilUseCase(repo, web_automation)
        atualizar_status_contabil()
        
        

if __name__ == '__main__':
    main()
