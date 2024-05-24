from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    logo = Component(css='[class*="FullLogo"]')
    main = Component(css='[class*="MainMenuStyles"]')
    appeal = Component(xpath="//div[text()='Оставить обращение']")
    support = Component(xpath="//div[text()='Центр поддержки']")
    city = Component(xpath="//div[text()='г Москва']")
    city_kirov = Component(xpath="//div[text()='обл Кировская']")
    submit = Button(xpath="//button[text()='Войти']")
    register = Button(xpath="//span[text()='Зарегистрироваться']")
    user_name = Component(xpath="//div[text()='pp_monitoring']")
    support_modal = Component(css='[class*="SupportModal"]')
    knowledge = Component(css='[href*="knowledgebase"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.main.visible
        assert self.appeal.visible

        return self.support.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
