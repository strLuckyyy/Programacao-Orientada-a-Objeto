class Player:
    def __init__(self, name: str, damageAtk: float, defense: float, life: float) -> None:
        self.playerName = name
        self.playerDamage = damageAtk
        self.playerDefense = defense
        self.playerLife = life
    

    def darDano(self, playerDamage: float):
        print('Player atacou o inimigo.')
        return playerDamage