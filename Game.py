from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss
from Novice import Novice
import random


class Game:
    def __init__(self):
        self.c1 = None #player 1
        self.c2 = None #player 2
        self.mode = None  #what mode the player would like to choose
        self.c1_wins = 0
        self.c2_wins = 0
        
    #The game must be able to select between 2 modes: Single player and Player vs Player.
    
    def select_mode(self):
        print ("Welcome to THE GAME! please choose your game mode: ")
        print ("Player Type")
        print ("1. Single Player")
        print ("2. Player Vs Player")
        choice = input ("Select 1 for single player and Select 2 for PvP")
        
        if choice == '1' :
            self.mode = 'Single Player'
            self.start_single_player()
        elif choice == '2':
            self.mode = 'Player vs Player'
            self.start_player_vs_player()
        else :
            print ("Please choose your Game Mode")
            self.select_mode()
    
    #for single player mode
    
    def start_single_player(self):
        print ("WELCOME TO SINGLE PLAYER MODE")
        self.player1 = Novice(input("What's your name?': "))
        self.player2 = Boss("Monster")  # Opponent in this mode is the boss aka the monster
        self.play_game()
    
    #for player vs player
    
    def start_player_vs_player(self):
        print ("WELCOME TO PLAYER VS PLAYER MODE")
        self.player1 = self.select_role(input("Player 1, enter your name: "))
        self.player2 = self.select_role(input("Player 2, enter your name: "))
        self.play_game()
    
    def select_role(self, username):
        print(f"Select a role for {username}:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Magician")
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return Swordsman(username)
        elif choice == '2':
            return Archer(username)
        elif choice == '3':
            return Magician(username)
        else:
            print(" Defaulting to Novice.")
            return Novice(username)

    def play_game(self):
        while self.player1.getHp() > 0 and self.player2.getHp() > 0:
            self.take_turns()
            self.check_winner()

    def take_turns(self):
        players = [self.player1, self.player2]
        random.shuffle(players)
        attacker = players[0]
        defender = players[1]
        Novice.slashAttack(Boss) 
        print(f"{attacker.getusername()}'s turn!")
        attacker.basicAttack(defender)
        print(f"{defender.getusername()} HP: {defender.getHp()}")

    def check_winner(self):
        if self.player1.getHp() <= 0:
            print(f"{self.player2.getusername()} wins!")
            self.player2_wins += 1
            self.reset_game()
        elif self.player2.getHp() <= 0:
            print(f"{self.player1.getusername()} wins!")
            self.player1_wins += 1
            self.reset_game()

    def reset_game(self):
        choice = input("Do you want to play another match? (y/n): ")
        if choice == 'y':
            if self.mode == 'Single Player':
                self.start_single_player()
            else:
                self.start_player_vs_player()
        else:
            print(f"Final Score - Player 1 Wins: {self.player1_wins}, Player 2 Wins: {self.player2_wins}")
            print("Thanks for playing!")
            exit()
        
    