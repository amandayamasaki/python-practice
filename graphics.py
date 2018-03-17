class Ui:
  def p_choice(self, choice):
    if choice == "rock":
      return l_r
    if choice == "paper":
      return l_p
    if choice == "scissors":
      return l_s
      
  def c_choice(self, choice):
    if choice == "rock":
      return r_r
    if choice == "paper":
      return r_p
    if choice == "scissors":
      return r_s
  
  def game_visual(self, player_c, computer_c):
    board = self.p_choice(player_c) + (self.c_choice(computer_c))
    print(board)
    print("you played", player_c, "| computer played", computer_c)
  
  def display_res(self, res):
    if res == "win":
      return win
    elif res == "loss":
      return loss
  
ui = Ui()

space ="         "

l_r = """
    _______
---'   ____) 
      (_____)
      (_____)
      (____)
---.__(___)
"""

l_p = """
    _______
---'   ____)____
          ______)
          _______)
          ______)
---.__________)
"""

l_s = """
    _______
---'   ____)____
          ______)
      __________)
      (____)    
---.__(___)
"""

r_r = """
  _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---
"""

r_p = """
       _______
  ____(____   '---
 (______
(_______
 (______
   (__________.---
"""

r_s = """
      _______
 ____(____   '---
(______
(__________
     (____)
      (___)__.---
"""

win = """
                         _      
  _  _ ___ _  _  __ __ _(_)_ _  
 | || / _ \ || | \ V  V / | ' \ 
  \_, \___/\_,_|  \_/\_/|_|_||_|
  |__/    
"""

loss = """
                  _             
  _  _ ___ _  _  | |___ ___ ___ 
 | || / _ \ || | | / _ (_-</ -_)
  \_, \___/\_,_| |_\___/__/\___|
  |__/           
"""





