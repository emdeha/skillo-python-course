from abc import ABC, abstractmethod


class Fee(ABC):
    @abstractmethod
    def withdrawal_fee(self):
        pass

    @abstractmethod
    def monthly_fee(self, overdraft):
        pass
