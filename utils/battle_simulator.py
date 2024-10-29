import random

class BattleSimulator:
    @staticmethod
    def simulate_battle(hero1, hero2):
        hero1_chance = hero1.nivel_forca + hero1.popularidade + random.randint(0, 10)
        hero2_chance = hero2.nivel_forca + hero2.popularidade + random.randint(0, 10)
        
        if hero1.popularidade > hero2.popularidade:
            hero1_chance += 5
        elif hero2.popularidade > hero1.popularidade:
            hero2_chance += 5

        if hero1_chance > hero2_chance:
            hero1.vitorias += 1
            hero2.derrotas += 1
            result = {"vencedor": hero1.nome_heroi, "perdedor": hero2.nome_heroi}
        else:
            hero2.vitorias += 1
            hero1.derrotas += 1
            result = {"vencedor": hero2.nome_heroi, "perdedor": hero1.nome_heroi}

        return result
