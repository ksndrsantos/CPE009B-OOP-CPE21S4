from Character import Character  

class Novice(Character):
    def basicAttack (self,character):
        character.reduceHp(self.getDamage())
        print (f"{self.getusername()} performed Basic Attack! -{self.getDamage()}")
    
character1=Novice("Your Username")

"for single inheritance from the character.py"
