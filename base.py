from abc import ABC, abstractmethod

class Fase(ABC):
    @abstractmethod
    def executar(self):
        pass
