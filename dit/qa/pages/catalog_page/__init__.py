from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.footer import Footer
from dit.qa.pages.components.menu import Menu

__all__ = ['CatalogPage']


class CatalogPage(Page):
    menu = Menu(css='[class*="TopMenuStyles"]')
    footer = Footer(css='[class*="Footer"]')
    title = Component(xpath="//div[text()='Бумажная продукция']")
    catalog_block = Component(css='[class*="RightBlock"]')
    items = Components(css='[class*="MainInfoSmallNameHeader"]')

    def choose_item(self) -> str:
        item = self.items[0]
        name = item.webelement.text

        item.wait_for_clickability()
        item.webelement.click()

        return name

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible

                assert self.title.visible
                assert self.items[0].visible
                assert self.catalog_block.visible

                return self.footer.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
