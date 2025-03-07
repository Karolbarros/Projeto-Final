
from base import Fase
from Until import JogoUtil

# FASE INICIAL – Escolha entre o caminho iluminado (que leva ao sábio) ou o sombrio.
class FaseInicial(Fase):
    def __init__(self):
        self.__descricao = (
            "Você desperta em uma floresta misteriosa.\n"
            "Há um caminho iluminado pelo sol e outro sombrio à sua frente."
        )
        self.__opcoes = [
            "Seguir pelo caminho iluminado",
            "Seguir pelo caminho sombrio",
            "Ver inventário"
        ]

    def exibir_descricao(self):
        JogoUtil.print_slow(self.__descricao)

    def executar(self):
        JogoUtil.print_slow("\nFase Inicial")
        self.exibir_descricao()
        while True:
            JogoUtil.exibir_opcoes(self.__opcoes)
            escolha = JogoUtil.fazer_escolha(self.__opcoes)
            if self.__opcoes[escolha].lower() == "ver inventário":
                JogoUtil.mostrar_inventario()
            else:
                break

        if escolha == 0:
            return Parte2()
        elif escolha == 1:
            return Parte3()

# PARTE 2 – Encontro com o sábio que oferece a chave.
class Parte2(Fase):
    def __init__(self):
        self.__descricao = (
            "Você encontra um velho sábio que possui uma chave dourada e a oferece a você."
        )

    def exibir_descricao(self):
        JogoUtil.print_slow(self.__descricao)

    def executar(self):
        print("\nParte 2")
        self.exibir_descricao()
        opcoes_chave = ["Aceitar a chave", "Recusar a chave", "Ver inventário"]
        while True:
            JogoUtil.exibir_opcoes(opcoes_chave)
            escolha = JogoUtil.fazer_escolha(opcoes_chave)
            if opcoes_chave[escolha].lower() == "ver inventário":
                JogoUtil.mostrar_inventario()
            else:
                break

        if escolha == 0:
            JogoUtil.print_slow("Você aceita a chave dourada.")
            JogoUtil.adicionar_item("Chave dourada")
            return EscolhaDestino()
        else:
            JogoUtil.print_slow("Você recusa a chave dourada.")
            # Pergunta se deseja buscar a chave derrotando monstros
            opcoes_busca = [
                "Tentar buscar a chave derrotando monstros",
                "Continuar sem a chave",
                "Ver inventário"
            ]
            while True:
                JogoUtil.exibir_opcoes(opcoes_busca)
                escolha_busca = JogoUtil.fazer_escolha(opcoes_busca)
                if opcoes_busca[escolha_busca].lower() == "ver inventário":
                    JogoUtil.mostrar_inventario()
                else:
                    break
            if escolha_busca == 0:
                return BuscaChave()
            else:
                return EscolhaDestino()

# PARTE 3 – Caminho sombrio com escolhas de fugir ou enfrentar criaturas.
class Parte3(Fase):
    def __init__(self):
        self.__descricao = (
            "Você segue pelo caminho sombrio e se perde.\n"
            "Logo percebe olhos brilhando ao seu redor."
        )
        self.__opcoes = ["Correr", "Enfrentar as criaturas", "Ver inventário"]

    def exibir_descricao(self):
        JogoUtil.print_slow(self.__descricao)

    def executar(self):
        print("\nParte 3")
        self.exibir_descricao()
        while True:
            JogoUtil.exibir_opcoes(self.__opcoes)
            escolha = JogoUtil.fazer_escolha(self.__opcoes)
            if self.__opcoes[escolha].lower() == "ver inventário":
                JogoUtil.mostrar_inventario()
            else:
                break

        if escolha == 0:
            return Parte6()
        else:
            return Parte7()

# ESCOLHA DO DESTINO – Após a decisão sobre a chave, o jogador escolhe para onde ir.
class EscolhaDestino(Fase):
    def __init__(self):
        self.__descricao = "Agora, escolha seu destino:"
        self.__opcoes = ["Ir para o templo antigo", "Explorar a floresta", "Ver inventário"]

    def exibir_descricao(self):
        JogoUtil.print_slow(self.__descricao)

    def executar(self):
        print("\nEscolha do Destino")
        self.exibir_descricao()
        while True:
            JogoUtil.exibir_opcoes(self.__opcoes)
            escolha = JogoUtil.fazer_escolha(self.__opcoes)
            if self.__opcoes[escolha].lower() == "ver inventário":
                JogoUtil.mostrar_inventario()
            else:
                break
        # Se for para o templo ou floresta, o final dependerá se o jogador possui a chave.
        if escolha == 0:
            if "Chave dourada" in JogoUtil.inventory:
                return FinalTemploComChave()
            else:
                return FinalTemploSemChave()
        elif escolha == 1:
            if "Chave dourada" in JogoUtil.inventory:
                return FinalFlorestaComChave()
            else:
                return FinalFlorestaSemChave()

