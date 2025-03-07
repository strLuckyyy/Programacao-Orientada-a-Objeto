class Enemy:

    def __init__(self, name: str, damageAtk: float, defense: float, life: float) -> None:
        self.name = name
        self.damage = damageAtk
        self.defense = defense
        self.life = life


    def darDano(self, damage: float):
        print(f'inimigo chegou perto do jogador, ele golpeou dando {damage} de dano.')
    
    
    def receberDano(self, dano: float, life: float, defense: float):
        
        danoRecebido = dano - defense
        print(f'Inimigo foi atacado pelo jogador, ele recebeu {danoRecebido}'
              f'\nO inimigo está com {life} de vida.')


    def morte(self):
        print('O inimigo morreu.')
