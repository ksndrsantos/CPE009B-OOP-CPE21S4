from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician

class Boss(Swordsman, Archer, Magician):
    def __init__(self, username):
        super().__init__(username)
        self.setInt(10)
        self.setVit(25)
        self.setHp(self.getHp() + self.getVit())
