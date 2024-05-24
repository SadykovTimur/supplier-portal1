from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.footer import Footer
from dit.qa.pages.components.menu import Menu

__all__ = ['ProductPage']


class ProductPage(Page):
    menu = Menu(css='[class*="TopMenuStyles"]')
    footer = Footer(css='[class*="Footer"]')
    title = Text(css='[class*="SkuTitle"]')
    subheader = Component(css='[class*="HeaderSubheader"]')

    def wait_for_loading(self, name: str) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible

                assert self.title == name

                return self.footer.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_id_cte(self) -> None:
        def condition() -> bool:
            try:
                assert self.subheader.visible

                return 'ID СТЕ' in self.subheader.webelement.text

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()