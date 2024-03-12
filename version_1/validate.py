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
    # rules: False if dulicate element in 3x3 dataframe that is not 0
    element_counts = sudoku_3x3.value_counts()
    for i in range(1,10):
        try:
            # if element is not 0 and count is more than 1
            if element_counts[i] > 1:
                print(f"Duplicated element {i} in 3x3")
                return False
        except:
            # intermidiate sudoku allows absent of element, warning message only
            print(f"Element {i} does not exist in the 3x3")
    return True

def validate_intermediate_hline(hline):
    # rules: False if dulicate element in hline that is not 0
    element_counts = hline.value_counts()
    for i in range(1,10):
        try:
            # if element is not 0 and count is more than 1
            if element_counts[i] > 1:
                print(f"Duplicated element {i} in hline")
                return False
        except:
            # intermidiate sudoku allows absent of element, warning message only
            print(f"Element {i} does not exist in the hline")
    return True

def validate_intermediate_vline(vline):
    # rules: False if dulicate element in vline that is not 0
    element_counts = vline.value_counts()
    for i in range(1,10):
        try:
            # if element is not 0 and count is more than 1
            if element_counts[i] > 1:
                print(f"Duplicated element {i} in vline")
                return False
        except:
            # intermidiate sudoku allows absent of element, warning message only
            print(f"Element {i} does not exist in the vline")
    return True

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