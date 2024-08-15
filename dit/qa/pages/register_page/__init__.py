from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.register_page.components.action import Action
from dit.qa.pages.register_page.components.modal import Modal

__all__ = ['RegisterPage']


class RegisterPage(Page):
    title = Component(xpath="//h1[contains(text(),'Регистрация')]")
    signature = Component(xpath="//p[text()='Выберите электронную подпись для регистрации']")
    action_bar = Action(css='[class*="ActionBarStyles"]')
    modal = Modal(id="notification-modal")
    user_registration = Component(xpath="//h2[text()='Регистрация пользователя']")
    check_data = Component(xpath="//p[text()='Проверьте данные и внесите изменения при необходимости']")
    last_name = TextField(id="lastName")
    first_name = TextField(id="firstName")
    middle_name = TextField(name="user.attributes.middle.name")
    email = TextField(name="email")
    password = TextField(name="password")
    password_confirm = TextField(name="password-confirm")
    agreement = Button(id="acceptAgreement")
    regulation = Button(css='[for="acceptRegulation"]')
    checkbox = Components(css='[class*="radio"]')
    send = Button(xpath="//span[text()='Отправить']")
    unknown_user = Component(xpath="//span[text()='Имя пользователя уже занято.']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.signature.visible

                assert self.action_bar.auth.visible
                assert self.action_bar.register.visible

                return self.action_bar.electronic_signature.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Окно регистрации не загружено')
        self.app.restore_implicitly_wait()

    def wait_transition_register(self) -> None:
        def condition() -> bool:
            try:
                assert self.user_registration.visible
                assert self.last_name.visible
                assert self.first_name.visible
                assert self.middle_name.visible
                assert self.email.visible
                assert self.password.visible
                assert self.password_confirm.visible

                return self.check_data.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Упрощенная регистрация не загружена')
        self.app.restore_implicitly_wait()

    def wait_confirmation_create_user(self) -> None:
        def condition() -> bool:
            try:
                assert self.modal.create_user.visible
                assert (
                    self.modal.content == 'Создать пользователя Орлов Геннадий Сергеевич с email kakzdorov@yandex.ru?'
                )
                assert self.modal.accept.visible

                return self.modal.cancel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Модальное окно создания пользователя не загружено')
        self.app.restore_implicitly_wait()

    def wait_create_user(self) -> None:
        def condition() -> bool:
            try:
                return self.unknown_user.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Пользователь не создан')
        self.app.restore_implicitly_wait()
