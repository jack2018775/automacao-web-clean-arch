# src\domain\repositories\web_autimation.py
from abc import ABC, abstractmethod

# from .page import Page


class WebAutomation(ABC):
    @abstractmethod
    def goto_page(self, url: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def click(self, selector: str, timeout: int) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def duble_click(self, selector: str, timeout: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def send_keys(self, selector: str, text: str, timeout: int, press_enter: bool) -> None:
        raise NotImplementedError()

    @abstractmethod
    def wait_for_element(self, selector: str, timeout: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_text(self, selector) -> str:
        raise NotImplementedError()

    def element_exists(self, selector: str, timeout: int = 1) -> bool:
        raise NotImplementedError()

    # @abstractmethod
    # def get_curent_page(self) -> Page:
    #     raise NotImplementedError()

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

