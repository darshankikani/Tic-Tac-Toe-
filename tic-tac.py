import itertools

def win(current_game):

   def all_same(l):  ##function for optimizing if statement in winner logic
      if l.count(l[0]) == len(l) and l[0] !=0:
         return True
      else:
         return False

         
   ##horizental winner logic
   for row in tictactoeboard:
      print(row)
      if all_same(row):
         print (f"player {row[0]} is the winner horizontally!")
         return True

#diagonal winner logic
   diags =[]
   for col, row in enumerate(reversed(range(len(tictactoeboard)))):
      diags.append(tictactoeboard[row][col])
      
   if all_same(diags):
      print (f"player {diags[0]} is the winner diagonal ! (/)")
      return True
         
   diags =[]
   for ix in range (len(tictactoeboard)):
      diags.append(tictactoeboard[ix][ix])
      
   if all_same(diags):
      print (f"player {diags[0]} is the winner diagonal ! (\\)")
      return True


   ##vertical winner logic

   for col in range(len(tictactoeboard)):
      check= []

      for row in tictactoeboard:
         check.append(row[col])

      if all_same(check):
         print (f"player {check[0]} is the winner  vertically ! ")
         return True
   return False
      
def game_board(game_map, player=0, row=0, column=0, just_display=False):
   try:
      if game_map[row][column] != 0:  ##postion is already taken condition 
         print("This postion is taken ! choose another ")
         return game_map, False
      print("     0  1  2")  #print the column number on a board
      if not just_display:
         game_map[row][column] = player  ##it display the board with mark postion 
      for count, row in enumerate(game_map) :
           print(count, row)    #print board and row number on a board 
      return game_map, True
   except IndexError as e:
     print("Eroo: Make sure you input row/column as 0, 1 or 2 ?",e)  #show error when someone choose outof bund index 
     return game_map,False

play=True
players=[1,2]

while play:
   tictactoeboard = [[0,0,0],
                                    [0,0,0],
                                    [0,0,0]]
   game_won= False
   tictactoeboard, _ =game_board(tictactoeboard, just_display=True)
   player_choice= itertools.cycle([1,2])
   while not game_won:  #choose alternate player during play
      current_player = next(player_choice)
      print(f"current player : {current_player}")
      played =False

      while not played:  #ask for row and column from user
         column_choice = int(input ("What column do you want to play? (0, 1, 2) :  "))
         row_choice = int(input ("What row do you want to play? (0, 1, 2) :  "))
         tictactoeboard, played = game_board(tictactoeboard, current_player, row_choice, column_choice)

      if win(tictactoeboard):  #Ask user for further play 
         game_won= True
         again= input("The Game is over, Would you like to Play Again ? (y/n)  ")
         if again.lower() == "y":
            print("Restarting ")
         elif again.lower() == "n":
            print ("Byeee")
            play= False
         else:
            print("Not a Valid Answer , so see you later ")
            play=False





