from src.shared.domain.repositories.web_autimation import WebAutomation

class AcessarAbaTarefasUseCase:
    def __init__(self, web_automation: WebAutomation):
        self.web_automation = web_automation

    def __call__(self):
        self.web_automation.click('a[rel="2"]')
