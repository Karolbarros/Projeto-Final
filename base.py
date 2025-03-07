from abc import ABC, abstractmethod

class Fase(ABC):
    @abstractmethod
    def executar(self):
        pass

class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        """Adiciona um item ao inventário."""
        if item not in self.itens:
            self.itens.append(item)
            print(f"{item} foi adicionado ao seu inventário.")
        else:
            print(f"O item {item} já está no inventário.")

    def remover_item(self, item):
        """Remove um item do inventário."""
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} foi removido do inventário.")
        else:
            print(f"O item {item} não está no inventário.")

    def mostrar_inventario(self):
        """Exibe os itens presentes no inventário."""
        if not self.itens:
            print("Seu inventário está vazio.")
        else:
            print("Itens no seu inventário:")
            for item in self.itens:
                print(f"- {item}")

    def tem_item(self, item):
        """Verifica se um item está presente no inventário."""
        return item in self.itens