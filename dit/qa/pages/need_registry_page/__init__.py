from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.footer import Footer
from dit.qa.pages.components.menu import Menu

__all__ = ['NeedRegistryPage']


class NeedRegistryPage(Page):
    menu = Menu(css='[class*="TopMenuStyles"]')
    footer = Footer(css='[class*="Footer"]')
    title = Component(xpath="//h1[text()='Единый реестр закупок']")
    container = Component(css='[class*="fresnel-container"] ')
    card_list = Components(css='[class*="PublicList"] [class*="InfoName"]')
    need = Component(xpath="//span[text()='Закупки по потребностям']")

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

                assert self.title.visible
                assert self.container.visible
                assert self.card_list[0].visible
                assert self.need.visible

                return self.footer.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
