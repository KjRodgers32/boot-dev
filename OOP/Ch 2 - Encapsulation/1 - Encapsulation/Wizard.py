class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

        def get_fireballed(self):
            self.health -= 500
        
        def drink_mana_potion(self):
            self.mana += 100