import pandas as pd

def transform_str_to_df(data_input):
    # remove space and transform string to 9x9 matrix
    data_input = data_input.replace(' ','')
    res = []; temp = []
    for i in data_input:
        temp.append(int(i))
        if len(temp) == 9:
            res.append(temp)
            temp = []
    return pd.DataFrame(res)

def count_blank_cell(sudoku):
    # count the number of blank cell in the 9x9 matrix
    return sum(sudoku.apply(lambda x: sum(x == 0)))

def find_blank_a_cell(sudoku):
    # find the first blank cell in the 9x9 matrix
    for i in range(9):
        for j in range(9):
            if sudoku.iloc[i,j] == 0:
                return i,j
    return -1,-1

def get_position_name_by_index(index):
        # get the position name by index
        if index in [0,1,2]:
            return 'top'
        elif index in [3,4,5]:
            return 'mid'
        elif index in [6,7,8]:
            return 'bot'
        
def get_square(data, vertical, horizontal):
    # select a 3x3 matrix from the 9x9 matrix
    if vertical == 'top':
        res = data.iloc[0:3]
    elif vertical == 'mid':
        res = data.iloc[3:6]
    elif vertical == 'bot':
        res = data.iloc[6:9]
    if horizontal == 'top':
        res = data.iloc[:,0:3]
    elif horizontal == 'mid':
        res = data.iloc[:,3:6]
    elif horizontal == 'bot':
        res = data.iloc[:,6:9]
    return res

def get_vline(data,col_idx):
    # select a column from the 9x9 matrix
    return data.iloc[:,col_idx]

def get_hline(data,row_idx):
    # select a row from the 9x9 matrix
    return data.iloc[row_idx]