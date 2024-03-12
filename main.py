import pandas as pd
import yfinance as yf
import os
import test
from validate import *
import retrieve

if __name__ == '__main__':
  # get input
  input_sudoku = input("Tell me the sudoku: ") 
  #'1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'
  # 123456789456789123789123456234567891567891234891234567345678912678912345912345678
  res = retrieve.transform_str_to_df(input_sudoku)
  print(validate_9x9(res))
  print(res)

