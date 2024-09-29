from Novice import Novice
import random

class Archer(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setAgi(5)  
        self.setInt(5) 
        self.setVit(5)  
        self.setHp(self.getHp() + self.getVit()) 

    def rangedAttack(self, character):
       
        damage = self.getDamage() + random.randint(0, self.getInt())
        character.reduceHp(damage) 
        print(f"{self.getusername()} performed a Ranged Attack! -{damage} HP")
