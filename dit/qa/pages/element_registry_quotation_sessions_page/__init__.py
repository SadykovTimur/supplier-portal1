from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.menu import Menu

__all__ = ['ElementRegistryQuotationSessionsPage']


class ElementRegistryQuotationSessionsPage(Page):
    menu = Menu(css='[class*="TopMenuWrapper"]')
    footer = Component(css='[class*="Footer"]')
    highlight_block = Component(css='[class*="HighlightBlockContainer"]')
    container = Component(css='[id*="left-column"] ')
    status = Text(css='[class*="StateIndicator"]')
    title = Text(css="[id*='main-info'] [class$='header']")

    def wait_for_loading(self, name: str) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible

                assert self.highlight_block.visible
                assert self.container.visible
                assert self.title == name

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Данные о КС не загружены')
        self.app.restore_implicitly_wait()

    def wait_for_loading_status(self) -> None:
        def condition() -> bool:
            try:
                return self.status in ['АКТИВНАЯ', 'СНЯТА С ПУБЛИКАЦИИ', 'ПРОВЕДЕНА', 'НЕ СОСТОЯЛАСЬ']

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Статусы котировочных сессий не загружены')
        self.app.restore_implicitly_wait()
