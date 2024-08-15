from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Action']


class ActionWrapper(ComponentWrapper):
    auth = Component(xpath="//a[text()='Перейти к авторизации']")
    register = Button(xpath="//span[text()='Регистрация без ЭП']")
    electronic_signature = Button(xpath="//span[text()='Выбрать электронную подпись']")
    continue_btn = Button(xpath="//span[text()='Продолжить']")


class Action(Component):
    def __get__(self, instance, owner) -> ActionWrapper:
        return ActionWrapper(instance.app, self.find(instance), self._locator)
