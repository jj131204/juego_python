
import random
import time
from personajes.arqueros import Arquero
from personajes.guerreros import Guerrero
from personajes.magos import Mago

# Crear instancias de cada personaje
p1 = Guerrero("Volibear", "Guerrero feroz")
p2 = Mago("Ryze", "Hechicero azul")
p3 = Arquero("Ashe", "Maestra del arco")

p1.life = 100
p1.attackeDamage = 30
p1.defense = 20

p2.life = 80
p2.attackeDamage = 40
p2.defense = 10

p3.life = 80
p3.attackeDamage = 35
p3.defense = 15

personajes = [p1, p2, p3]

player1, player2 = random.sample(personajes, 2)

print(f"\n🔥 ¡Combate entre {player1.name} y {player2.name} inicia! 🔥\n")

turno = 1
while player1.life > 0 and player2.life > 0:
    print(f"🔁 Turno {turno}")
    if turno % 2 == 1:
        player1.attack(player2)
    else:
        player2.attack(player1)

    print(f"vida de ${player1.name} es: ${player1.life} y la vide de ${player2.name} es: ${player2.life}")
    time.sleep(1)  # pausa de 1 segundo entre turnos
    turno += 1

