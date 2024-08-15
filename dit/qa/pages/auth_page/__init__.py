from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.menu import Menu

__all__ = ['AuthPage']


class AuthPage(Page):
    menu = Menu(css='[class*="TopMenuStyles"]')
    title = Component(xpath="//h2[text()='Вход']")
    login = TextField(id="login")
    password = TextField(id="password")
    forgot_password = Component(xpath="//a[text()='Забыли пароль?']")
    submit = Button(xpath="//span[text()='Войти']")
    log_pass = Component(xpath="//div[text()='Логин и пароль']")
    ep = Component(xpath="//div[text()='ЭП']")
    invest = Component(xpath="//div[text()='Инвестпортал']")
    mo = Component(xpath="//div[text()='МО ЕАСУЗ']")
    ros = Component(xpath="//div[text()='Росэлторг']")
    vtb = Component(xpath="//div[text()='ВТБ Коннект']")
    tek = Component(xpath="//div[text()='ТЭК-Торг']")
    mos = Component(xpath="//div[text()='mos.ru']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.logo.visible
                assert self.menu.main.visible
                assert self.menu.support_modal.visible
                assert self.menu.knowledge.visible

                assert self.title.visible
                assert self.login.visible
                assert self.password.visible
                assert self.forgot_password.visible
                assert self.log_pass.visible
                assert self.ep.visible
                assert self.invest.visible
                assert self.mo.visible
                assert self.ros.visible
                assert self.vtb.visible
                assert self.tek.visible
                assert self.mos.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Страница авторизации не загружена')
        self.app.restore_implicitly_wait()
