class Personaje:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__life = 100
        self.__attackeDamage = 15
        self.__defense = 5

    
    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        if 0 <= value <= 100:
            self.__life = value

    @property
    def attackeDamage(self):
        return self.__attackeDamage

    @attackeDamage.setter
    def attackeDamage(self, value):
        if 0 <= value <= 100:
            self.__attackeDamage = value
        else:
            print("Valor para la vida inválido. Debe ser entre 0 y 100")

    @property
    def defense(self):
        return self.__defense 

    @defense.setter
    def defense(self, value):
        if 0 <= value <= 100:
            self.__defense = value
        else:
            print("Valor para la vida inválido. Debe ser entre 0 y 100")

    def attack(self, objetive):
        if not isinstance(objetive, Personaje):
            print("❌ El objetivo no es un personaje válido")
            return
        else:
            print(objetive.life() > 0)
            if objetive.life() == 0:
                print(f"El personaje ${self.name} le ha ganado a ${objetive.name}")
            else:
                objetive.life = objetive.__attackeDamage - objetive.__defense
            
            if objetive.life() == 0: 
                print(f"El personaje ${self.name} le ha ganado a ${objetive.name}")
    