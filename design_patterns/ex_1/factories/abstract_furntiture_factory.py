from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass