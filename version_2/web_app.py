import streamlit as st
import pandas as pd
import numpy as np
import main

def solver_st(input_sudoku):
    # Display the DataFrame
    # st.write("### Excel Data")
    # st.dataframe(input_sudoku)

    # Solve the sudoku
    completed_sudoku = main.solver(input_sudoku)
    st.write(completed_sudoku)

def app():
    st.title("Sudoku Solver")

    # Display a info message
    # with st.expander("ℹ️ How to use Sudoku Solver"):
    #     st.write("""
    #     This page allows you to 
    #     """)
    data_type = st.radio(
        "Would you like to upload an Sudoku Image or fill a form?",
        ["Fill a Form", "Upload Sudoku Image", ],
        horizontal=True,
        key = 'data_type'
        )
    if data_type == "Upload Sudoku Image":
        # File upload widget
        uploaded_file = st.file_uploader("Choose an Sudoku Image", type=["jpg", "jpeg", "png"])

        st.warning('Computer Vision is under construction', icon="⚠️")
        if uploaded_file is not None:
            # Read the Excel file into a DataFrame
            excel_data = pd.read_excel(uploaded_file ,usecols=['stock_symbol','number_of_shares','target_percentage'])
            # Rebalance the portfolio
            solver_st(excel_data)

    elif data_type == "Fill a Form":
        if 'data' not in st.session_state:
            st.session_state['data'] = pd.DataFrame(columns=['stock_symbol','number_of_shares','target_percentage'])


        fill_input_type = st.radio(
            "Would you like to type sequence of number or one by one?",
            [ "One by One", "Sequence",],
            horizontal=True,
            key = 'fill_input_type'
            )
        st.write(fill_input_type)
        if fill_input_type == "Sequence":
            # Add a text input for stock symbol
            input_sudoku = st.text_input("Sudoku input row by row \n\n 0 represent empty cell \n\n\
                                         E.g. 900310004002000600000056809024680000000003001630000400008000150291064730560178940")
        
        elif fill_input_type == "One by One":
            # 
            st.write("### Fill the Sudoku")
            input_sudoku = []
            for i, col in enumerate(st.columns(9) * 9):
                exec(f"input_sudoku.append(str(col.number_input(str(i),min_value = 1 , max_value = 9, value = None, key = i, label_visibility = 'collapsed')))")
            input_sudoku = ''.join(input_sudoku)
            input_sudoku = input_sudoku.replace('None', '0')
            
        # Create a submit button and add a label
        solve_button = st.button(label='Find a Solution!',)

        if solve_button:
            solver_st(input_sudoku)


        # Create a button to remove last row
        remove = st.button("Reset", type="primary")
        

if __name__ == "__main__":
    app()
