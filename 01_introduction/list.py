from abc import ABCMeta, abstractmethod


class AbstractList(metaclass=ABCMeta):
    @abstractmethod
    def get(self, i):
        pass

    @abstractmethod
    def set(self, i, x):
        pass

    @abstractmethod
    def add(self, i, x):
        pass

    @abstractmethod
    def remove(self, i):
        pass
