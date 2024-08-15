from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    logo = Component(css='[class*="FullLogo"]')
    main = Component(css='[class*="MainMenuStyles"]')
    registration = Component(css='[class*="PrimaryButton"]')
    submit = Button(xpath="//button[text()='Войти']")
    user_name = Component(xpath="//div[text()='pp_monitoring']")
    support_modal = Component(css='[class*="SupportModal"]')
    knowledge = Component(css='[href*="knowledgebase"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.main.visible
        assert self.registration.visible

        return self.submit.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
