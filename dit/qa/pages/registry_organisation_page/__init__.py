from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.menu import Menu

__all__ = ['RegistryOrganisationPage']


class RegistryOrganisationPage(Page):
    menu = Menu(css='[class*="TopMenuWrapper"]')
    footer = Component(css='[class*="Footer"]')
    title = Component(xpath="//h1[text()='Реестр организаций']")
    container = Component(css='[class*="fresnel-container"] ')
    card_list = Components(css='[class*="PublicList"] [class*="InfoName"]')
    organisation = Component(xpath="//span[text()='Все организации']")

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
                assert self.organisation.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Страница реестра организаций не загружена')
        self.app.restore_implicitly_wait()
