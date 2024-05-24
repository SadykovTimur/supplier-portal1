from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Modal']


class ModalWrapper(ComponentWrapper):
    create_user = Component(xpath="//h2[text()='Подтверждение создания пользователя']")
    content = Text(css='[class*="NotificationContent"]')
    accept = Button(id="notification-accept")
    cancel = Button(id="notification-cancel")


class Modal(Component):
    def __get__(self, instance, owner) -> ModalWrapper:
        return ModalWrapper(instance.app, self.find(instance), self._locator)
