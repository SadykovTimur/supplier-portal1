from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['TestLinkPage']


class TestLinkPage(Page):
    number = Text(tag='body')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                return '"2"' == self.number

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Server answer incorrect')
        self.app.restore_implicitly_wait()
