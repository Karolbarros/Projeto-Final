
import time
from base import Inventario

class JogoUtil:
    inventory = []  # Inventário global

    @staticmethod
    def exibir_opcoes(opcoes, delay=0.05):
        """Exibe as opções disponíveis com um pequeno atraso entre os caracteres."""
        for i, opcao in enumerate(opcoes, 1):
            JogoUtil.print_slow(f'{i}. {opcao}', delay)

    @staticmethod
    def fazer_escolha(opcoes, delay=0.05):
        """Pede ao jogador para escolher uma opção."""
        while True:
            try:
                escolha = int(input("\nEscolha uma opção: ")) - 1
                if 0 <= escolha < len(opcoes):
                    return escolha
                else:
                    print("Ops!... Tente novamente.")
            except ValueError:
                print("Escolha inválida. Tente novamente.")

    @staticmethod
    def print_slow(text, delay=0.05):
        """Imprime o texto lentamente, caractere por caractere."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def adicionar_item(item):
        """Adiciona um item ao inventário."""
        JogoUtil.inventory.append(item)
        print(f"{item} foi adicionado ao seu inventário.")

    @staticmethod
    def mostrar_inventario():
        """Exibe o inventário atual do jogador."""
        print("\nSeu inventário:")
        if JogoUtil.inventory:
            for item in JogoUtil.inventory:
                print(f"- {item}")
        else:
            print("(Vazio)")
        print()
