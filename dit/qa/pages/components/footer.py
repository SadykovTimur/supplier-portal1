from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Footer']


class FooterWrapper(ComponentWrapper):
    logo = Component(css='[class*="Logo"]')
    portal = Component(xpath="//div[text()='О портале']")
    contact = Component(xpath="//div[text()='Контакты']")
    news = Component(xpath="//div[text()='Новости']")
    support_center = Component(xpath="//div[text()='Центр поддержки']")
    map = Component(xpath="//div[text()='Карта сайта']")
    tg = Component(xpath="//div[text()='Наш телеграм-канал']")

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.portal.visible
        assert self.news.visible
        assert self.support_center.visible
        assert self.map.visible
        return self.contact.visible


class Footer(Component):
    def __get__(self, instance, owner) -> FooterWrapper:
        return FooterWrapper(instance.app, self.find(instance), self._locator)
