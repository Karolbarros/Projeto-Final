

import time

class JogoUtil:
    inventory = []  # Inventário global

    @staticmethod
    def exibir_opcoes(opcoes, delay=0.05):
        for i, opcao in enumerate(opcoes, 1):
            JogoUtil.print_slow(f'{i}. {opcao}', delay)

    @staticmethod
    def fazer_escolha(opcoes, delay=0.05):
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
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def adicionar_item(item):
        JogoUtil.inventory.append(item)

    @staticmethod
    def mostrar_inventario():
        print("\nSeu inventário:")
        if JogoUtil.inventory:
            for item in JogoUtil.inventory:
                print("-", item)
        else:
            print("(Vazio)")
        print()
