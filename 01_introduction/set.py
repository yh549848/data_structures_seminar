from abc import ABCMeta, abstractmethod


class AbstractSet(metaclass=ABCMeta):
    @abstractmethod
    def add(self, x):
        pass

    @abstractmethod
    def remove(self, x):
        pass

    @abstractmethod
    def find(self, x):
        pass
