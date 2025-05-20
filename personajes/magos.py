from personajes.personaje import Personaje

class Mago(Personaje):
    def __init__(self, name, description):
        super().__init__(name, description)

    def attack(self, objetive):
        if not isinstance(objetive, Personaje):
            print("❌ El objetivo no es un personaje válido")
            return
        else:
            print(objetive.life > 0)
            if objetive.life == 0:
                print(f"El personaje ${self.name} le ha ganado a ${objetive.name}")
            else:
                objetive.life -= self.attackeDamage

            # Verificar nuevamente despues de que el ovjetivo reciba el ataque
            if objetive.life == 0: 
                print(f"El personaje ${self.name} le ha ganado a ${objetive.name}")
    