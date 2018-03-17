import random
import graphics as g

class Player:
  def choice(self):
    print("============================================")
    print("Please enter 'rock', 'paper', or 'scissors'.")
    p_choice = input()
    if p_choice == 'rock':
      return 'rock'
    elif p_choice == 'paper':
      return 'paper'
    elif p_choice == 'scissors':
      return 'scissors'
    else:
      print("that is an invalid guess, try again!")
      return None
    
class Computer :
  def choice(self):
    ran_choice = random.choice('rps')
    if ran_choice == 'r':
      return 'rock'
    if ran_choice == 'p':
      return 'paper'
    if ran_choice == 's':
      return 'scissors'

class Game:
  @staticmethod
  def logic(computer_c, player_c):
    if computer_c == 'rock' and player_c == 'rock':
      return "tie"
    elif computer_c == 'rock' and player_c == 'paper':
      return "you"
    elif computer_c == 'rock' and player_c == 'scissors':
      return "computer"
    elif computer_c == 'paper' and player_c == 'rock':
      return "computer"
    elif computer_c == 'paper' and player_c == 'paper':
      return "tie"
    elif computer_c == 'paper' and player_c == 'scissors':
      return "you"
    elif computer_c == 'scissors' and player_c == 'rock':
      return "you"
    elif computer_c == 'scissors' and player_c == 'paper':
      return "computer"
    elif computer_c == 'scissors' and player_c == 'scissors':
      return "tie"
 
  def play_game(self, num_rounds):
    player = Player()
    computer = Computer()
    current_rounds = 0
    player_score = 0
    computer_score = 0
    while current_rounds <= num_rounds -1:
      computer_c = computer.choice()
      player_c = player.choice()
      game_logic = self.logic(computer_c, player_c)
      if game_logic != None:
        current_rounds += 1
        g.ui.game_visual(player_c, computer_c)
        if game_logic == 'computer':
          print("The computer wins this round!")
          computer_score += 1
        elif game_logic == 'you':
          print("You win this round!")
          player_score += 1
        elif game_logic == 'tie':
          print("This round is a tie.")
        if current_rounds == num_rounds:
          if player_score > computer_score:
            print(g.ui.display_res("win"))
          elif computer_score > player_score:
            print(g.ui.display_res("loss"))
          elif computer_score == player_score:
            print("It's a tie game.")
    
game = Game()

def start_game():
  print("How many rounds would you like to play?")
  game_num = int(input())
  game.play_game(game_num)
  
start_game()

# print(random.choice("rps"))