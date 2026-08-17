"""
Q1: Create a DataFrame for student marks and print basic information like shape, columns, and
data types.
data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}
"""

import pandas as pd

def main():
    Border="-"*50
    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82]
        }

    # Create Dataframe
    df = pd.DataFrame(data)
    print(Border)
    print(df)

    print(Border)   
    print("DataFrame Shape :", df.shape)
    print(Border)    

    print("DataFrame Columns :", df.columns.to_list())
    print(Border)

    print("Data Types :\n", df.dtypes)
    print(Border)

if __name__ == "__main__":
    main()