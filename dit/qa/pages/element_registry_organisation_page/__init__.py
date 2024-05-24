from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.footer import Footer
from dit.qa.pages.components.menu import Menu

__all__ = ['ElementRegistryOrganisationPage']


class ElementRegistryOrganisationPage(Page):
    menu = Menu(css='[class*="TopMenuStyles"]')
    footer = Footer(css='[class*="Footer"]')
    title = Text(xpath='//div[@class="column"]/child::h2')
    company = Component(css='[class*="CompanyDetails"]')

    def wait_for_loading(self, name: str) -> None:
        def condition() -> bool:
            try:
                assert self.menu.is_visible

                assert self.title == name
                assert self.company.visible

                return self.footer.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
