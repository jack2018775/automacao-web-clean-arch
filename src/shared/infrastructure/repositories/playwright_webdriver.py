#src\infrastructure\playwright\playwright_webdriver.py
from playwright.sync_api import Page, Playwright

from src.shared.domain.repositories.web_autimation import WebAutomation
import time


class PlaywrightWebAutomation(WebAutomation):
    def __init__(self, page: Page, headless: bool = False):
        self.page = page
        self.headless = headless

    @classmethod
    def create(cls, playwright: Playwright, headless: bool = False) -> WebAutomation:
        browser = playwright.firefox.launch(headless=headless)
        page = browser.new_page()
        return cls(page, headless)

    def goto_page(self, url: str) -> None:
        self.page.goto(url)

    def click(self, selector: str, timeout: int = 3, sleep:float = 0.5) -> None:
        time.sleep(sleep)
        self.page.wait_for_selector(selector, timeout=timeout*1000)
        self.page.click(selector)

    def duble_click(self, selector: str, timeout: int = 2) -> None:
        self.page.wait_for_selector(selector, timeout=timeout*1000)
        self.page.dblclick(selector, delay=0.5)

    def send_keys(self, selector: str, text: str, timeout: int = 2, press_enter: bool = False, press_tab: bool = False) -> None:
        time.sleep(timeout)
        self.page.wait_for_selector(selector, timeout=timeout*1000)
        self.page.fill(selector, text)
        if press_enter:
            self.page.press(selector, "Enter")
        if press_tab:
            self.page.press(selector, 'Tab')

    def wait_for_element(self, selector: str, timeout: int = 2) -> None:
        
        self.page.wait_for_selector(selector, timeout=timeout*1000)

    def element_exists(self, selector: str, timeout: int = 2, sleep: int = 1) -> bool:
        time.sleep(sleep)
        return self.page.is_visible(selector, timeout=timeout*1000)

    def get_text(self, selector) -> str:
        return self.page.inner_text(selector)

    def close(self) -> None:
        self.page.close()
