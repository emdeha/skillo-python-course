from abc import ABC, abstractmethod


class DictionaryInterface(ABC):
    @abstractmethod
    def get_value(self, key):
        pass

    @abstractmethod
    def set_value(self, key, value):
        pass


class DictionaryBasedOnList(DictionaryInterface):
    def __init__(self):
        self.__ls = []

    def get_value(self, key):
        return self.__ls[key.__hash__()]

    def set_value(self, key, value):
        self.__ls[key.__hash__()] = value


class DictionaryBasedOnDictionary(DictionaryInterface):
    def __init__(self):
        self.__dict = {}

    def get_value(self, key):
        return self.__dict[key]

    def set_value(self, key, value):
        self.__dict[key] = value


word_lengths = DictionaryBasedOnList()

word_lengths.set_value('one', 3)
word_lengths.set_value('four', 4)

print(word_lengths.get_value('one'))  # 3
print(word_lengths.get_value('four'))  # 4