# BUSCA DA CHAVE – Caso o jogador tenha recusado a chave do sábio e queira tentar obtê-la enfrentando monstros.
class BuscaChave(Fase):
    def __init__(self):
        self.__descricao = (
            "Você decide tentar buscar a chave derrotando monstros.\n"
            "Rumores dizem que em uma caverna escura, monstros guardam um tesouro incomum."
        )
        self.__opcoes = ["Enfrentar os monstros", "Voltar sem tentar", "Ver inventário"]

    def exibir_descricao(self):
        JogoUtil.print_slow(self.__descricao)

    def executar(self):
        print("\nBusca da Chave")
        self.exibir_descricao()
        while True:
            JogoUtil.exibir_opcoes(self.__opcoes)
            escolha = JogoUtil.fazer_escolha(self.__opcoes)
            if self.__opcoes[escolha].lower() == "ver inventário":
                JogoUtil.mostrar_inventario()
            else:
                break
        if escolha == 0:
            return BatalhaMonstro()
        else:
            return EscolhaDestino()

# BATALHA CONTRA OS MONSTROS – Simula o confronto para conquistar a chave.
class BatalhaMonstro(Fase):
    def __init__(self):
        self.__descricao = "Você enfrenta os monstros em uma batalha intensa."
        self.__opcoes = ["Lutar com todas as forças", "Fugir da batalha"]

    def exibir_descricao(self):
        JogoUtil.print_slow(self.__descricao)

    def executar(self):
        print("\nBatalha contra os Monstros")
        self.exibir_descricao()
        while True:
            JogoUtil.exibir_opcoes(self.__opcoes)
            escolha = JogoUtil.fazer_escolha(self.__opcoes)
            if escolha == 0:
                # Aqui assumimos a vitória do jogador.
                JogoUtil.print_slow(
                    "Após uma luta árdua, você derrota os monstros e conquista a chave dourada!"
                )
                if "Chave dourada" not in JogoUtil.inventory:
                    JogoUtil.adicionar_item("Chave dourada")
                return EscolhaDestino()
            elif escolha == 1:
                return FinalFuga()

# FIM – Caso o jogador fuja da batalha.
class FinalFuga(Fase):
    def executar(self):
        JogoUtil.print_slow(
            "Você foge da batalha, perdendo a chance de obter a chave. Fim de jogo."
        )
        return None

# FINAIS – Diferentes desfechos de acordo com a escolha do destino e se a chave foi obtida.
class FinalTemploComChave(Fase):
    def executar(self):
        JogoUtil.print_slow(
            "Você usa a chave dourada para abrir a porta do templo e encontra riquezas incalculáveis. Parabéns!"
        )
        return None

class FinalFlorestaComChave(Fase):
    def executar(self):
        JogoUtil.print_slow(
            "Na floresta, um baú misterioso aparece. Com a chave dourada, você o abre e descobre segredos ancestrais!"
        )
        return None

class FinalTemploSemChave(Fase):
    def executar(self):
        JogoUtil.print_slow(
            "Você chega ao templo antigo, mas sem a chave, a porta permanece trancada.\n"
            "Você se perde tentando descobrir outra entrada. Fim de jogo."
        )
        return None

class FinalFlorestaSemChave(Fase):
    def executar(self):
        JogoUtil.print_slow(
            "Explorando a floresta, você encontra um baú trancado.\n"
            "Sem a chave, o mistério permanece sem solução. Fim de jogo."
        )
        return None

# Finais do caminho sombrio
class Parte6(Fase):
    def executar(self):
        JogoUtil.print_slow("Você corre, mas as criaturas são mais rápidas. Fim de jogo.")
        return None

class Parte7(Fase):
    def executar(self):
        JogoUtil.print_slow("Você enfrenta as criaturas e vence, tornando-se um herói lendário!")
        return None
