from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.menu import Menu

__all__ = ['RegistryQuotationSessionsPage']


class RegistryQuotationSessionsPage(Page):
    menu = Menu(css='[class*="TopMenuWrapper"]')
    footer = Component(css='[class*="Footer"]')
    title = Text(tag='h1')
    container = Component(css='[class*="fresnel-container"]')
    card_list = Components(css='[class*="PublicList"] [class*="InfoName"]')
    quotation_session = Component(xpath="//span[text()='Котировочные сессии']")

    def choose_item(self) -> str:
        item = self.card_list[0]
        name = item.webelement.text

        item.wait_for_clickability()
        item.webelement.click()

        return name

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible

                assert self.title == 'Единый реестр закупок'
                assert self.container.visible
                assert self.card_list[0].visible
                assert self.quotation_session.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Страница реестра котировочных сессий не загружена')
        self.app.restore_implicitly_wait()
