# Exercise 1: Import pandas and numpy and check version:
import pandas as pd
import numpy as np
print("Exercise 1:")
print(pd.__version__)
print(np.__version__)

# Exercise 2: Create pandas series from list, np array, and dict:
my_list = list("abcdefghijklmnopqrstuvwxyz")
my_arr = np.arange(26)
my_dict = dict(zip(my_list, my_arr))

my_series_1 = pd.Series(my_list)
my_series_2 = pd.Series(my_arr)
my_series_3 = pd.Series(my_dict)

print("Exercise 2:")
print(my_series_1)
print(my_series_2)
print(my_series_3)

#Exercise 3: Convert the index of series "my_series_3" into a column of a dataframe:
my_df = my_series_3.reset_index()
print(my_df)


