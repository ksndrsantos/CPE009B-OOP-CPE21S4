from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

Character1 = Swordsman("Royce")
Character2 = Magician("Archie")

print(f"{Character1.getusername()} HP: {Character1.getHp()}")  
print(f"{Character2.getusername()} HP: {Character2.getHp()}")  

Character1.slashAttack(Character2)  
Character1.basicAttack(Character2)   

print(f"{Character1.getusername()} HP: {Character1.getHp()}")  
print(f"{Character2.getusername()} HP: {Character2.getHp()}")  

Character2.heal()                     
Character2.magicAttack(Character1)    
Character2.rangedAttack(Character1)   

print(f"{Character1.getusername()} HP: {Character1.getHp()}") 
print(f"{Character2.getusername()} HP: {Character2.getHp()}")  

