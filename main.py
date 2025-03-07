
from fases import FaseInicial
from util import JogoUtil

class Jogo:
    def __init__(self):
        # Reinicia o inventário sempre que o jogo recomeça
        JogoUtil.inventory = []
        self.__fase_atual = FaseInicial()

    def jogar(self):
        while self.__fase_atual:
            self.__fase_atual = self.__fase_atual.executar()
            if not self.__fase_atual:
                jogar_novamente = input("\nQuer jogar novamente? (sim/nao) ").strip().lower()
                if jogar_novamente == "sim":
                    JogoUtil.inventory = []  # Limpa o inventário
                    self.__fase_atual = FaseInicial()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()

