import pandas as pd
from retrieve import *

def validate_9x9_input(input_sudoku):
    # make sure it has 81 elements
    input_sudoku = input_sudoku.replace(' ','')
    return len(input_sudoku) == 81

def validate_3x3(sudoku_3x3):
    # make sure 3x3 matrix has 9 unique elements
    return  set(sudoku_3x3.values.reshape(-1)) == set(range(1,10))


def validate_hline(hline):
    # make sure row has 9 unique elements
    element_counts = hline.value_counts()
    for i in range(1,10):
        try:
            if element_counts[i] != 1:
                print(f"Duplicated element {i} in hline")
                return False
        except:
            print(f"Element {i} does not exist in the hline")
            return False
    return True

def validate_vline(vline):
    # make sure column has 9 unique elements
    element_counts = vline.value_counts()
    for i in range(1,10):
        try:
            if element_counts[i] != 1:
                print(f"Duplicated element {i} in vline")
                return False
        except:
            print(f"Element {i} does not exist in the vline")
            return False
    return True

def validate_intermediate_3x3(sudoku_3x3):
    # True if only 1 available slot in the 3x3 dataframe
    return sudoku_3x3.sum().sum() == 1

def validate_intermediate_hline(hline):
    # True if only 1 available slot in the hline
    return hline.sum() == 1

def validate_intermediate_vline(vline):
    # True if only 1 available slot in the vline
    return vline.sum() == 1

def validate_9x9(input_sudoku):
    # validate the sudoku is completed and followed the rules

    # validate each 3x3
    position = ['top','mid','bot']
    for i_pos in position:
        for j_pos in position:
            sudoku_3x3 = get_square(input_sudoku, i_pos, j_pos)
            if validate_3x3(sudoku_3x3) == False:
                print(f"{i_pos}-{j_pos} duplicated element detected\n" , sudoku_3x3)
                return False

# validate each horizontal line
    for i in range(len(input_sudoku)):
        hline = input_sudoku.iloc[i]
        if validate_hline(hline) == False:
            return False

    # validate each vertical line
    for i in range(len(input_sudoku)):
        vline = input_sudoku.iloc[i]
        if validate_vline(vline) == False:
            return False
    return True

def mark_3x3(number_availability, row, col):
    # take a 9x9 dataframe and mark the availability of number in the cell
    # 3x3
    i_start = row//3 * 3
    j_start = col//3 * 3
    number_availability.iloc[i_start:i_start+3, j_start:j_start+3] = [[False]*3 for i in range(3)]

    return number_availability

def mark_hline(number_availability, row):
    # take a 9x9 dataframe and mark the availability of the row be False
    # horizontal
    number_availability.iloc[row] = [False] * 9
    return number_availability

def mark_vline(number_availability, col):
    # take a 9x9 dataframe and mark the availability of the col be False
    # vertical
    number_availability.iloc[:,col] = [False] * 9
    return number_availability

def mark_availability(number_availability, row, col):
    # take a 9x9 dataframe and mark the availability of number in the cell
    # 3x3
    number_availability = mark_3x3(number_availability, row, col)
    # horizontal
    number_availability = mark_hline(number_availability, row)
    # vertical
    number_availability = mark_vline(number_availability, col)
    return number_availability

def create_numbers_availability(input_sudoku):
    # create a 9x9 dataframe for each number to store the availability of number in each cell
    numbers_availability = []
    for i in range(1,10):
        # create a all True 9x9 dataframe to store the availability of number i in each cell
        temp = pd.DataFrame([[True] * 9 for i in range(9)])
        # go through each cell in the 9x9 matrix
        for j in range(9):
            for k in range(9):
                if input_sudoku.iloc[j,k] == i:
                    temp.iloc[j,k] = False
                    # set 3x3, horizontal, and vertical to False
                    temp = mark_availability(temp, j, k)
                elif input_sudoku.iloc[j,k] != 0:
                    temp.iloc[j,k] = False
                else:
                    continue
        print(temp)
        numbers_availability.append(temp)
    return numbers_availability

def early_stopping(sudoku, old_number_of_blank) -> bool:
    # early stopping if the sudoku cannot be further solved
    new_number_of_blank = count_blank_cell(sudoku)
    if new_number_of_blank == old_number_of_blank:
        return True
    else:
        return False

if __name__ == '__main__':
    # get input
    input_sudoku = input("Tell me the sudoku: ") 
    # Try to insert a value in the blank cell, check functionality of insert_9x9_element
    # 023456789456789123789123450234567891567891234891234567345678912678912345912345678
    # 900500000687340050004107030040026008026051490091403062002700905000000301500009607
    # 900310004002000600000056809024680000000003001630000400008000150291064730560178940
    sudoku = transform_str_to_df(input_sudoku)
    print(validate_intermediate_3x3(get_square(sudoku, 'top', 'top')))
    print(validate_intermediate_hline(get_hline(sudoku, 0)))
    print(validate_intermediate_vline(get_vline(sudoku, 0)))
    
