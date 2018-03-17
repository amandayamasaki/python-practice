

res = []

# Create blank game board
def create_board(row:int, col:int):
    res = []
    for i in range(row):
        res.append([])
        for j in range(col):
            res[-1].append(' ')
    return res

           
def create_contents(row: int, col: int):
    for i in range(row):
        conts = list(input())
        if len(conts)<col:
            conts.append(' '*(col-len(conts)))
        res.append(conts)
    return res

# ==============================================================================

'''def create_board (row: int, column: int):
  #  Creates a empty 2d list
    result = []
   

    for i in range(row):
        result.append([])
        for i in range(column):
            result[-1].append(' ')

    return result



def create_contents(row: int, column: int):
    #creates a 2d list with content
           
    result = []
    for i in range(row):
        
            conts = list(input())
            if len(conts)<column:
                conts.append(' '*(column-len(conts)))
            result.append(conts)
           
                
            
        
    return result'''

