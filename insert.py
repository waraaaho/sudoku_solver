import validate
import retrieve
import time


# insert a element in 9x9 sudoku
def insert_9x9_element(sudoku, row, col):
    """
    insert a value iteratively [1,9] for a blank cell in 9x9 sudoku
    save the value iff a single value is valid for the cell
    """
    answer = 0
    i_pos = retrieve.get_position_name_by_index(row)
    j_pos = retrieve.get_position_name_by_index(col)

    for i in range(1,10):
        sudoku.iloc[row,col] = i 
        # validate the sudoku in 3x3, horizontal, and vertical
        if validate.validate_intermediate_3x3(retrieve.get_square(sudoku, i_pos, j_pos)) \
            and validate.validate_intermediate_hline(retrieve.get_hline(sudoku, row)) \
                and validate.validate_intermediate_vline(retrieve.get_vline(sudoku, col)):
            # restore blank cell if the sudoku is valid for multiple value in blank cell
            if answer != 0:
                sudoku.iloc[row,col] = 0
                print(f"failed to insert value at {row}-{col}")
                return sudoku
            # store value if the sudoku is valid
            answer = i 

    # insert the value in the blank cell and return
    sudoku.iloc[row,col] = answer
    print(f"inserted {answer} at {i_pos}-{j_pos}")
    return sudoku

# attempt to insert element in 9x9 sudoku for each blank cell
def insert_9x9(sudoku):
    """
    insert a value iteratively [1,9] for a blank cell in 9x9 sudoku
    save the value iff a single value is valid for the cell
    """
    for i in range(9):
        for j in range(9):
            if sudoku.iloc[i,j] == 0:
                # insert a value in the blank cell
                print(f"inserting value at {i}-{j}")
                time.sleep(0)
                sudoku = insert_9x9_element(sudoku, i, j)
    return sudoku

# attempt to insert element in 9x9 sudoku until the sudoku is completed
def start_insertion(sudoku, iteration_limit = 1000):
    """
    insert a value iteratively [1,9] for a blank cell in 9x9 sudoku
    save the value iff a single value is valid for the cell
    """
    iteration = 0
    while retrieve.count_blank_cell(sudoku) > 0:
        sudoku = insert_9x9(sudoku)
        iteration += 1
        if iteration%10 == 0:
            print(f"iteration {iteration}")
        if iteration >= iteration_limit:
            print(f"Solution Not Found, iteration limit reached {iteration}")
            break

    else:   
        print("Solution found")

    
    return sudoku

if __name__ == '__main__':
  # get input
  input_sudoku = input("Tell me the sudoku: ") 
  # Try to insert a value in the blank cell, check functionality of insert_9x9_element
  # 023456789456789123789123450234567891567891234891234567345678912678912345912345678
  # 900500000687340050004107030040026008026051490091403062002700905000000301500009607
  # 900310004002000600000056809024680000000003001630000400008000150291064730560178940
  sudoku = retrieve.transform_str_to_df(input_sudoku)
  print(sudoku)
  print(start_insertion(sudoku))
  print(sudoku)