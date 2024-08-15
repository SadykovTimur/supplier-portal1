from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.menu import Menu

__all__ = ['StartPage']


class StartPage(Page):
    menu = Menu(css='[class*="TopMenuWrapper"]')
    footer = Component(css='[class*="Footer"]')
    portal = Text(css='[class*="JumbotronHeader"]')
    modal = Button(xpath='//span[text()="Пройти опрос позже"] ')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible
                assert self.portal == 'ПОРТАЛ ПОСТАВЩИКОВ'

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Стартовая страница не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_after_auth(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.logo.visible
                assert self.menu.main.visible
                assert self.menu.user_name.visible

                assert self.portal == 'ПОРТАЛ ПОСТАВЩИКОВ'

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Главная страница не загружена')
        self.app.restore_implicitly_wait()
