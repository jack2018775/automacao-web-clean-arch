# src\domain\use_cases\login_use_case.py
from src.tarefa_setor_updater.domain.entities.user import User
from src.shared.domain.repositories.web_autimation import WebAutomation
import time


class LoginUseCase:
    def __init__(self, web_automation: WebAutomation, url: str, user: User):
        self.web_automation = web_automation
        self.url = url
        self.email = user.email
        self.password = user.password

    def __call__(self):
        self.web_automation.goto_page(self.url)
        self.web_automation.send_keys('input[id="email"]', self.email)
        self.web_automation.click("#btn-next-login")
        self.web_automation.send_keys('input[id="password"]', self.password)
        
        max_attempts = 3
        attempts = 1
        
        while attempts <= max_attempts:
            print(f"Tentando logar {attempts} de {max_attempts}")
            
            if not self.web_automation.element_exists('#btn-enter-login'):
                print("Login inválido")
                break
            else:
                self.web_automation.click('#btn-enter-login')
                time.sleep(2)
                
            
            attempts += 1
        
        
        # return self.web_automation.get_curent_page()
