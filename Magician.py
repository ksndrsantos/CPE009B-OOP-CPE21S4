from Novice import Novice

class Magician(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setInt(5)  # Set intelligence to 5
        self.setVit(10)  # Set vitality to 10
        self.setHp(self.getHp() + self.getVit())  # Increase HP based on vitality

    def heal(self):
        self.addHp(self.getInt())  # Heal based on intelligence
        print(f"{self.getusername()} performed Heal! +{self.getInt()} HP")

    def magicAttack(self, character):
        damage = self.getDamage() + self.getInt()  # Use local variable instead of self.new_damage
        character.reduceHp(damage)  # Reduce opponent's HP
        print(f"{self.getusername()} performed Magic Attack! -{damage} HP")
