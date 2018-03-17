import gm

start = gm.create_board(3, 4)



# print game board
def display(row:int, col:int):
    for item in gm.create_contents(row,col):
        print('| '+'  '.join(item)+' |')
        
    print  (' '+'-' *3*col+ ' ')


display(3,4)
        


# ===============================================================================================

'''def number_rows():
    #returns number of rows selected by user. You can assume this will be no less than 4.
    row = input()
    return row
def number_columns():
    #returns number of columns selected by user. You can assume this will be no less than 3.
    column = input()
    return column

 
    

def start():
    #returns input of start with an empty field or contents of the field in the input.
    row = int(number_rows())
    column = int(number_columns())
    start = input()
    if start == 'EMPTY':
   
        game  = game_mechanics.create_board(row, column)
        print(game)
        print('display board')
##        display(row,column)
        
    elif start == 'CONTENTS': 
        print(game_mechanics.create_contents(row,column))
        display(row,column)
        
            
      

def display(row: int, column: int):
    #creates a visual grid with content
    for item in game_mechanics.create_contents(row,column):
        
      
        
        
        print('|'+str(item)+'|')

    print  (' '+'-' *3*column+ ' ')


    
            
    

if __name__ == "__main__":
    start()'''



