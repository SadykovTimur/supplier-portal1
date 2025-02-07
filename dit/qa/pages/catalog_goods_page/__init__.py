from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.menu import Menu

__all__ = ['CatalogGoodsPage']


class CatalogGoodsPage(Page):
    menu = Menu(css='[class*="TopMenuWrapper"]')
    footer = Component(css='[class*="Footer"]')
    catalog_search = Text(css='[class*="TitleWithDropdown"]')
    production = Components(css='[class*="CatalogProductionItemLayout"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible

                assert 'Каталог товаров' == self.catalog_search
                assert self.production[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Страница каталога не загружена')
        self.app.restore_implicitly_wait()
