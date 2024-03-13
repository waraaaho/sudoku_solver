import validate_v2
import retrieve
import time


# insert a element in 9x9 sudoku
def insert_9x9_element(sudoku, numbers_availability, row, col):
    """
    insert a value iteratively [1,9] for a blank cell in 9x9 sudoku
    save the value iff a single value is valid for the cell
    """
    i_pos = retrieve.get_position_name_by_index(row)
    j_pos = retrieve.get_position_name_by_index(col)

    for i in range(1,10):
        number_availability = numbers_availability[i-1]
        # check if the number is available in the cell
        if number_availability.iloc[row,col] == False:
            continue
        # validate the sudoku in 3x3, horizontal, and vertical by checking the number_availability
        if validate_v2.validate_intermediate_3x3(retrieve.get_square(number_availability, i_pos, j_pos)) \
            or validate_v2.validate_intermediate_hline(retrieve.get_hline(number_availability, row)) \
                or validate_v2.validate_intermediate_vline(retrieve.get_vline(number_availability, col)):
            
            # store the number if the sudoku is valid
            sudoku.iloc[row,col] = i
            print(f"inserted {i} at {i_pos}-{j_pos}")

            # mark the availability of number in the number_availability
            number_availability = validate_v2.mark_availability(number_availability, row, col)
            # pd is pass by reference, so no need to return the number_availability
            #numbers_availability[i-1] = number_availability
            # Not available for others number as the cell now occupied
            for j in range(9):
                numbers_availability[j].iloc[row,col] = False
            break
    return sudoku

# attempt to insert element in 9x9 sudoku for each blank cell
def insert_9x9(sudoku, numbers_availability):
    """
    insert a value iteratively [1,9] for a blank cell in 9x9 sudoku
    save the value iff a single value is valid for the cell
    """
    for i in range(9):
        for j in range(9):
            if sudoku.iloc[i,j] == 0:
                # insert a value in the blank cell
                #print(f"inserting value at {i}-{j}")
                time.sleep(0)
                sudoku = insert_9x9_element(sudoku, numbers_availability, i, j)
    return sudoku

# attempt to insert element in 9x9 sudoku until the sudoku is completed
def start_insertion(sudoku, numbers_availability, iteration_limit = 100):
    """
    insert a value iteratively [1,9] for a blank cell in 9x9 sudoku
    save the value iff a single value is valid for the cell
    """
    print(f"Number of blanks: {retrieve.count_blank_cell(sudoku)}")
    iteration = 0
    while retrieve.count_blank_cell(sudoku) > 0:
        #print(f"{iteration}-th sudoku: {sudoku}")
        sudoku = insert_9x9(sudoku, numbers_availability)
        iteration += 1
        if iteration%10 == 0:
            print(f"iteration {iteration}")
        if iteration >= iteration_limit:
            print(f"Solution Not Found, iteration limit reached {iteration}")
            break

    else:   
        print("Solution found")

    print(f"Simulation ended at iteration {iteration} with {retrieve.count_blank_cell(sudoku)} blanks left")
    return sudoku

if __name__ == '__main__':
    # get input
    input_sudoku = input("Tell me the sudoku: ") 
    # Try to insert a value in the blank cell, check functionality of insert_9x9_element
    # 023456789456789123789123450234567891567891234891234567345678912678912345912345678
    # 900500000687340050004107030040026008026051490091403062002700905000000301500009607
    # original
    # 900310004002000600000056809024680000000003001630000400008000150291064730560178940
    # 1000 tries
    # 986310004002800603300056809124680300800003061630001480008030156291564738563178942
    # 2000 tries
    # 986310504052800603300056809124685390805003061630001485008030156291564738563178942
    # 3000 tries
    # 986310504052800613310056809124685397805003261639021485008030156291564738563178942
    # 4000 tries
    # 9 8 6 3 1 0 5 7 4 4 5 2 8 0 7 6 1 3 3 1 7 4 5 6 8 0 9 1 2 4 6 8 5 3 9 7 87 5 0 4 3 2 6 1 6 3 9 7 2 1 4 8 5 7 4 8 0 3 0 1 5 6 2 9 1 5 6 4 7 3 8 5 63 1 7 8 9 4 2
    # 4006 tries
    #9 8 6 3 1 2 5 7 4 4 5 2 8 9 7 6 1 3 3 1 7 4 5 6 8 2 9 1 2 4 6 8 5 3 9 7 87 5 9 4 3 2 6 1 6 3 9 7 2 1 4 8 5 7 4 8 2 3 9 1 5 6 2 9 1 5 6 4 7 3 8 5 63 1 7 8 9 4 2
    sudoku = retrieve.transform_str_to_df(input_sudoku)
    numbers_availability = validate_v2.create_numbers_availability(sudoku)
    print(start_insertion(sudoku, numbers_availability,100))
    print(sudoku.values.reshape(-1))